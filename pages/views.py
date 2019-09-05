from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request,*args , **kwargs):
    print(request)
    print(args)
    print(kwargs)
    #return HttpResponse("<h1>hello World: Home page</h1>") #string of HTML code
    return render(request,"home.html",{})

def support_view(request,*args , **kwargs):
    #return HttpResponse("<h1>hello World: Support Page</h1>") #string of HTML code
    return render(request,"support.html",{})

def contact_view(request,*args , **kwargs):

    #return HttpResponse("<h1>hello World: Contact Page</h1>") #string of HTML code
    return render(request,"contact.html",{})

def about_view(request,*args , **kwargs):
    my_context = {
        "my_text":"utk",
        "my_num" :123,
        "my_list":[12,23,34],
        "my_html":"<h1>Hello World!</h1>"
    }
    #return HttpResponse("<h1>hello World: About Page</h1>") #string of HTML code
    return render(request,"about.html",my_context)
