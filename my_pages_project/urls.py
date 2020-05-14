"""my_pages_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

import os
import sys
import logging

#CTR = 1
logger = logging.getLogger(__name__)
#logger.setLevel(logging.DEBUG)
#print("@@@@@@@@@@@@@@@@@@@@ urls.py logger ctr=%s is %s" % (CTR, logger,))
#CTR += 1
# PARENT is the ROOT LOGGER
#print("@@@@@@@@@@@@@@@@@@@@ urls.py logger dir=%s" % (dir(logger),))
#ppp = logger.parent
#print("@@@@@@@@@@@@@@@@@@@@ urls.py logger parent=%s" % (ppp,))

logger.error("This is my_pages_app/urls.py @ 33")
logger.warning("This is my_pages_app/urls.py @ 34")
logger.info("This is my_pages_app/urls.py @ 35")
logger.debug("This is my_pages_app/urls.py @ 36")

if True:
	#xyz = logging.getLogger("django")
	#xyz.setLevel(logging.DEBUG)
	#print("@@@   @@@   my_pages_app/urls.py@38  django is %s" % (xyz,))
	
	xyz = logging.getLogger("django.server")
	xyz.setLevel(logging.DEBUG)
	print("@@@   @@@   my_pages_app/urls.py@42  django.server is %s" % (xyz,))
	
	xyz = logging.getLogger("django.request")
	xyz.setLevel(logging.DEBUG)
	print("@@@   @@@   my_pages_app/urls.py@46  django.request is %s" % (xyz,))



urlpatterns = [
    path('admin/', admin.site.urls),
	path("", include("my_pages_app.urls")),
	# ANR @@@@ these cause the {% url 'home' %} template tag to
	#          resolve to stuff like /about/about
	#path("home/", include("my_pages_app.urls")),
	#path("about/", include("my_pages_app.urls")),

]

### end ###

