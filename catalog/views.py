from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User,Group
# Create your views here.
def index(req):

    numkino = Kino.objects.all().count()
    numactor = Actor.objects.all().count()
    numfree = Kino.objects.filter(status__kino=1).count()
    if req.user.username:
        username = req.user.first_name
        print(req.user.first_name,'#',req.user.id)
        # req.session['username']= username
    else:
        username = 'Гость'
        print(req.user.id)
    #     req.session['username']= username
    # print(req.session['username'])
    data={'k1':numkino,'k2':numactor,'k3':numfree,'username':username}
    # user = User.objects.create_user('User2','user2@mail.ru','useruser')
    # user.first_name = 'Vlad'
    # user.last_name = 'Petrov'
    # user.save()

    return render(req,'index.html', context=data)

# def allkino(req):
#     return render(req,'index.html')

from django.views import generic
class Kinolist123(generic.ListView):
    model = Kino
    paginate_by = 5

class KinoDetail(generic.DetailView):
    model = Kino


class AcList(generic.ListView):
    model = Actor
    paginate_by = 4

class AcDetail(generic.DetailView):
    model = Actor

class DiList(generic.ListView):
    model = Director
    paginate_by = 4

class DiDetail(generic.DetailView):
    model = Director
# from django.http import HttpResponse
# def info(req,id):
#     film = Kino.objects.get(id=id)
#     return HttpResponse(film.title)

def statusView(req):
    podpiska = Status.objects.all()
    data={'k1':podpiska}
    return render(req,'stview.html',data)

def prosmotr(req,k2):
    mas=['Free','Based','Super']
    mas2=['бесплатно','базовая','супер']
    userid = req.user.id


    print(userid,'############')
    if userid==None:
        k1 = 'Free'
    else:
        k1=User.objects.get(id=userid).groups.all()
        k1=k1[0].name
    if mas.index(k1)>=mas2.index(k2):
        k3='ok'
    else:
        k3=''
    data={'prava':k1,'kino':k2,'k3':k3}
    return render(req,'pro.html', data)

def buy(req,type):
    usid=req.user.id
    usnow = User.objects.get(id=usid)
    usgr = usnow.groups.all()[0]
    print(usid,usnow,usgr)
    grold = Group.objects.get(id=usgr.id)
    print(grold)
    grold.user_set.remove(usnow)
    grnew=Group.objects.get(id=type)
    print(grold,grnew)
    grnew.user_set.add(usnow)
    k1=grnew.name
    data={'type':k1}
    return render(req,'buy.html', data)

from .form import SignUpForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
def reg(req):
    # anketa=UserCreationForm()

    print(1)
    if req.POST:
        print(2)
        anketa = SignUpForm(req.POST)
        # anketa = UserCreationForm(req.POST)
        if anketa.is_valid():
            print(3)
            anketa.save()
            k1 = anketa.cleaned_data.get('username')
            k2 = anketa.cleaned_data.get('password1')
            # k3 = anketa.cleaned_data.get('email')
            # k4 = anketa.cleaned_data.get('first_name')
            # k5 = anketa.cleaned_data.get('last_name')
            user = authenticate(username=k1, password=k2)

            login(req, user)
            man=User.objects.get(username=k1)
            group = Group.objects.get(id=1)
            group.user_set.add(man)
            return redirect('home')
    else:
        anketa = SignUpForm()
        data = {'form': anketa}
        return render(req,'registration/reg.html',data)