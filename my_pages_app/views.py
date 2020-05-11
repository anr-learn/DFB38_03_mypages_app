from django.shortcuts import render

from django.views.generic import TemplateView

class MyHomePageView(TemplateView):
	template_name = "home.html"

class MyAboutPageView(TemplateView):
	template_name = "about.html"

### end ###

