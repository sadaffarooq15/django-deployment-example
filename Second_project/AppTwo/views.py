from django.shortcuts import render
from AppTwo.forms import NewUserForm
# Create your views here.
 
def index(request):
     return render(request, 'Apptwo/index.html')


def help(request):
    helpdict = {'help_me': 'help page'}
    return render(request, 'Apptwo/help.html',context=helpdict)

def users(request):
     # user_list = User.objects.order_by('firstname')
     # user_dict = {'User':user_list}
     # return render(request,'Apptwo/user.html',context=user_dict)
    form = NewUserForm()
    if request.method == "POST":
         form = NewUserForm(request.POST)
         
         if form.is_valid():
              form.save(commit=True)
              return index(request)
         else:
              print("ERROR FORM INVALID")
    return render(request,'Apptwo/user.html',{'form':form})