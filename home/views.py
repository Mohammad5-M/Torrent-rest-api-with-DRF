from django.shortcuts import render 
from django.views.generic import TemplateView

# Create your views here.
class Homeview(TemplateView):
    template_name: str ="myfirsttemplate"
    def get(self,request):
        return render(request,'home/index.html')

class RegisterView(TemplateView):
    template_name: str ="myfirsttemplate"
    def get(self,request):
        return render(request,'home/register.html')
