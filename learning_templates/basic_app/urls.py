from django.urls import path
from basic_app import views

#set NAME Space

app_name = 'basic_app'

urlpatterns  = [

        path('other/',views.other, name ='other'),
        path('relative/',views.relative, name = 'relative')


]
