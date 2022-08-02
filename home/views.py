import imp
from webbrowser import get
from django.shortcuts import render 
from django.views.generic import TemplateView ,CreateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin


from home.forms import MyUserForm

# Create your views here.
class Homeview(TemplateView):
    template_name: str ="myfirsttemplate"
    def get(self,request):
        return render(request,'home/index.html')



class RegisterView(SuccessMessageMixin,CreateView):
    form_class = MyUserForm
    success_url = reverse_lazy('homeview')
    template_name = 'home/register.html'
    success_message = "created successfully"

