from django.shortcuts import render

from django.http import HttpResponse
from django.views import View
# Create your views here.

class home(View):
    def get(self, request):

        context = {"title":"Programmerly"}
        return render(request, "codingquestions/mainpage.html", context)

