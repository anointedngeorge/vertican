
from django.conf import settings

# ADMIN_LOGIN_PATH = 'admin/'
# ADMIN_URI = "/admin"


CUSTOMLINKS = {
        "realestate": [{
            "name": "Make Messages", 
            "url": "make_messages", 
            "icon": "fas fa-comments",
            "permissions": ["books.view_book"]
        }],

        "customer": [{
            "name": "Create Client", 
            "url": f"/admin/authuser/user/add/", 
            "icon": "fas fa-add",
            # "permissions": ["books.view_book"]
        }],

}