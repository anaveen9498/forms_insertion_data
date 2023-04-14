from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
# Create your views here.
def insert_topic(request):
    if request.method=='POST':
        tpn=request.POST['topic_name']
        TO=Topic.objects.get_or_create(topic_name=tpn)[0]
        TO.save()
        return HttpResponse('Topic_Name inserted Successfully!!!...')
    return render(request,'insert_topic.html')


def insert_webpage(request):
    lo=Topic.objects.all()
    d={'name':lo}
    if request.method=='POST':
        tpn=request.POST['tn']
        pln=request.POST['pn']
        URL=request.POST['url']
        eml=request.POST['em']
        TO=Topic.objects.get(topic_name=tpn)
        TO.save()
        T=Webpage.objects.get_or_create(topic_name=TO,player_name=pln,url=URL,Email=eml)[0]
        T.save()
        return HttpResponse('Webpage Details Inserted Successfully!!!..')
    return render(request,'insert_webpage.html',d)


def insert_accessrecords(request):
    po=Webpage.objects.all()
    d={'pname':po}
    if request.method=='POST':
        pln=request.POST['pn']
        autr=request.POST['author']
        dt=request.POST['date']

        TO=Webpage.objects.get(player_name=pln)
        TO.save()
        TT=AccessRecords.objects.get_or_create(player_name=TO,author=autr,date=dt)[0]
        TT.save()
        return HttpResponse('Access Records Data Inserted Successfully!!!...')
    return render(request,'insert_accessrecords.html',d)