import json
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.urls import reverse
from .models import Person, Info


def index(request):
    return render(request, 'dateapp/index.html')

def detail(request, person_id, info_id): 
    username = get_object_or_404(Person, pk=person_id)
    date = get_object_or_404(Info, pk=info_id)
    infos=Info.objects.all().order_by('date') # filter date로
    return render(request, 'dateapp/detail.html')


def calendar(request):
    informations=Info.objects.all().order_by('date') # 날짜순으로 정렬
    context={} #context- dict 내용물 - str
    a=0
    print(informations[1].user)
    for row in informations.values_list():
        # context.update({a:json.dumps(row,sort_keys=True,indent=4,cls=DjangoJSONEncoder)})
        print(row)
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

    print(context)
    return render(request, 'dateapp/calendar.html',{'context':context})

#def name(request):
