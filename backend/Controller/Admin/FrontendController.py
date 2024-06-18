from flask import  render_template, abort, request, session, flash, url_for, redirect
from models import Frontend, db
from helper import getPageSections, uploadImage, imagePath, removeFile
import json

class FrontController():
    def seoEdit():
        pageTitle = 'SEO Configuration'
        seo = Frontend.query.filter_by(data_keys='seo.data').order_by(Frontend.id.desc()).first()
        seo = seo.to_dict()
        if not seo:
            data_values = '{"keywords":["admin","blog"],"description":"Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit","social_title":"WEBSITENAME","social_description":"Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit","image":null}'
            data_values = json.load(data_values)
            
            new_ = Frontend(data_keys='seo.data', data_values=data_values)
            db.session.add(new_)
            db.session.commit()
        return render_template('/admin/frontend/seo.html', pageTitle=pageTitle, seo=seo)

    def frontSections(key):
        try:
            section = getPageSections()[key]
        except:
            return abort(403)
        try:
            content = Frontend.query.filter_by(data_keys=key+'.content').order_by(Frontend.id.desc()).first()
            content = content.to_dict()
        except:
            content=False
        elements = Frontend.query.filter_by(data_keys=key+'.element').order_by(Frontend.id.desc()).all()
        
        elements = [{'id': e.id, 'data_keys': e.data_keys, 'data_values': eval(e.data_values),'created_at': e.created_at, 'updated_at': e.updated_at} for e in elements]
        
        pageTitle = section['name']
        emptyMessage = 'No item created yet.'
        try:
            imgCount = section['content']['images']
            imgCount = len(imgCount)
        except:
            imgCount = False
        # return widget
        return render_template('admin/frontend/index.html', section=section, content=content, elements=elements, key=key, pageTitle=pageTitle, emptyMessage=emptyMessage, imgCount=imgCount)
    
    def frontElement(key, id = False):
        section = getPageSections()[key]
        if not section:
            return abort(404)

        section['element'].pop('modal', None)
        pageTitle = section['name'] + ' Items'
        try:
            imgCount = section['element']['images']
            imgCount = len(imgCount)
        except:
            imgCount = False
        
        if id and id !='0':
            data = Frontend.query.get(id); data = data.to_dict()
            return render_template('admin/frontend/element.html', section=section, key=key, pageTitle=pageTitle, data=data, imgCount=imgCount)
        return render_template('admin/frontend/element.html', section=section, key=key, pageTitle=pageTitle, imgCount=imgCount)
    
    def except_(key, arrs):
        for arr in arrs:
            if key.startswith(arr) and key != 'keywords[]':
                return False
        return True

    def frontContent():
        key = request.form['key']
        valInputs = request.form
        inputContentValue = {}
        for keyName, input in valInputs.items(): 
            if FrontController.except_(keyName,['csrf_token', 'image_input', 'key', 'status', 'type', 'id']):
                if keyName.endswith('[]'):
                    inputContentValue[keyName[:-2]] = valInputs.getlist(keyName)
                    continue
                inputContentValue[keyName] = input
        type = request.form['type']
        if not type: abort(404)
        try: imgJson = getPageSections()[key][type]['images'] 
        except: imgJson = False
        if 'id' in request.form:    
            contentD = Frontend.query.get(request.form['id']) 
            content = contentD.to_dict()
        else:
            contentD = Frontend.query.filter_by(data_keys=key+'.'+type).first()
            content = contentD.to_dict()
            if not contentD or type == 'element':
                contentD = Frontend(data_keys=key+'.'+type)
                db.session.add(contentD)
                # db.session.commit()
        if type == 'data':
            inputContentValue['image'] = content['data_values']['image']
            if request.files['image_input']:
                image_input = request.files['image_input']
                try:
                    inputContentValue['image'] = uploadImage(image_input,imagePath()['seo']['path'], imagePath()['seo']['size'], content['data_values']['image'])
                except:
                    flash('Could not upload the image.', ('error'))
                    return redirect(request.referrer)
            
        else:
            if imgJson:
                for imgKey, imgValue in imgJson.items():
                    imgData = request.files.getlist(f'image_input[{imgKey}]')[0]
                    if imgData:
                        try:
                            inputContentValue[imgKey] = FrontController.storeImage(imgJson,type,key,imgData,imgKey,content['data_values'][imgKey])
                        except:
                            flash('Could not upload the image.', ('error'))
                            return redirect(request.referrer)
                        
                    elif content['data_values'][imgKey] and 'id' in request.form:
                        inputContentValue[imgKey] = content['data_values'][imgKey]
                    elif content['data_values'][imgKey] and type == 'content':
                        inputContentValue[imgKey] = content['data_values'][imgKey]
                    else:
                        inputContentValue[imgKey] = ''#content['data_values'][imgKey]
        contentD.data_values = str(inputContentValue)
        db.session.commit()
        flash('Content has been updated.', ('success'))
        return redirect(request.referrer)
    
    def storeImage(imgJson,type,key,image,imgKey,old_image = None):
        path = 'assets/images/frontend/'+key
        if type == 'element' or type == 'content':
            size = imgJson[imgKey]['size']
            # thumb = imgJson[imgKey]['thumb']
        else:
            path = imagePath()[key]['path']
            size = imagePath()[key]['size']
            # thumb = imagePath()[key]['thumb']
        return uploadImage(image, path, size, old_image)

    def remove():
        id = request.form['id']
        frontends = Frontend.query.get(id); frontend = frontends.to_dict() #to_dict(frontends, Front)
        key = frontend['data_keys'].split('.')[0]
        type = frontend['data_keys'].split('.')[1]
        if type == 'element' or type == 'content':
            path = 'assets/images/frontend/'+key
            try:imgJson = getPageSections()[key][type]['images']
            except: imgJson = False
            if imgJson:
                for imgKey, imgValue in imgJson.items():
                    removeFile(path+'/'+frontend['data_values'][imgKey])
        db.session.query(Frontend).filter(Frontend.id == id).delete()
        db.session.commit()
        flash('Content has been removed.', ('success'))
        return redirect(request.referrer)
