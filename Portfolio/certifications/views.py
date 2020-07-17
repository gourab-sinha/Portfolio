from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.


def certifications(request):
    template = loader.get_template("certifications/certifications.html")
    return HttpResponse(template.render({}, request))


