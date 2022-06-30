from django.urls import path
from .import views
urlpatterns = [
   path("",views.intro,name='intro'),
   path("About Us",views.abt,name='about'),
   path("Contact Details",views.cont,name='contact'),
   path("Newpage",views.new,name='news')
]