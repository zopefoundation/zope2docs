from OFS.Folder import Folder
from Products.PageTemplates.PageTemplateFile import PageTemplateFile

addLmsMain_form =  PageTemplateFile('addLmsMain_form', globals())

def addLmsMain(dispatcher, id):
    """Add LMS"""
    dispatcher._setObject(id, LmsMain(id))
    return "LMS Installed: %s" % id

class LmsMain(Folder):
    meta_type = "LMS"

    index_html = PageTemplateFile('index_html', globals())
