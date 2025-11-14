from django.http import HttpResponse
from django.shortcuts import render, redirect

from myapp.models import admintbl, routestbl, managebustbl, managequotastbl, booknowtbl


# Create your views here.
def index(request):
    return render(request,"Adminpanel/index.html")

def index_code(request):
    if request.method == "POST":
        a=request.POST.get("email")
        b=request.POST.get("password")
        data=admintbl.objects.filter(userename=a).first()
        if not data:
            return HttpResponse('Email not found')
        elif data.password == b:
            request.session['user'] = a
            return redirect("../dashboard")
        else:
            return HttpResponse('Passwords do not match')
    else:
        return redirect('../adminpanel')

def dashboard(request):
    sesid=request.session.get('user')
    if not sesid:
        return redirect('../adminpanel')
    return render(request, "Adminpanel/dashboard.html")

def managebus(request):
    sesid=request.session.get('user')
    if not sesid:
        return redirect('../adminpanel')
    getdata=routestbl.objects.all()
    fetch=managebustbl.objects.all()
    return render(request, "Adminpanel/managebus.html",{'getshow':getdata ,'fetchdata':fetch})

def manage_routes(request):
    sesid=request.session.get('user')
    if not sesid:
        return redirect('../adminpanel')
    data=routestbl.objects.all()
    return render(request,"Adminpanel/manage_routes.html",{'show':data})

def manage_routes_code(request):
   if request.method == "POST":
       a=request.POST.get("source")
       b=request.POST.get("destination")
       c=request.POST.get("distance")
       d=request.POST.get("duration")
       routestbl.objects.create(source=a,destination=b,distance=c,duration=d)
       return redirect("../manage_routes")

   else:
       return redirect('../adminpanel')

def busmanage_code(request):
    if request.method == "POST":
        a=request.POST.get("busname")
        b=request.POST.get("routeid")
        c=request.POST.get("dtime")
        d=request.POST.get("totalseat")
        managebustbl.objects.create(busname=a,routeid=b,dtime=c,totalseat=d)
        return redirect("../managebus")
    else:
        return redirect('../adminpanel')

def manage_quotas(request):
    sesid=request.session.get('user')
    if not sesid:
        return redirect('../adminpanel')
    data=managequotastbl.objects.all()
    return render(request, "Adminpanel/manage_quotas.html",{'show':data})

def manage_quotas_code(request):
    if request.method == "POST":
        a=request.POST.get("qname")
        b=request.POST.get("per")
        c=request.POST.get("cutoffTime")
        managequotastbl.objects.create(qname=a,per=b,cutofftime=c)
        return redirect("../manage_quotas")
    else:
        return redirect('../adminpanel')


def bus(request):
    return render(request,'User/bus.html')

def searchcode(request):
    if request.method == "POST":
        a=request.POST.get("source")
        b=request.POST.get("destination")
        c=request.POST.get("jdate")
        data=routestbl.objects.filter(source=a,destination=b)
        return render(request,"User/bus.html",{'show':data})
    else:
        return redirect('../')

def viewbus(request,id):
    data=managebustbl.objects.filter(routeid=id)
    return render(request,"User/viewbus.html",{'show':data})

def booknow(request,id):
    data = managebustbl.objects.filter(id=id).first()
    data1=routestbl.objects.filter(id=data.routeid).first()
    return render(request,"User/booknow.html",{'show':data,"show1":data1})

def booknowcode(request):
    if request.method == "POST":
        a=request.POST.get("busname")
        b=request.POST.get("dtime")
        c=request.POST.get("source")
        d=request.POST.get("destination")
        e=request.POST.get("name")
        f=request.POST.get("mob")
        g=request.POST.get("email")
        h=request.POST.get("jdate")
        i=request.POST.get("quota")
        data=booknowtbl.objects.create( status=' pending ',busname=a,dtime=b,source=c,destination=d,name=e,mobile=f,email=g,jdate=h,quota=i)
        request.session['bus']=data.id
        return redirect("../confirmation")
    else:
        return redirect('../')

def confirmation(request):
    sesid=request.session.get('bus')
    if not sesid:
        return redirect('../')
    data=booknowtbl.objects.filter(id=sesid).first()
    return render(request,"User/confirmation.html",{'show':data})

def bookin_view(request):
    sesid=request.session.get('user')
    if not sesid:
        return redirect('../adminpanel')
    data=booknowtbl.objects.all()
    return render(request,"Adminpanel/bookin_view.html",{'show':data})


def confirmcode(request,id):
    data=booknowtbl.objects.filter(id=id).first()
    if data.status == 'pending':
        booknowtbl.objects.filter(id=id).update(status=' confirmed')
        return redirect("../bookin_view")
    else:
        return HttpResponse('Status already confirm so don`t click')