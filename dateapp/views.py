from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Person, Info

def index(request):
    a = Person.objects.get(username="Harry")
    return render(request, 'dateapp/index.html',{'userl':a})

def detail(request, user_id):
    user = get_object_or_404(Person, pk=user_id)
    return render(request, 'dateapp/detail.html', {'user': user})

# def results(request, user_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % user_id)

def calendar(request):
    a=Info.objects.all().order_by('date')
    print(a)
    return render(request, 'dateapp/calendar.html',{'a':a})
