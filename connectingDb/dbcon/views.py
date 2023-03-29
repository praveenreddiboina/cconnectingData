from django.shortcuts import render

# Create your views here.
def home(request):
    firstName=request.GET.get("fname")
    lastName=request.GET.get("lname")
    fullName=firstName+ " ",lastName
    context={"fullName":fullName}

    
    return render(request, "home.html",context)