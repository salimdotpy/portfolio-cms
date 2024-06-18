from flask import  render_template, abort, request, session, flash, url_for, redirect
from models import Page, db
from helper import getPageSections, activeTemplate, imagePath, removeFile
import json

class PageBuilderController():
    def managePages():
        # HOME PAGE
        count = Page.query.filter_by(tempname=activeTemplate(), slug='home').count()
        if count == 0:
            page = Page(tempname=activeTemplate(), name='Home', slug='home')
            db.session.add(page)
            db.session.commit()

        pdata = Page.query.filter_by(tempname=activeTemplate()).all()
        pdata = [{'id':e.id, 'name': e.name, 'slug': e.slug, 'tempname': e.tempname, 'secs': eval(str(e.secs)), 'is_default': e.is_default, 'created_at': e.created_at, 'updated_at': e.updated_at} for e in pdata]
        pageTitle = 'Manage Section'
        emptyMessage = 'No Page Created Yet'
        return render_template('/admin/frontend/builder/pages.html', pageTitle=pageTitle, pdata=pdata, emptyMessage=emptyMessage)

    def managePagesSave():
        slug = request.form['slug']
        name = request.form['name']
        exist = Page.query.filter_by(tempname=activeTemplate(), slug=slug).count()
        if exist != 0:
            flash('This page already exists on your current template. Please change the slug.', ('error'))
            return redirect(request.referrer)
        page = Page(tempname=activeTemplate(), name=name, slug=slug)
        db.session.add(page)
        db.session.commit()
        flash('New page added successfully', ('success'))
        return redirect(request.referrer)

    def managePagesUpdate():
        id = request.form['id']
        slug = request.form['slug']
        name = request.form['name']
        page = Page.query.get(id)
        
        exist = Page.query.filter_by(tempname=activeTemplate(), slug=slug).first()
        if exist and exist.slug != page.slug:
            flash('This page already exist on your current template. please change the slug.', ('error'))
            return redirect(request.referrer)

        page.name = name
        page.slug = slug
        db.session.commit()
        flash('Update successfully', ('success'))
        return redirect(request.referrer)

    def managePagesDelete():
        id = request.form['id']
        db.session.query(Page).filter(Page.id == id).delete()
        db.session.commit()
        flash('Page deleted successfully', ('success'))
        return redirect(request.referrer)
        
    def manageSection(id):
        pdata = Page.query.filter_by(id=id).first().to_dict()
        pageTitle = 'Manage Section of '+pdata['name']
        sections =  getPageSections(True)
        return render_template('/admin/frontend/builder/index.html', pageTitle=pageTitle, pdata=pdata, sections=sections)
        
    def manageSectionUpdate(id):
        page = Page.query.get(id)
        if not request.form.getlist('secs[]'):
            page.secs = None
        else:
            page.secs = str(request.form.getlist('secs[]'))
        db.session.commit()
        flash('Updated successfully', ('success'))
        return redirect(request.referrer)
