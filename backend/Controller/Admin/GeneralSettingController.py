from flask import  render_template, request, flash, url_for, redirect
from models import GeneralSetting, db
from helper import uploadImage, imagePath
import json

class GeneralSettingController():
    def index():
        general = GeneralSetting.query.first()
        pageTitle = 'General Setting'
        jsonUrl = 'templates/admin/partials/timezone.json'
        with open(jsonUrl, 'r') as file:
            timezones = json.load(file)
        return render_template('/admin/setting/general_setting.html', pageTitle=pageTitle, general=general, timezones=timezones)

    def update():
        general = GeneralSetting.query.first()
        general.ev = 1 if request.form.get('ev') else 0
        general.en = 1 if request.form.get('en') else 0
        general.sv = 1 if request.form.get('sv') else 0
        general.sn = 1 if request.form.get('sn') else 0
        general.force_ssl = 1 if request.form.get('force_ssl') else 0
        general.secure_password = 1 if request.form.get('secure_password') else 0
        general.registration = 1 if request.form.get('registration') else 0
        general.agree = 1 if request.form.get('agree') else 0
        general.sitename = request.form['sitename']
        general.base_color = request.form['base_color']
        general.secondary_color = request.form['secondary_color']
        db.session.commit()
        flash('General setting has been updated.', ('success'))
        return redirect(request.referrer)
    def logoIcon():
        pageTitle = 'Logo & Favicon'
        return render_template('/admin/setting/logo_icon.html', pageTitle=pageTitle)

    def logoIconUpdate():
        if request.files['logo']:
            try:
                path = imagePath()['logoIcon']['path']
                uploadImage(request.files['logo'], path, name='logo.png')
            except:
                flash('Logo could not be uploaded.', ('error'))
                return redirect(request.referrer)
        
        if request.files['favicon']:
            try:
                path = imagePath()['logoIcon']['path']
                uploadImage(request.files['favicon'],imagePath()['logoIcon']['path'], imagePath()['favicon']['size'], name='favicon.png')
            except:
                flash('Logo could not be uploaded.', ('error'))
                return redirect(request.referrer)
        flash('Logo & favicon has been updated.', ('success'))
        return redirect(request.referrer)

    def customCss():
        pageTitle = 'Custom CSS'
        path = url_for('static', filename='assets/basic/css/custom.css')[1:]
        with open(path, 'r') as file:
            file_content = file.read()
        return render_template('/admin/setting/custom_css.html', pageTitle=pageTitle, file_content=file_content)

    def customCssSubmit():
        path = url_for('static', filename='assets/basic/css/custom.css')[1:]
        file = open(path, 'w')
        file.write(request.form['css'].replace('\n', ''))
        file.close()
        flash('CSS updated successfully', ('success'))
        return redirect(request.referrer)

#     public function optimize(){
#         Artisan::call('optimize:clear');
#         $notify[] = ['success','Cache cleared successfully'];
#         return back()->withNotify($notify);
#     }


#     public function cookie(){
#         $pageTitle = 'GDPR Cookie';
#         $cookie = Frontend::where('data_keys','cookie.data')->firstOrFail();
#         return view('admin.setting.cookie',compact('pageTitle','cookie'));
#     }

#     public function cookieSubmit(Request $request){
#         $request->validate([
#             'link'=>'required',
#             'description'=>'required',
#         ]);
#         $cookie = Frontend::where('data_keys','cookie.data')->firstOrFail();
#         $cookie->data_values = [
#             'link' => $request->link,
#             'description' => $request->description,
#             'status' => $request->status ? 1 : 0,
#         ];
#         $cookie->save();
#         $notify[] = ['success','Cookie policy updated successfully'];
#         return back()->withNotify($notify);
#     }
# }
