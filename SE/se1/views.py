from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from se1.models import Studentinfo 
from se1.models import Project
from se1.models import Profinfo
from se1.models import Studprojgrade
from se1.models import Studcontact
from se1.models import Studemail
from django.db import connection
from se1.models import Projprof
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
# Create your views here.

def renderpolls(request):
    return HttpResponse("Hello, world.You're at the polls")

def renderdashboard(request):
    u = request.session['member_id']
    all1 = list(Studprojgrade.objects.filter(usn=u))
    all2=[]
    all3=[]
    all4 = []
    for i in all1:
        all5 = []
        x=i.projid
        l=list(Project.objects.filter(projid=x ))
        if(not l[0].complete):
            all4 = list(Projprof.objects.filter(projid = x))
            for ii in all4:
                xx = ii.profid
                #print(xx)
                all6 = []
                all6 = list(Profinfo.objects.filter(profid = xx))
                all5.append(all6[0])
            l1=list(Studprojgrade.objects.filter(projid=x))
            l.append(l1)
            l.append(all5)
            all2.append(l)
    return render(request,'se1/dashboard/dashboard.html',{'all2': all2})

def rendernotifications(request):
	return render(request,'se1/dashboard/notifications.html',{})

def rendertable(request):
    u = request.session['member_id']
    all1 = list(Studprojgrade.objects.filter(usn=u))
    all2=[]
    all3=[]
    all4 = []
    for i in all1:
        all5 = []
        x=i.projid
        l=list(Project.objects.filter(projid=x ))
        if(l[0].complete):
            all4 = list(Projprof.objects.filter(projid = x))
            for ii in all4:
                xx = ii.profid
                #print(xx)
                all6 = []
                all6 = list(Profinfo.objects.filter(profid = xx))
                all5.append(all6[0])
            l1=list(Studprojgrade.objects.filter(projid=x))
            l.append(l1)
            l.append(all5)
            all2.append(l)
    return render(request,'se1/dashboard/table.html',{'all2': all2})

def rendertemplate(request):
    return render(request,'se1/dashboard/template.html',{})

@csrf_exempt
def renderuser(request):
    u = request.session['member_id']
    usr = User.objects.get(username = u)
    cursor = connection.cursor()
    name = Studentinfo.objects.filter(usn = u)
    phnos = Studcontact.objects.filter(usn = u)
    emails = Studemail.objects.filter(usn = u)
    if(request.method == 'POST'):
        data = request.POST
        #login(request, user)
        passwrd = data["passwrd"]
        passwrd2 = data["passwrd2"]
        if(passwrd == passwrd2):
            usr.set_password(passwrd)
            usr.save()
            cursor.execute("update Studentinfo set passwd = '"+ passwrd+ "' where usn = '"+ u +"'")
            template = loader.get_template('se1/dashboard/user.html')
            return HttpResponse(template.render({'KEY': 1, 'name':name[0].name, 'usn':u, 'phnos':phnos[0].phno, 'emails':emails[0].email},request),status=200)
        else:
            template = loader.get_template('se1/dashboard/user.html')
            return HttpResponse(template.render({'KEY': 2, 'name':name[0].name, 'usn':u, 'phnos':phnos[0].phno, 'emails':emails[0].email},request),status=200)

    else:
        return render(request,'se1/dashboard/user.html',{'name':name[0].name, 'usn':u, 'phnos':phnos[0].phno, 'emails':emails[0].email})

def renderadd_project(request):
    return render(request,'se1/dashboard/add_project.html',{})

@csrf_exempt
def renderindex(request):
    if(request.method=="POST"):
        data = request.POST #data is now a dictionary
        x = data['username']
        y = data['passwrd']

        user = authenticate(username = x, password = y)

        if user is not None:
            #login(request, user)
            request.session['member_id'] = user.username
            print("User:", request.session['member_id'])
            return redirect(renderdashboard)
        else:
            template = loader.get_template('se1/dashboard/index.html')
            context={'KEY':1}
            return HttpResponse(template.render(context,request),status=200)
    else:
        template = loader.get_template('se1/dashboard/index.html')
        context={'KEY':0}
        return HttpResponse(template.render(context,request),status=200)

def rendertable1(request):
    all1 = list(Project.objects.all())
    all2=[]
    all3=[]
    all4 = []
    for i in all1:
        x=i.projid
        l=list(Project.objects.filter(projid=x ))
        all4 = list(Projprof.objects.filter(projid = x))
        l1=list(Studprojgrade.objects.filter(projid=x))
        l.append(l1)
        l.append(all4)
        all2.append(l)
    return render(request,'se1/dashboard/table1.html',{'all2': all2})

def rendertable2(request):
    return render(request,'se1/dashboard/table2.html',{})


