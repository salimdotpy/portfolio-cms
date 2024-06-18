from flask import render_template, request, redirect, flash
from models import EmailSMSTemplate, GeneralSetting, db
from helper import to_dict

class EmailTemplateController():
    def index():
        pageTitle = 'Email Templates'
        emptyMessage = 'No templates available'
        email_templates = EmailSMSTemplate.query.all()
        return render_template('admin/email_template/index.html', pageTitle=pageTitle, emptyMessage=emptyMessage, email_templates=email_templates)
    
    def edit(id):
        email_template = EmailSMSTemplate.query.get(id)
        email_template = email_template.to_dict()
        pageTitle = email_template['name']
        emptyMessage = 'No shortcode available'
        return render_template('admin/email_template/edit.html', pageTitle=pageTitle, emptyMessage=emptyMessage, email_template=email_template)

    def update(id):
        email_template = EmailSMSTemplate.query.get(id)
        email_template.subj = request.form['subject']
        email_template.email_body = request.form['email_body']
        email_template.email_status = 1 if request.form.get('email_status') else  0
        db.session.commit()

        flash(email_template.name+' template has been updated.', ('success'))
        return redirect(request.referrer)

    def emailSetting():
        pageTitle = 'Email Configuration'
        return render_template('admin/email_template/email_setting.html', pageTitle=pageTitle)

    def emailSettingUpdate():
        flash('Email configuration has been updated.', ('success'))
        return redirect(request.referrer)

    def emailTemplate():
        pageTitle = 'Global Email Template'
        return render_template('admin/email_template/email_template.html', pageTitle=pageTitle)

    def emailTemplateUpdate():
        general = GeneralSetting.query.first_or_404()
        general.email_from = request.form['email_from']
        general.email_template = request.form['email_template']
        db.session.commit()
        flash('Global email template has been updated.', ('success'))
        return redirect(request.referrer)

    def sendTestMail():
        general = GeneralSetting.query.first()
        config = general.mail_config
        receiver_name = request.form['email'].split('@')[0]
        subject = 'Testing ' + config.name + ' Mail'
        message = 'This is a test email, please ignore it if you are not meant to get this email.'

        try:
            print(request.form['email'], subject, message, receiver_name)
        except:
            flash('Invalid credential', ('error'))
            return redirect(request.referrer)
        
        flash('You should receive a test mail at ' + request.form['email'] + ' shortly.', ('success'))
        return redirect(request.referrer)
