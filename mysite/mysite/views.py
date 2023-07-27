from django.views import View
from django.shortcuts import render, redirect

from .forms import LoginForm

class HomePageView(View):
    def get(self, request):
        return render(request, 'mysite/home_page.html')
    
class DetailPageView(View):
    def get(self, request):
        return render(request, 'mysite/detail_page.html')

class  LoginPageView(View):
    def post(self, request):
        return redirect('home-page')
    def get(self, request):
        return render(request, 'mysite/login_page.html', {'login_form': LoginForm()})