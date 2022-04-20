from django.shortcuts import render
from time import gmtime, strftime
from django.utils import timezone
from datetime import datetime

time = timezone.localtime() 
def index(request):
    context = {
        "date": strftime("%b %d, %Y", gmtime()),
        "time": strftime("%H:%M %p", gmtime()),
        "time2": timezone.now().strftime("%H:%M %p"),
        "date2": datetime.now().strftime("%b %d, %Y")
    }
    return render(request,'index.html', context)