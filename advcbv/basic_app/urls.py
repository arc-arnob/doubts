from django.conf.urls import url
from basic_app import views
from django.urls import path


app_name = 'basic_app'

urlpatterns = [

    url('',views.SchoolListView.as_view(),name = 'list'),
    url('(?P<pk>[-\w]+)/', views.SchoolDetailView.as_view(), name = 'detail')

]
