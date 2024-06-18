import json, os, re, random, requests, time
from flask import url_for, request, session
from PIL import Image
from models import Frontend

# USEFUL FUNCTIONS

def activeTemplate(asset=False):
    from models import GeneralSetting
    
    general = GeneralSetting.query.first()
    template = general.active_template
    sess = session.get('template')
    if sess:
        template = sess
    if asset:
        return f'assets/templates/{template}/'
    return f'templates.{template}.'

def activeTemplateName():
    from models import GeneralSetting
    
    general = GeneralSetting.query.first()
    template = general.active_template
    sess = session.get('template')
    if sess:
        template = sess
    return template

def getContent(data_keys, singleQuery = False, limit = None, orderById = False):
    if singleQuery:
        content = Frontend.query.filter_by(data_keys=data_keys).order_by(Frontend.id.desc()).first().to_dict()
    else:
        article = Frontend.query.filter_by(data_keys=data_keys).order_by(Frontend.id.desc()).all()
        if orderById:
            article = Frontend.query.filter_by(data_keys=data_keys).all()
        content = [{'id': e.id, 'data_keys': e.data_keys, 'data_values': eval(e.data_values),'created_at': e.created_at, 'updated_at': e.updated_at} for e in article]
        if limit:
            content = [content[cnt] for cnt in range(len(content)) if cnt < limit ]
    return content

def getNumber(length=8):
    characters = '1234567890'
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

def getLatestVersion():
    purchasecode = "your_purchase_code_here"  # Replace with your actual purchase code
    website = f"{request.host_url}{request.full_path} - your_app_url_here"  # Replace your_app_url_here with your actual app URL
    url = f"https://license.viserlab.com/updates/version/{systemDetails()['name']}"
    param = {'purchasecode': purchasecode, 'website': website}
    result = requests.post(url, data=param)
    if result.status_code == 200:
        return result.text
    else:
        return None

def getImage(image, size=None):
    if os.path.exists(url_for('static', filename=image)[1:]) and os.path.isfile(url_for('static', filename=image)[1:]):
        return url_for('static', filename=image+'')
    return url_for('static', filename='assets/images/default.png')

def getPageSections(arr=False):
    jsonUrl = f"templates/basic/sections.json"
    with open(jsonUrl, 'r') as file:
        sections = json.load(file)
    return dict(sorted(sections.items())) if arr else sections

def getTemplates():
    purchasecode = "your_purchase_code_here"  # Replace with your actual purchase code
    website = f"{request.host_url}{request.full_path} - your_app_url_here"  # Replace your_app_url_here with your actual app URL
    url = f"https://license.viserlab.com/updates/templates/{systemDetails()['name']}"
    param = {'purchasecode': purchasecode, 'website': website}
    result = requests.post(url, data=param)
    if result.status_code == 200:
        return result.text
    else:
        return None

def imagePath():
    data = {}
    data['image'] = { 
        'default': 'assets/images/default.png', 
    }
    data['ticket'] = {
        'path': 'assets/support',
    }
    data['language'] = {
        'path': 'assets/images/lang',
        'size': '64x64'
    }
    data['logoIcon'] = {
        'path': 'assets/images/logoIcon',
    }
    data['favicon'] = {
        'size': '128x128',
    }
    data['extensions'] = {
        'path': 'assets/images/extensions',
        'size': '36x36',
    }
    data['seo'] = {
        'path': 'assets/images/seo',
        'size': '600x315'
    }
    data['profile'] = {
        'user': {
            'path':'assets/images/user/profile',
            'size':'350x300'
        },
        'admin': {
            'path':'assets/admin/images/profile',
            'size':'400x400'
        }
    }
    return data

def makeDirectory(path):
    if not os.path.exists(path):
        os.makedirs(path)
        return True
    return True

def menuActive(routeName):
    if request.path.split('/')[-1] == routeName:
        return 'active'
    elif request.endpoint == routeName:
        return 'active'
    elif request.path.split('/')[-2] == routeName:
        return 'active'
    return False

def osBrowser():
    userAgent = request.user_agent.string
    osPlatform = "Unknown OS Platform"
    osArray = {
        'windows nt 10': 'Windows 10',
        'windows nt 6.3': 'Windows 8.1',
        'windows nt 6.2': 'Windows 8',
        'windows nt 6.1': 'Windows 7',
        'windows nt 6.0': 'Windows Vista',
        'windows nt 5.2': 'Windows Server 2003/XP x64',
        'windows nt 5.1': 'Windows XP',
        'windows xp': 'Windows XP',
        'windows nt 5.0': 'Windows 2000',
        'windows me': 'Windows ME',
        'win98': 'Windows 98',
        'win95': 'Windows 95',
        'win16': 'Windows 3.11',
        'macintosh|mac os x': 'Mac OS X',
        'mac_powerpc': 'Mac OS 9',
        'linux': 'Linux',
        'ubuntu': 'Ubuntu',
        'iphone': 'iPhone',
        'ipod': 'iPod',
        'ipad': 'iPad',
        'android': 'Android',
        'blackberry': 'BlackBerry',
        'webos': 'Mobile'
    }
    for regex, value in osArray.items():
        if re.search(regex, userAgent, re.IGNORECASE):
            osPlatform = value

    browser = "Unknown Browser"
    browserArray = {
        'msie': 'Internet Explorer',
        'firefox': 'Firefox',
        'safari': 'Safari',
        'chrome': 'Chrome',
        'edge': 'Edge',
        'opera': 'Opera',
        'netscape': 'Netscape',
        'maxthon': 'Maxthon',
        'konqueror': 'Konqueror',
        'mobile': 'Handheld Browser'
    }
    for regex, value in browserArray.items():
        if re.search(regex, userAgent, re.IGNORECASE):
            browser = value

    data = {'os_platform': osPlatform, 'browser': browser}
    return data

def removeFile(path):
    path = url_for('static', filename=path)[1:]
    if os.path.exists(path) and os.path.isfile(path):
        os.remove(path)
        return True
    return False

def siteName():
    from models import GeneralSetting
    
    general = GeneralSetting.query.first()
    sitename = len(general.sitename.split())
    sitenameArr = general.sitename.split()
    if sitename > 1:
        title = f"<span>{sitenameArr[0]}</span> {general.sitename.replace(sitenameArr[0], '', 1)}", sitenameArr[0]
    else:
        title = f"<span>{general.sitename}</span>", general.sitename
    
    return title

def systemDetails():
        system = {}
        system['name'] = 'SalimTech'
        system['version'] = '1.0'
        return system
    
def to_dict(record, table):
    try:
        return [{column: json.loads(getattr(value, column)) \
        if isinstance(getattr(value, column), str) and \
            getattr(value, column).startswith('{') and getattr(value, column).endswith('}') \
                else getattr(value, column) for column in \
                    table.__table__.c.keys()} for value in record]
    except:
        return {column: json.loads(getattr(record, column)) \
        if isinstance(getattr(record, column), str) and \
            getattr(record, column).startswith('{') and getattr(record, column).endswith('}') \
                else getattr(record, column) for column in table.__table__.columns.keys()\
                    }
    
def uniqueFilename():
    return f"{random.getrandbits(64)}_{int(time.time())}"

def uploadFile(file, location, size=None, old=None):
    path = makeDirectory(url_for('static', filename=location))
    if not path:
        raise Exception('File could not be created.')

    if old:
        removeFile(os.path.join(location, old))

    filename = f"{uniqueFilename()}.{file.filename.split('.')[-1]}"
    file.save(os.path.join(location, filename))
    return filename

def uploadImage(file, location, size=None, old=None, thumb=None, name=None):
    location = url_for('static', filename=location)[1:]
    path = makeDirectory(location)
    if not path:
        raise Exception('File could not be created.')

    if old:
        removeFile(os.path.join(location, old))
        removeFile(os.path.join(location, 'thumb_' + old))
    
    filename = name if name else f"{uniqueFilename()}.{file.filename.split('.')[-1]}"
    file.save(os.path.join(location, filename))
    
    if size:
        width, height = map(int, size.lower().split('x'))
        image = Image.open(os.path.join(location, filename))
        # image.thumbnail((width, height))
        image = image.resize((width, height))
        image.save(os.path.join(location, filename))
    
    if thumb:
        thumb_width, thumb_height = map(int, thumb.lower().split('x'))
        thumb_image = Image.open(os.path.join(location, filename))
        # thumb_image.thumbnail((thumb_width, thumb_height))
        thumb_image = thumb_image.resize((thumb_width, thumb_height))
        thumb_image.save(os.path.join(location, 'thumb_' + filename))

    return filename

def verificationCode(length):
    if length == 0:
        return 0
    min_val = pow(10, length - 1)
    max_val = 0
    for _ in range(length):
        max_val = (max_val * 10) + 9
    return random.randint(min_val, max_val)