from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import HomeItem
from .models import DoneItem
from subprocess import check_output
import os
import time
import psutil 

def homeView(request):
	all_home_items = HomeItem.objects.all()
	return render(request, 'home.html', {'all_items' : all_home_items})

def addHome(request):
	new_item = HomeItem(content = request.POST['content'], date_created = request.POST['date_created'], author = request.POST['author'])
	new_item.save()
	return HttpResponseRedirect('/home/')

def deleteHome(request, home_id):
	done_item =  HomeItem.objects.get(id = home_id)
	done_item.delete()
	add_item = DoneItem(content = done_item.content, date_completed = done_item.date_created, author = done_item.author)
	add_item.save()
	return HttpResponseRedirect('/home/')

def doneItems(request):
	all_done_items = DoneItem.objects.all()
	return render(request, 'done.html', {'done_items' : all_done_items})

def redirectAbout(request):
	return render(request, 'about.html')

# Create your views here.
def terminateSite(request, program):
    list = []
    for proc in psutil.process_iter():
      try:
       	  pinfo = proc.as_dict(attrs=['pid', 'name', 'create_time'])
       	  if program.lower() == pinfo['name'].lower() :
              list.append(pinfo.get('pid'))
      except (psutil.NoSuchProcess, psutil.AccessDenied , psutil.ZombieProcess) :
          pass
    for p in list:
        os.kill(p, 2)
    return HttpResponseRedirect('/home/')

def sleepSite(request, number):
    time.sleep(number/1000)
    return render(request, 'donework.html', {'time' : number/1000})

