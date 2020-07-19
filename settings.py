import os
ROOT_PATH = os.path.dirname(__file__)

# Django requirements
SECRET_KEY = "BIG secret"
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(ROOT_PATH, "templates"),
        ],
        "APP_DIRS": True,
    },
]
INSTALLED_APPS = []

# setting up directory paths
STATIC_DIR = os.path.join(ROOT_PATH, 'static')
DEPLOY_DIR = os.path.join(ROOT_PATH, 'deploy')

# setting up some helpful values
STATIC_URL_FORMAT = u"/%s"
STATIC_IMAGE_FORMAT = STATIC_URL_FORMAT % u"img/%s"
EMAIL = u"bonnie@beproofreading.com"

# creating default rendering context
CONTEXT = {
    "EMAIL": EMAIL,
    "CONTACT_FORM":
    "https://docs.google.com/forms/d/e/1FAIpQLSeWt0TGAi3Z3rSRsoVVIsNo1mRPYuC24OjJgObbhG-o2J0LCA/viewform",
    "LINKEDIN": "https://www.linkedin.com/in/bonnie-echmalian-804940122/",
}
PAGES_TO_RENDER = ("index", "services", "rates", "about")
