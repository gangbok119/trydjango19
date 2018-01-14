from django.contrib import messages
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
# Create(POST)/Retrieve List Search (GET)/Update(PUT/PATCH)/Delete(DELETE)
from .models import Post
from .forms import PostForm

def post_home(request):
    return HttpResponse("<h1>Hello</h1>")


def post_create(request):
    form = PostForm(request.POST or None)
    # if request.method == "POST":
    #     content = request.POST.get("content")
    #     title = request.POST.get("title")
    #      Post.objects.create(title=title,content=content)
    #

    # form.cleaned_data
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request,"Successfully Created")
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        'form': form,
    }

    return render(request,"post_form.html",context=context)


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
    return render(request, "post_list.html", context=context)


def post_update(request,pk=None):
    instance = get_object_or_404(Post, pk=pk)
    form = PostForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
        messages.success(request,"Item Saved")
        return redirect(instance.get_absolute_url())

    context = {
        "title":instance.title,
        "instance":instance,
        "form":form,

    }
    return render(request,"post_form.html",context=context)


def post_delete(request,pk=None):
    instance = get_object_or_404(Post,pk=pk)
    instance.delete()
    messages.success(request,"Successfully Deleted")
    return redirect(post_list)