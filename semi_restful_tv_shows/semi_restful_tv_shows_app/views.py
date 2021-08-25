from django.db import models
# from django.http.response import HttpResponse
# from django.http import response
from django.shortcuts import redirect, render, HttpResponse
from . models import Show


def index(request):
    return redirect('/shows')

def display_all_shows(request):
    context = {
        'shows' : Show.objects.all()
    }
    return render(request, "all_shows.html", context)


def add_show_form(request):
    return render(request, "create_show.html")

def delete_show(request, show_id):
    show = Show.objects.get(id=show_id)
    show.delete()
    return redirect('/shows')

def update_show(request, show_id):
    show = Show.objects.get(id=show_id)
    show.title = request.POST['title']
    show.network = request.POST['network']
    show.release_date = request.POST['release_date']
    show.save()
    return redirect(f"shows/{show.id}")

def create_new_show(request):
    show = Show.objects.create (title = request.POST['title'], release_date = request.POST['release_date'], desc = request.POST['desc'], network = request.POST['network'])
    # return redirect(f"show_details/{show.id}")
    #*****************************************************THis path @ created new show redirect to display show page by id****
    return redirect(f"/show_details/{show.id}")


def display_show_info(request, show_id):
    context = {
        'shows' : Show.objects.get(id = show_id)
    }
    return render(request, "display_show_info.html", context)

def edit_show(request, show_id):
    context = {
        'shows' : Show.objects.get(id=show_id)
    }
    return render(request, "edit_show.html", context)

