from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
# Create(POST)/Retrieve List Search (GET)/Update(PUT/PATCH)/Delete(DELETE)
from .models import Post


def post_home(request):
    return HttpResponse("<h1>Hello</h1>")


def post_create(request):
    return HttpResponse("<h1>Create</h1>")


def post_detail(request,pk=None):  # retrieve
    instance = get_object_or_404(Post,pk=pk)

    context = {
        "title": instance.title,
        "instance":instance
    }

    return render(request, "post_detail.html", context=context)


def post_list(request):  # List items
    # if request.user.is_authenticated():
    #     context = {
    #         "title": "My User List"
    #     }
    #     return render(request, "index.html", context=context)
    #
    # else:

    queryset = Post.objects.all()
    context = {
        "object_list":queryset,
        "title": "List"
    }
    return render(request, "index.html", context=context)


def post_update(request):
    return HttpResponse("<h1>Update</h1>")


def post_delete(request):
    return HttpResponse("<h1>Delete</h1>")
