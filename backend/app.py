from routes import app
from models import db

@app.context_processor
def utility_processor():
    from helper import systemDetails, imagePath, getImage, osBrowser, siteName, getContent , getTemplates, getPageSections, getLatestVersion, activeTemplate, activeTemplateName, menuActive
    from models import GeneralSetting

    general = GeneralSetting.query.first_or_404()
    return dict(systemDetails=systemDetails, imagePath=imagePath, getImage=getImage, osBrowser=osBrowser, siteName=siteName, getContent=getContent, getTemplates=getTemplates, getPageSections=getPageSections, getLatestVersion=getLatestVersion, activeTemplate=activeTemplate, activeTemplateName=activeTemplateName, menuActive=menuActive, general=general)

if __name__ == '__main__':
    # Create the database tables.
    with app.app_context():
        db.create_all()
    # Start the Flask development web server.
    # app.run(debug=True, host='0.0.0.0')
    app.run(debug=True)
