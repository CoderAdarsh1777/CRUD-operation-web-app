from django.shortcuts import render,redirect
from Employee.models import Employees
from django.core.paginator import Paginator

def home(request):
    emp = Employees.objects.all()
    paginator = Paginator(emp,8)
    page_number = request.GET.get('page')
    Servicedatafinal = paginator.get_page(page_number)
    totalpage = Servicedatafinal.paginator.num_pages
    content = {
        'emp':Servicedatafinal,
        'lastpage':totalpage,
        'totalpagelist':[n+1 for n in range(totalpage)],
        'items': enumerate(emp, start=1)
    }
    return render(request,'index.html',content)

def saveenquiry(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        en=Employees(name=name,email=email,address=address,phone=phone)
        en.save()
        return redirect('home')
    return render(request,'index.html')

def edit(request):
    emp = Employees.objects.all()

    content = {
        'emp':emp
    }
    return redirect(request,'index.html',content)

def update(request,id):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        en=Employees(id=id,name=name,email=email,address=address,phone=phone)
        en.save()
        return redirect('home')
    return redirect(request,'index.html')

def delete(request,id):
    emp = Employees.objects.filter(id=id).delete()
    content = {
        'emp':emp
    }
    return redirect('home')

def page(request):
    data = Employees.objects.all()
    paginator = Paginator()

    return render(request,'index.html')