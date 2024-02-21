from django.shortcuts import render
from django.http import HttpResponse
from dj_app.models import Topic,Webpage,AccessRecord
# Create your views here.

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpages_list}
     # my_dict = {'insert_content': "HELLO THIS IS THE PART 2 DJANGO PROJECT!"}
    return render(request, 'app/index.html',context = date_dict)
