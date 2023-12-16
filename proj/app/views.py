from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from . import models
# Create your views here.
def index(request):
    return HttpResponse(loader.get_template('misc/index.html').render({},request))

def home(request):
    members = models.Member.objects.all().values()
    template = loader.get_template('members/home.html')
    context = {
        'members':members
    }
    return HttpResponse(template.render(context,request))

def add(request):
    template = loader.get_template('members/add.html')
    return HttpResponse(template.render({},request))

def addrecord(request):
    fn = request.POST['fname']
    ln = request.POST['lname']

    member = models.Member(fname=fn, lname=ln)
    member.save()
    return HttpResponseRedirect(reverse('home'))

def update(request,id):
    member = models.Member.objects.get(id=id)
    template = loader.get_template("members/update.html")
    context={
        'member':member
    }
    return HttpResponse(template.render(context,request))

def updaterecord(request,id):
    fn = request.POST['fname']
    ln = request.POST['lname']

    member = models.Member.objects.get(id=id)
    member.fname = fn
    member.lname = ln
    member.save()
    return HttpResponseRedirect(reverse('home'))

def delete(request,id):
    member = models.Member.objects.get(id=id)
    template = loader.get_template("members/delete.html")
    context={
        "member":member
    }
    return HttpResponse(template.render(context,request))

def deleterecord(request,id):
    member = models.Member.objects.get(id=id)
    member.delete()
    return HttpResponseRedirect(reverse('home'))
