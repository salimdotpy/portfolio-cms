from flask import render_template
from models import GeneralSetting, Transaction, User, Admin, UserWallet, AdminNotification, db
from helper import to_dict

class AdminController():
    def dashboard():
        pageTitle = "Dashboard"
        # User info
        widget={}
        widget['total_users'] = User.query.count()
        widget['veried_users'] = User.query.filter_by(status=1).count()
        widget['email_unverified_users'] = User.query.filter_by(ev=0).count()
        widget['sms_unverified_users'] = User.query.filter_by(sv=0).count()
        general = GeneralSetting.query.count()
        totalWallet = UserWallet.query.count()
        totalReceive = Transaction.query.count()
        front = to_dict(User.query.all(), User)
        totalTrx = Transaction.query.count()
        return render_template('admin/dashboard.html', widget = widget, general=general, totalWallet=totalWallet, totalReceive=totalReceive, totalTrx=totalTrx, front=front, pageTitle=pageTitle)
    
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