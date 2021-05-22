from django.shortcuts import render, redirect
from employe.forms import Empfrom
from employe.models import Emplyee

def empbase(request):
    Empdet = Emplyee.objects.all()
    return render(request, 'Emp.html', {'Empdet': Empdet})

def createemp(request):
    form = Empfrom(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('empdet')

    return render(request, 'Createuser.html', {'form': form})

def Update_emp(request, emp_id):
    employe = Emplyee.objects.get(pk=emp_id)
    form = Empfrom(request.POST or None, instance=employe)

    if form.is_valid():
        form.save()
        return redirect('empdet')
    return render(request, 'Createuser.html', {'form': form, 'employe': employe})

def delete_emp(request, emp_id):
    employe = Emplyee.objects.get(pk=emp_id)
    employe.delete()

    return redirect('empdet')
