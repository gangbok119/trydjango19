from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# Create(POST)/Retrieve List Search (GET)/Update(PUT/PATCH)/Delete(DELETE)



def post_home(request):

    return HttpResponse("<h1>Hello</h1>")

def post_create(request):

    return HttpResponse("<h1>Create</h1>")


def post_detail(request):

    return HttpResponse("<h1>Detail</h1>")
def post_list(request):

    return render(request,"index.html",{})
def post_update(request):

    return HttpResponse("<h1>Update</h1>")
def post_delete(request):

    return HttpResponse("<h1>Delete</h1>")

