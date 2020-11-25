from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Input

# Create your views here.


def index(request):
    return HttpResponse("날짜 잡는 사이트")
    
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)