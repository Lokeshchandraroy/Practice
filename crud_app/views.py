from django.shortcuts import render, redirect
from .models import UserDetails
from .forms import UserForm

def index(request):
    users = UserDetails.objects.all()
    return render(request, 'crud_app/index.html', {'users': users})

def add_user(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'crud_app/form.html', {'form': form})

def update_user(request, id):
    user = UserDetails.objects.get(id=id)
    form = UserForm(request.POST or None, instance=user)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'crud_app/form.html', {'form': form})

def delete_user(request, id):
    user = UserDetails.objects.get(id=id)
    user.delete()
    return redirect('index')
