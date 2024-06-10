from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from testapp.models import Empmodel
from testapp import forms
from testapp import forms
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView, CreateView, ListView
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
# Create your views here.


def Empmain(request):
    return render(request, 'testapp/main.html')


def signup(request):
    form = forms.Empforms()
    if request.method == 'POST':
        form = forms.Empforms(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            return redirect('/')
    return render(request, 'testapp/signup.html', {'form': form})


@login_required
def Emphome(request):
    return render(request, 'testapp/home.html')


@login_required
def Empadmin(request):
    return render(request, 'testapp/admin.html')


def Empmodel1(request):
    print(request.user)
    emp = Empmodel.objects.filter(user=request.user)
    return render(request, 'testapp/work.html', {'emp': emp})


def Emplogout(request):
    return render(request, 'testapp/logout.html')


def Empforms1(request):
    form = forms.Empforms()
    if request.method == 'POST':
        form = forms.Empforms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/work')
    return render(request, 'testapp/addform.html', {'form': form})
# class Empcreate(CreateView):
#     model=Empmodel
#     fields='__all__'
#     template_name='testapp/loform.html'
#     success_url=reverse_lazy('back')


@csrf_exempt
def Empcreate(request):
    if request.method == "GET":
        return render(request, 'testapp/loform.html')
    print(request.POST)
    name = request.POST['name']
    type = request.POST['type']
    todo = Empmodel.objects.create(name=name, type=type, user=request.user)
    return render(request, 'testapp/loform.html')


class Empupdate(UpdateView):
    model = Empmodel
    fields = ('type',)
    context_object_name = 'book'
    success_url = reverse_lazy('back')


class Empdelete(DeleteView):
    model = Empmodel
    context_object_name = "book1"
    success_url = reverse_lazy('back')


def Resour(request):
    return render(request, 'testapp/resources.html')


def OnlineTraining(request):
    return render(request, 'testapp/courses.html')
