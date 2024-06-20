from flask import render_template
from models import GeneralSetting, User, Admin, AdminNotification, db
from helper import to_dict

class AdminController():
    def dashboard():
        pageTitle = "Dashboard"
        # User info
        widget={}
        widget['total_users'] = User.query.count()
        general = GeneralSetting.query.count()
        return render_template('admin/dashboard.html', widget = widget, general=general, pageTitle=pageTitle)
    
    def profile():
        pageTitle = "Profile"
        admin = to_dict(Admin.query.first(), Admin)
        return admin
    
    def profileUpdate():
        pass

    def password():
        pageTitle = "Password Setting"
        admin = to_dict(Admin.query.first(), Admin)
        return admin
    
    def passwordUpdate():
        pass

    def notifications():
        pageTitle ="Notifications"
        notifications = to_dict(AdminNotification.query.order_by(AdminNotification.id.desc()).all(), AdminNotification)
        return notifications
    
    def notificationRead(id):
        notification = AdminNotification.query.get(id)
        notification.read_status = 1
        db.session.commit()
        return to_dict(notification, AdminNotification)
    def login():
        pageTitle = "Admin Login"
        return render_template('admin/auth/login.html', pageTitle=pageTitle)