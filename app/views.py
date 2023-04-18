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


def retriev_data(request):
    LOT=Topic.objects.all()
    d={'topics':LOT}
    if request.method=='POST':
        td=request.POST.getlist('topic')
        print(td)
        nav=Webpage.objects.none()

        for i in td:
            nav=nav|Webpage.objects.filter(topic_name=i)
        dd={'webpages':nav}
        return render(request,'details_webpage.html',dd)
    return render(request,'retriev_data.html',d)




def checkbox(request):
    LO=Topic.objects.all()
    d={'tpt':LO}
    return render(request,'checkbox.html',d)


def access_retrieve(request):
    LAO=Webpage.objects.all()
    d={'player':LAO}
    if request.method=='POST':
        plrn=request.POST.getlist('pn')
        print(plrn)
        N=AccessRecords.objects.none()
        for x in N:
            N=N|AccessRecords.objects.filter(player_name=x)
        dd={'access':plrn}
        return render(request,'display.html',dd)

    return render(request,'access_retrieve.html',d)