from django.urls import path

from .views import MyHomePageView, MyAboutPageView

# NOTE  ************** ANR ***************
# You need the trailing '/' on home/ and about/
# else Django won't find  127.0.0.1:8000/home (or ...home/ for that matter);
#
# ALSO NOTE that 'name=...' should specify unique names or the
# reverse lookup will be confused 
# NOTE **********************************



urlpatterns = [
	path("", MyHomePageView.as_view(), name="home"),
	## DONT USE DUPLICATE name ----  path("home/", MyHomePageView.as_view(), name="home"),
	path("home/", MyHomePageView.as_view(), name="home2"),
	path("about/", MyAboutPageView.as_view(), name="about"),
]

### end ###

