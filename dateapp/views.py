import json
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.urls import reverse
from .models import Person, Info


def index(request):
    return render(request, 'dateapp/index.html')

def detail(request): 
    namevalue = request.POST['namevalue']
    inputdate = request.POST['date']
    #infos=Info.objects.all().order_by('date') # filter date로
    return render(request, 'dateapp/detail.html',{
        'namevalue':namevalue,
        'date':inputdate
        })


def calendar(request):
    try:
        namevalue = request.POST['namevalue']
        print(namevalue)
        try:
            timevalue = request.POST['timevalue']
            datevalue = request.POST['datevalue']
            dovalue = request.POST['dovalue']
            print(datevalue)
            print(type(datevalue))
            print(dovalue)
            print(timevalue)
        except (KeyError):
            pass
    except (KeyError):
        return render(request, 'dateapp/index.html', {
            'error_message': "Please write your name"
        })
    informations=Info.objects.all().order_by('date') # 날짜순으로 정렬
    context={} #context- dict 내용물 - str
    a=0
    for row in informations.values_list():
        # context.update({a:json.dumps(row,sort_keys=True,indent=4,cls=DjangoJSONEncoder)})
        #print(row)
        InfoId=row[0]
        personname=str(informations[a].user)
        date=str(row[2])
        time=str(row[3])
        do=str(row[4])
        #[infotable의 id, user_id, date, time, do]
        x={
            "InfoId":InfoId,"username": personname,"date":date,"time":time,"do":do,
        }
        y= json.dumps(x,sort_keys=False,cls=DjangoJSONEncoder)
        print(y)
        context.update({a:y})
        a=a+1
    #context.update({'user':user})
    #print(context)
    return render(request, 'dateapp/calendar.html',{
        'context':context,
        'namevalue':namevalue
        })

