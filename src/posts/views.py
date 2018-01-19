from urllib.parse import quote_plus

from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
# Create(POST)/Retrieve List Search (GET)/Update(PUT/PATCH)/Delete(DELETE)
from django.utils.text import slugify

from .models import Post
from .forms import PostForm

def post_home(request):
    return HttpResponse("<h1>Hello</h1>")


def save(self, *args, **kwargs):
    super(Post,self).save(*args,*kwargs)
    if not self.slug:
        self.slug = slugify(self.title) + "-" + str(self.pk)
        self.save()

def post_create(request):
    form = PostForm(request.POST or None, request.FILES or None)
    # if request.method == "POST":
    #     content = request.POST.get("content")
    #     title = request.POST.get("title")
    #      Post.objects.create(title=title,content=content)
    #

    # form.cleaned_data
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        messages.success(request,"Successfully Created")
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        'form': form,
    }

    return render(request,"post_form.html",context=context)


def post_detail(request,slug=None):  # retrieve
    instance = get_object_or_404(Post,slug=slug)
    share_string = quote_plus(instance.content)
    context = {
        "title": instance.title,
        "instance":instance,
        "share_string": share_string,
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

    queryset_list = Post.objects.all()
    paginator = Paginator(queryset_list, 3)
    page_request_var = "page"
    page = request.GET.get(page_request_var)

    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    context = {
        "object_list":queryset,
        "title":"List",
        "page_request_var":page_request_var,
    }
    return render(request,"post_list.html",context=context)

def post_update(request,slug=None):
    instance = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None,request.FILES or None, instance=instance)
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


def post_delete(request,slug=None):
    instance = get_object_or_404(Post,slug=slug)
    instance.delete()
    messages.success(request,"Successfully Deleted")
    return redirect(post_list)