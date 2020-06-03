from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView
from . import models
# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self,**kwargs):
        context  = super().get_context_data(**kwargs)
        context['injectme'] = 'Github repo'     #"Basic Injection!"
        return context



class SchoolListView(ListView):
    model = models.School # default school_list
    template_name = 'basic_app/school_list.html' #added templat_name for better redability

class SchoolDetailView(DetailView):
    context_object_name = 'school_details' # default is lower case School
    model = models.School
    template_name = 'basic_app/school_detail.html'