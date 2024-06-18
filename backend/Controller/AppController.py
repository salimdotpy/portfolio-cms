from flask import render_template, request, redirect, flash

from models import Frontend, Page
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr
from helper import getContent, activeTemplate

class AppController():
    def home():
        pageTitle = "Home"
        section = Page.query.filter_by(tempname=activeTemplate(), slug='home').first()
        #['about', 'facts', 'skills', 'resume', 'portfolio', 'services', 'testimonials', 'contact']
        return render_template('basic/home.html', pageTitle=pageTitle, section=section.to_dict())
    
    def portfolio():
        pageTitle = "Portfolio"
        section = Page.query.filter_by(tempname=activeTemplate(), slug='portfolio').first()
        return render_template('basic/portfolio.html', pageTitle=pageTitle, section=section.to_dict())
    
    def contact_us():
        contact = getContent('contact.content', True)['data_values']['email']
        name = request.form['name']
        sender = formatter(name, request.form['email'])
        subject = request.form['subject']
        message = request.form['message']
        try:
            send_email(sender, contact, subject, message)
            flash(f'Hi {name}, Your message has been sent. Thank you!', ('success'))
            return redirect(request.referrer)
        except:
            flash('Unable to send your message', ('error'))
            return redirect(request.referrer)

    def portfolio_details(id):
        pageTitle = "Portfolio Details"
        data = Frontend.query.get(id); data = data.to_dict()#to_dict(data, Frontend) or abort(404)
        return render_template('basic/portfolio_details.html', pageTitle=pageTitle, data=data, id=id)
    
    def handel_404(error):
        pageTitle = "404 | Page not found"
        return render_template('errors/404.html', pageTitle=pageTitle), 404
    
    def handel_419(error):
        pageTitle = "419 | Session has expired"
        return render_template('errors/419.html', pageTitle=pageTitle)
    
def send_email(sender, receiver, subject, body):
    # Create a MIME multipart message
    message = MIMEMultipart()
    message['Subject'] = subject
    message['From'] = sender
    message['To'] = receiver#', '.join(receiver)

    # Attach the body of the email
    message.attach(MIMEText(f'You have a new message from:\n{sender}\nbody:\n{body}', 'plain'))

    # Connect to the SMTP server and send the email
    crd_email = 'osenikamorudeen36@gmail.com'
    crd_password = 'pwwgffcfjnvrrcon'
    smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
    smtp_server.starttls()
    smtp_server.login(crd_email, crd_password)
    smtp_server.sendmail(sender, receiver, message.as_string())
    smtp_server.quit()
def formatter(name:str, email:str)->str:
    return formataddr((name, email))