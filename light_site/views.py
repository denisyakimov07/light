from django.shortcuts import render

# Create your views here.
from django.views import View


class HomeView(View):
    """Home page"""
    def get(self, request):
        return render(request, "light_site/base.html")

