from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Admin(db.Model):
    __tablename__ = "admins"
    id = db.Column(db.BigInteger(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(40, collation='utf8mb4_unicode_ci'), nullable=False)
    email = db.Column(db.String(40, collation='utf8mb4_unicode_ci'), nullable=False, unique=True)
    username = db.Column(db.String(40, collation='utf8mb4_unicode_ci'), nullable=False, unique=True)
    email_verified_at = db.Column(db.TIMESTAMP, nullable=True)
    image = db.Column(db.String(255, collation='utf8mb4_unicode_ci'), default=None, nullable=True)
    password = db.Column(db.String(255, collation='utf8mb4_unicode_ci'), nullable=False)
    created_at = db.Column(db.TIMESTAMP, nullable=True)
    updated_at = db.Column(db.TIMESTAMP, nullable=True)

class AdminNotification(db.Model):
    __tablename__ = "admin_notifications"
    id = db.Column(db.BigInteger(), primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer(), nullable=False, default=0)
    title = db.Column(db.String(255, collation='utf8mb4_unicode_ci'), nullable=True, default=None)
    read_status = db.Column(db.Boolean, nullable=False, default=False)
    click_url = db.Column(db.Text(collation='utf8mb4_unicode_ci'), nullable=True, default=None)
    created_at = db.Column(db.TIMESTAMP, nullable=True)
    updated_at = db.Column(db.TIMESTAMP, nullable=True)

class AdminPasswordReset(db.Model):
    __tablename__ = "admin_password_resets"
    id = db.Column(db.BigInteger(), primary_key=True, autoincrement=True)
    email = db.Column(db.String(40, collation='utf8mb4_unicode_ci'), nullable=False)
    token = db.Column(db.String(40, collation='utf8mb4_unicode_ci'), nullable=False)
    status = db.Column(db.Boolean, nullable=False, default=True)
    created_at = db.Column(db.TIMESTAMP, nullable=True)
    updated_at = db.Column(db.TIMESTAMP, nullable=True)

class EmailLog(db.Model):
    __tablename__ = "email_logs"
    id = db.Column(db.BigInteger(), primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer(), nullable=False)
    mail_sender = db.Column(db.String(40, collation='utf8mb4_unicode_ci'), nullable=True, default=None)
    email_from = db.Column(db.String(40, collation='utf8mb4_unicode_ci'), nullable=True, default=None)
    email_to = db.Column(db.String(40, collation='utf8mb4_unicode_ci'), nullable=True, default=None)
    subject = db.Column(db.String(255, collation='utf8mb4_unicode_ci'), nullable=True, default=None)
    message = db.Column(db.Text(collation='utf8mb4_unicode_ci'), nullable=True, default=None)
    created_at = db.Column(db.TIMESTAMP, nullable=True)
    updated_at = db.Column(db.TIMESTAMP, nullable=True)

class EmailSMSTemplate(db.Model):
    __tablename__ = "email_sms_templates"
    id = db.Column(db.BigInteger(), primary_key=True, autoincrement=True)
    act = db.Column(db.String(40, collation='utf8mb4_unicode_ci'), nullable=False)
    name = db.Column(db.String(40, collation='utf8mb4_unicode_ci'), nullable=False)
    subj = db.Column(db.String(255, collation='utf8mb4_unicode_ci'), nullable=False)
    email_body = db.Column(db.Text(collation='utf8mb4_unicode_ci'), default=None, nullable=True)
    sms_body = db.Column(db.Text(collation='utf8mb4_unicode_ci'), default=None, nullable=True)
    shortcodes = db.Column(db.Text(collation='utf8mb4_unicode_ci'), nullable=False)
    email_status = db.Column(db.Boolean, nullable=False, default=True)
    sms_status = db.Column(db.Boolean, nullable=False, default=True)
    created_at = db.Column(db.TIMESTAMP, nullable=True)
    updated_at = db.Column(db.TIMESTAMP, nullable=True)

    def to_dict(self):
        return {
            "id": self.id, "act": self.act, "name": self.name, "subj": self.subj, "email_body": self.email_body,
            "sms_body": self.sms_body, "shortcodes": eval(self.shortcodes), "email_status": self.email_status,
            "sms_status": self.sms_status, "created_at": self.created_at, "updated_at": self.updated_at
        }

class Extension(db.Model):
    __tablename__ = 'extensions'
    id = db.Column(db.BigInteger(), primary_key=True, autoincrement=True)
    act = db.Column(db.String(40, collation='utf8mb4_unicode_ci'), nullable=False)
    name = db.Column(db.String(40, collation='utf8mb4_unicode_ci'), nullable=False)
    description = db.Column(db.Text(collation='utf8mb4_unicode_ci'), default=None, nullable=True)
    image = db.Column(db.String(255, collation='utf8mb4_unicode_ci'), default=None, nullable=True)
    script = db.Column(db.Text(collation='utf8mb4_unicode_ci'), default=None, nullable=True)
    shortcode = db.Column(db.Text(collation='utf8mb4_unicode_ci'), default=None, nullable=True, comment='object')
    support = db.Column(db.Text(collation='utf8mb4_unicode_ci'), default=None, nullable=True, comment='help section')
    status = db.Column(db.Boolean, nullable=False, default=True, comment='1=>enable, 2=>disable')
    deleted_at = db.Column(db.DateTime, default=None, nullable=True)
    created_at = db.Column(db.TIMESTAMP, nullable=True)
    updated_at = db.Column(db.TIMESTAMP, nullable=True)


class Frontend(db.Model):
    __tablename__ = "fronts"
    id = db.Column(db.BigInteger(), primary_key=True, autoincrement=True)
    data_keys = db.Column(db.String(40, collation='utf8mb4_unicode_ci'), nullable=False)
    data_values = db.Column(db.Text(collation='utf8mb4_unicode_ci'), nullable=False)
    created_at = db.Column(db.TIMESTAMP, nullable=True)
    updated_at = db.Column(db.TIMESTAMP, nullable=True)

    def to_dict(self):
        return {
            'id':self.id,
            'data_keys': self.data_keys,
            'data_values': eval(str(self.data_values)),
            'created_at': str(self.created_at),
            'updated_at': str(self.updated_at)
        }

class GeneralSetting(db.Model):
    __tablename__ = "general_settings"
    id = db.Column(db.BigInteger(), primary_key=True, autoincrement=True)
    sitename = db.Column(db.String(40, collation='utf8mb4_unicode_ci'), default=None, nullable=True)
    last_cron = db.Column(db.String(255, collation='utf8mb4_unicode_ci'), default=None, nullable=True)
    usd_rate = db.Column(db.DECIMAL(18, 2), default=0.00)
    wallet_limit = db.Column(db.Integer, default=None, nullable=True)
    api = db.Column(db.String(255, collation='utf8mb4_unicode_ci'), default=None, nullable=True)
    api_version = db.Column(db.SmallInteger, default=0)
    pin = db.Column(db.String(255, collation='utf8mb4_unicode_ci'), default=None, nullable=True)
    wallet = db.Column(db.String(255, collation='utf8mb4_unicode_ci'), default=None, nullable=True)
    fixed_charge = db.Column(db.DECIMAL(18, 8), default=0.00000000)
    percent_charge = db.Column(db.DECIMAL(5, 2), default=0.00)
    cur_text = db.Column(db.String(40, collation='utf8mb4_unicode_ci'), default=None, nullable=True, comment='currency text')
    cur_sym = db.Column(db.String(40, collation='utf8mb4_unicode_ci'), default=None, nullable=True, comment='currency symbol')
    email_from = db.Column(db.String(40, collation='utf8mb4_unicode_ci'), default=None, nullable=True)
    email_template = db.Column(db.Text(collation='utf8mb4_unicode_ci'), default=None, nullable=True)
    sms_api = db.Column(db.String(255, collation='utf8mb4_unicode_ci'), default=None, nullable=True)
    base_color = db.Column(db.String(40, collation='utf8mb4_unicode_ci'), default=None, nullable=True)
    secondary_color = db.Column(db.String(40, collation='utf8mb4_unicode_ci'), default=None, nullable=True)
    mail_config = db.Column(db.Text(collation='utf8mb4_unicode_ci'), default=None, nullable=True, comment='email configuration')
    sms_config = db.Column(db.Text(collation='utf8mb4_unicode_ci'), default=None, nullable=True)
    ev = db.Column(db.Boolean, nullable=False, default=False, comment='email verification, 0 - dont check, 1 - check')
    en = db.Column(db.Boolean, nullable=False, default=False, comment='email notification, 0 - dont send, 1 - send')
    sv = db.Column(db.Boolean, nullable=False, default=False, comment='sms verication, 0 - dont check, 1 - check')
    sn = db.Column(db.Boolean, nullable=False, default=False, comment='sms notification, 0 - dont send, 1 - send')
    force_ssl = db.Column(db.Boolean, nullable=False, default=False)
    secure_password = db.Column(db.Boolean, nullable=False, default=False)
    agree = db.Column(db.Boolean, nullable=False, default=False)
    registration = db.Column(db.Boolean, nullable=False, default=False, comment='0: Off , 1: On')
    active_template = db.Column(db.String(40, collation='utf8mb4_unicode_ci'), default=None, nullable=True)
    sys_version = db.Column(db.Text(collation='utf8mb4_unicode_ci'), default=None, nullable=True)
    created_at = db.Column(db.TIMESTAMP, nullable=True)
    updated_at = db.Column(db.TIMESTAMP, nullable=True)

class Language(db.Model):
    __tablename__ = "languages"
    id = db.Column(db.BigInteger(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(40, collation='utf8mb4_unicode_ci'), nullable=False)
    code = db.Column(db.String(40, collation='utf8mb4_unicode_ci'), nullable=False)
    icon = db.Column(db.String(255, collation='utf8mb4_unicode_ci'), default=None, nullable=True)
    text_align = db.Column(db.Boolean, nullable=False, default=False, comment='0: left to right text align, 1: right to left text align')
    is_default = db.Column(db.Boolean, nullable=False, default=False, comment='0: not default language, 1: default language')
    created_at = db.Column(db.TIMESTAMP, nullable=True)
    updated_at = db.Column(db.TIMESTAMP, nullable=True)

class Page(db.Model):
    __tablename__ = "pages"
    id = db.Column(db.BigInteger(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(40, collation='utf8mb4_unicode_ci'), default=None, nullable=True)
    slug = db.Column(db.String(40, collation='utf8mb4_unicode_ci'), default=None, nullable=True)
    tempname = db.Column(db.String(40, collation='utf8mb4_unicode_ci'), default=None, nullable=True, comment='template name')
    secs = db.Column(db.Text(collation='utf8mb4_unicode_ci'), default=None, nullable=True)
    is_default = db.Column(db.Boolean, nullable=False, default=False)
    created_at = db.Column(db.TIMESTAMP, nullable=True)
    updated_at = db.Column(db.TIMESTAMP, nullable=True)

    def to_dict(self):
        return {
            'id':self.id,
            'name': self.name,
            'slug': self.slug,
            'tempname': self.tempname,
            'secs': eval(str(self.secs)),
            'is_default': self.is_default,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }

class PasswordReset(db.Model):
    __tablename__ = "password_resets"
    email = db.Column(db.String(40, collation='utf8mb4_unicode_ci'), nullable=False, primary_key=True)
    token = db.Column(db.String(40, collation='utf8mb4_unicode_ci'), nullable=False)
    created_at = db.Column(db.TIMESTAMP, nullable=True)

class Send(db.Model):
    __tablename__ = "sends"
    id = db.Column(db.BigInteger(), primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, nullable=False)
    trx = db.Column(db.String(255, collation='utf8mb4_unicode_ci'), default=None, nullable=True)
    wallet_id = db.Column(db.Integer, nullable=False)
    receive_wallet = db.Column(db.String(255, collation='utf8mb4_unicode_ci'), nullable=False)
    amount = db.Column(db.DECIMAL(18, 8), nullable=False)
    charge = db.Column(db.DECIMAL(5, 2), nullable=False)
    status = db.Column(db.String(255, collation='utf8mb4_unicode_ci'), nullable=False, comment='0=>Pending, 1=>Completed')
    created_at = db.Column(db.TIMESTAMP, nullable=True)
    updated_at = db.Column(db.TIMESTAMP, nullable=True)

class SupportAttachment(db.Model):
    __tablename__ = "support_attachments"
    id = db.Column(db.BigInteger(), primary_key=True, autoincrement=True)
    support_message_id = db.Column(db.Integer, nullable=False)
    attachment = db.Column(db.String(255, collation='utf8mb4_unicode_ci'), nullable=False)
    created_at = db.Column(db.TIMESTAMP, nullable=True)
    updated_at = db.Column(db.TIMESTAMP, nullable=True)

class SupportMessage(db.Model):
    __tablename__ = "support_messages"
    id = db.Column(db.BigInteger(), primary_key=True, autoincrement=True)
    supportticket_id = db.Column(db.Integer, nullable=False, default=0)
    admin_id = db.Column(db.Integer, nullable=False, default=0)
    message = db.Column(db.Text(collation='utf8mb4_unicode_ci'), nullable=False)
    created_at = db.Column(db.TIMESTAMP, nullable=True)
    updated_at = db.Column(db.TIMESTAMP, nullable=True)

class SupportTicket(db.Model):
    __tablename__ = "support_tickets"
    id = db.Column(db.BigInteger(), primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, default=0)
    name = db.Column(db.String(40, collation='utf8mb4_unicode_ci'), default=None, nullable=True)
    email = db.Column(db.String(40, collation='utf8mb4_unicode_ci'), default=None, nullable=True)
    ticket = db.Column(db.String(40, collation='utf8mb4_unicode_ci'), default=None, nullable=True)
    subject = db.Column(db.String(255, collation='utf8mb4_unicode_ci'), default=None, nullable=True)
    status = db.Column(db.Boolean, nullable=False, comment='0: Open, 1: Answered, 2: Replied, 3: Closed')
    priority = db.Column(db.Boolean, nullable=False, default=0, comment='1 = Low, 2 = medium, 3 = high')
    last_reply = db.Column(db.DateTime, default=None)
    created_at = db.Column(db.TIMESTAMP, nullable=True)
    updated_at = db.Column(db.TIMESTAMP, nullable=True)

class Transaction(db.Model):
    __tablename__ = "transactions"
    id = db.Column(db.BigInteger(), primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer(), nullable=False, default=0)
    wallet_id = db.Column(db.Integer, default=0)
    amount = db.Column(db.DECIMAL(28, 8), nullable=False, default=0.00000000)
    charge = db.Column(db.DECIMAL(28, 8), nullable=False, default=0.00000000)
    post_balance = db.Column(db.DECIMAL(28, 8), nullable=False, default=0.00000000)
    trx_type = db.Column(db.String(40, collation='utf8mb4_unicode_ci'), default=None, nullable=True)
    trx = db.Column(db.String(40, collation='utf8mb4_unicode_ci'), default=None, nullable=True)
    details = db.Column(db.String(255, collation='utf8mb4_unicode_ci'), default=None, nullable=True)
    created_at = db.Column(db.TIMESTAMP, nullable=True)
    updated_at = db.Column(db.TIMESTAMP, nullable=True)

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.BigInteger(), primary_key=True, autoincrement=True)
    firstname = db.Column(db.String(40, collation='utf8mb4_unicode_ci'), default=None, nullable=True)
    lastname = db.Column(db.String(40, collation='utf8mb4_unicode_ci'), default=None, nullable=True)
    username = db.Column(db.String(40, collation='utf8mb4_unicode_ci'), nullable=False)
    email = db.Column(db.String(40, collation='utf8mb4_unicode_ci'), nullable=False)
    country_code = db.Column(db.String(40, collation='utf8mb4_unicode_ci'), default=None, nullable=True)
    mobile = db.Column(db.String(40, collation='utf8mb4_unicode_ci'), default=None, nullable=True)
    ref_by = db.Column(db.Integer, nullable=False, default=0)
    balance = db.Column(db.DECIMAL(28, 8), nullable=False, default=0.00000000)
    password = db.Column(db.String(255, collation='utf8mb4_unicode_ci'), nullable=False)
    image = db.Column(db.String(255, collation='utf8mb4_unicode_ci'), default=None, nullable=True)
    address = db.Column(db.Text(collation='utf8mb4_unicode_ci'), default=None, nullable=True, comment='contains full address')
    status = db.Column(db.Boolean, nullable=False, default=1, comment='0: banned, 1: active')
    ev = db.Column(db.Boolean, nullable=False, default=0, comment='0: email unverified, 1: email verified')
    sv = db.Column(db.Boolean, nullable=False, default=0, comment='0: sms unverified, 1: sms verified')
    ver_code = db.Column(db.String(40, collation='utf8mb4_unicode_ci'), default=None, nullable=True, comment='stores verification code')
    ver_code_send_at = db.Column(db.DateTime, default=None, nullable=True, comment='verification send time')
    ts = db.Column(db.Boolean, nullable=False, default=0, comment='0: 2fa off, 1: 2fa on')
    tv = db.Column(db.Boolean, nullable=False, default=1, comment='0: 2fa unverified, 1: 2fa verified')
    tsc = db.Column(db.String(255, collation='utf8mb4_unicode_ci'), default=None, nullable=True)
    remember_token = db.Column(db.String(255, collation='utf8mb4_unicode_ci'), default=None, nullable=True)
    created_at = db.Column(db.TIMESTAMP, nullable=True)
    updated_at = db.Column(db.TIMESTAMP, nullable=True)

class UserLogin(db.Model):
    __tablename__ = "user_logins"
    id = db.Column(db.BigInteger(), primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, nullable=False, default=0)
    user_ip = db.Column(db.String(40, collation='utf8mb4_unicode_ci'), default=None, nullable=True)
    city = db.Column(db.String(40, collation='utf8mb4_unicode_ci'), default=None, nullable=True)
    country = db.Column(db.String(40, collation='utf8mb4_unicode_ci'), default=None, nullable=True)
    country_code = db.Column(db.String(40, collation='utf8mb4_unicode_ci'), default=None, nullable=True)
    longitude = db.Column(db.String(40, collation='utf8mb4_unicode_ci'), default=None, nullable=True)
    latitude = db.Column(db.String(40, collation='utf8mb4_unicode_ci'), default=None, nullable=True)
    browser = db.Column(db.String(40, collation='utf8mb4_unicode_ci'), default=None, nullable=True)
    os = db.Column(db.String(40, collation='utf8mb4_unicode_ci'), default=None, nullable=True)
    created_at = db.Column(db.TIMESTAMP, nullable=True)
    updated_at = db.Column(db.TIMESTAMP, nullable=True)

class UserWallet(db.Model):
    __tablename__ = "user_wallets"
    id = db.Column(db.BigInteger(), primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(255, collation='utf8mb4_unicode_ci'), default=None, nullable=True)
    coin_code = db.Column(db.String(15, collation='utf8mb4_unicode_ci'), nullable=False)
    wallet_address = db.Column(db.String(255, collation='utf8mb4_unicode_ci'), nullable=False)
    balance = db.Column(db.DECIMAL(18, 8), default=0.00000000)
    last_cron = db.Column(db.Integer, nullable=False, default=0)
    created_at = db.Column(db.TIMESTAMP, nullable=True)
    updated_at = db.Column(db.TIMESTAMP, nullable=True)

# Create the table
# db.create_all()

