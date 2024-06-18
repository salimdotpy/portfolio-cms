from flask import Flask, jsonify, request, session
from flask_wtf.csrf import CSRFProtect, generate_csrf
from Controller.Admin.AdminController import AdminController
from Controller.Admin.FrontendController import FrontController
from Controller.Admin.GeneralSettingController import GeneralSettingController 
from Controller.AppController import AppController 
from Controller.Admin.PageBuilderController import PageBuilderController
from Controller.Admin.EmailTemplateController import EmailTemplateController
from flask_restful import Api
from flask_cors import CORS
from Resources.Frontend import FrontendApi
from models import db
import config

app = Flask(__name__)
app.secret_key = b'salimtech'

app.config.from_object(config)

# Initialize the Flask-SQLAlchemy object.
db.init_app(app)
csrf = CSRFProtect(app)

# Create the Flask-RESTful API manager.
CORS(app, supports_credentials=True, origins=["http://localhost:3000"])
api = Api(app)

# |--------------------------------------------------------------------------
# | Error Routes
# |--------------------------------------------------------------------------
app.register_error_handler(404, AppController.handel_404)
app.register_error_handler(500, AppController.handel_419)

# |--------------------------------------------------------------------------
# | Admin Routes
# |--------------------------------------------------------------------------
app.add_url_rule('/admin','admin.login', AdminController.login, methods=['GET', 'POST'])
app.add_url_rule('/admin/dashboard','dashboard', AdminController.dashboard)
app.add_url_rule('/admin/profile', 'profile', AdminController.profile)
app.add_url_rule('/notifications', 'notifications', AdminController.notifications)
app.add_url_rule('/admin/read/<id>','read', AdminController.notificationRead)

app.add_url_rule('/admin/seo', 'seo', FrontController.seoEdit)
app.add_url_rule('/general-setting', 'setting.index', GeneralSettingController.index)
app.add_url_rule('/general-setting', 'setting.update', GeneralSettingController.update, methods=['POST'])

app.add_url_rule('/setting/logo-icon', 'setting.logo.icon', GeneralSettingController.logoIcon)
app.add_url_rule('/setting/logo-icon', 'setting.logo.update', GeneralSettingController.logoIconUpdate, methods=['POST'])
app.add_url_rule('/custom-css', 'setting.custom.css', GeneralSettingController.customCss)
app.add_url_rule('/custom-css', 'setting.custom.update', GeneralSettingController.customCssSubmit, methods=['POST'])

app.add_url_rule('/admin/frontend/frontend-sections/<key>','sections', 
                 FrontController.frontSections)
app.add_url_rule('/admin/frontend/frontend-content','sections.content', 
                 FrontController.frontContent, methods=["GET", "POST"])
app.add_url_rule('/admin/frontend/frontend-element/<key>/<id>','sections.element', 
                 FrontController.frontElement)
app.add_url_rule('/admin/frontend/remove','remove', 
                 FrontController.remove, methods=["GET", "POST"])


app.add_url_rule('/admin/email-template/global','email.template.global', 
                 EmailTemplateController.emailTemplate)
app.add_url_rule('/admin/email-template/global','email.global.update', 
                 EmailTemplateController.emailTemplateUpdate, methods=['POST'])
app.add_url_rule('/admin/email-template/setting','email.template.setting', 
                 EmailTemplateController.emailSetting)
app.add_url_rule('/admin/email-template/setting','email.setting.update', 
                 EmailTemplateController.emailSettingUpdate, methods=['POST'])
app.add_url_rule('/admin/email-template/index','email.template.index', 
                 EmailTemplateController.index)
app.add_url_rule('/admin/email-template/<id>/edit','email.template.edit', 
                 EmailTemplateController.edit)
app.add_url_rule('/admin/email-template/<id>/update','email.template.update', 
                 EmailTemplateController.update, methods=['POST'])

app.add_url_rule('/admin/frontend/manage-pages','manage.pages', 
                 PageBuilderController.managePages)
app.add_url_rule('/admin/frontend/manage-pages/','manage.pages.save', PageBuilderController.managePagesSave, methods=['POST'])
app.add_url_rule('/admin/frontend/manage-pages/update','manage.pages.update', PageBuilderController.managePagesUpdate, methods=['POST'])
app.add_url_rule('/admin/frontend/manage-pages/delete','manage.pages.delete', PageBuilderController.managePagesDelete, methods=['POST'])
app.add_url_rule('/admin/frontend/manage-section/<id>','manage.section', PageBuilderController.manageSection)
app.add_url_rule('/admin/frontend/manage-section/<id>','manage.section.update', PageBuilderController.manageSectionUpdate, methods=['POST'])

# app route

# |--------------------------------------------------------------------------
# | User Routes
# |--------------------------------------------------------------------------
app.add_url_rule('/','home', AppController.home)
app.add_url_rule('/portfolio','portfolio', AppController.portfolio)
app.add_url_rule('/','contact.us', AppController.contact_us, methods=["POST"])
app.add_url_rule('/portfolio-details/<id>','portfolio.details', AppController.portfolio_details)

@app.route('/get-csrf-token', methods=['GET'])
def get_csrf_token():
    token = generate_csrf()
    response = jsonify({'csrf_token': token})
    return response

# Create the endpoints.
api.add_resource(FrontendApi,'/api', '/api/<int:id>')