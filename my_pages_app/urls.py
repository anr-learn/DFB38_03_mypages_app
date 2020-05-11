from django.urls import path

from .views import MyHomePageView, MyAboutPageView

# NOTE  ************** ANR ***************
# You need the trailing '/' on home/ and about/
# else Django won't find  127.0.0.1:8000/home (or ...home/ for that matter);
# NOTE **********************************

urlpatterns = [
	path("", MyHomePageView.as_view(), name="home"),
	path("home/", MyHomePageView.as_view(), name="home"),
	path("about/", MyAboutPageView.as_view(), name="about"),
]

### end ###

