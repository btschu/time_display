from django.shortcuts import render
from time import gmtime, strftime
from django.utils import timezone
from datetime import datetime

time = timezone.localtime()
def index(request):
    context = {
        # one solution
        "date": strftime("%b %d, %Y", gmtime()),
        "time": strftime("%H:%M %p", gmtime()),

        # another solution
        "date2": datetime.now().strftime("%b %d, %Y"),
        "time2": timezone.now().strftime("%H:%M %p"),
    }
    return render(request,'index.html', context)