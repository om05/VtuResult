"""vtu_results URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin

from . import views
# This is where you define what action needs to be taken when you encounter a particular url using regular expressions
# We will define the admin section in the future for now lets just work on the results page /
# django reads the url using regular expressions 
# it is advised that you go through the regular expressions as it would help you understand 
# in short we will use regular expression "^$" which means when it does not encounter any url go to the homepage 
# Eg: www.easyvturesults.com will redirect to the homepage but when the user types 
# www.easyvturesults.com/4pa11cs011 it should do a different process and show the results
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.index),
    url(r'marks/',views.marks),
]
