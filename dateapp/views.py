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
    try:
        namevalue = request.POST['namevalue']
        inputdate = request.POST['date']
        info=Info.objects.all().filter(date=inputdate)[:] # filter date로
        return render(request, 'dateapp/detail.html',{
            'namevalue':namevalue,
            'date':inputdate,
            'info':info,
            })
    except (KeyError):
        return render(request, 'dateapp/index.html', {
            'error_message': "Please write your name"
        })

def calendar(request):
    try:
        namevalue = request.POST['namevalue']
        if(namevalue.strip()==""):
             return render(request, 'dateapp/index.html', {
            'error_message': "Please rewrite your name"
        })
        try:
            username = request.POST['namevalue']
            time = request.POST['timevalue']
            date = request.POST['datevalue']
            do = request.POST['dovalue']
            if(do.strip()==""):
                return render(request, 'dateapp/detail.html', {
                'error_message': "Please rewrite what you want to do",
                'namevalue' : username,
                'date' : date
            })
            flag=False
            info=Info.objects.all().filter(do=do)[:]
            if(info): # 중복 처리 
                for i in info:
                    if(str(i.time)[:5]==time and str(i.date) == date):
                        flag=True
                        break
            per = Person.objects.filter(username=username)
            if(not flag):
                if(per): # 이미 있음
                    i = Info.objects.create(user=per[0],date=date,time=time,do=do)
                    i.save()
                else: # 없음
                    p = Person.objects.create(username=username)
                    p.save()
                    i = Info.objects.create(user=p,date=date,time=time,do=do)
                    i.save()

                
        except (KeyError):
            pass
    except (KeyError):
        return render(request, 'dateapp/index.html', {
            'error_message': "Please write your name"
        })
    information=Info.objects.all().order_by('date') # 날짜순으로 정렬
    context={} #context- dict 내용물 - str
    a=0
    for row in information.values_list():
        # context.update({a:json.dumps(row,sort_keys=True,indent=4,cls=DjangoJSONEncoder)})
        #print(row)
        InfoId=row[0]
        personname=str(information[a].user)
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

