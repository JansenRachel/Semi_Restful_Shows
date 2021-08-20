from django.db import models
# from django.http import request
from django.shortcuts import redirect, render, HttpResponse
from . models import Show


def display_all_shows(request):
    context = {
        'shows' : Show.objects.all()
    }
    return render(request, "all_shows.html", context)

# def delete_show(request):
#     return redirect('shows')

# def update_show(request):
#     return redirect('shows')


def add_show_form(request):
    return render(request, "create_show.html")

def create_new_show(request):
    # context = {
    #     'show_id' : show_id
    # }
    # if request.method == "POST":
    #     Show.objects.create (title = request.POST['title'], release_date = request.POST['release_date'], desc = request.POST['desc'], network = request.POST['network'])
    # thisShow = Show.objects.get(id= request.POST['show'])
    # return redirect(f"{thisShow.id}")
    # return redirect('{show.id}', context)
    return HttpResponse("This show and all info about it")

def display_show_info(request, show_id):
    context = {
        'shows' : Show.objects.all()
    }
    
    return render(request, "display_show_info.html", context)

def edit_show(request, show_id):
    return render(request, "edit_show.html")

