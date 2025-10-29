from django.shortcuts import render, redirect
from .forms import user_form
from .models import Employee

# Create your views here.


def user_list(request):
    context = {'user_list': Employee.objects.all()}
    return render(request, "crud_operations/user_list.html", context)


def user_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = user_form()
        else:
            employee = Employee.objects.get(pk=id)
            form = user_form(instance=employee)
        return render(request, "crud_operations/user_form.html", {'form': form})
    else:
        if id == 0:
            form = user_form(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = user_form(request.POST,instance= )
        if form.is_valid():
            form.save()
        return redirect('/user/list')


def employee_delete(request,id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/user/list')