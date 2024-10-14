from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader

from .models import BlogPost

# Create your views here.
def index(request):
    # return HttpResponse("Hello!, you are in the blogs index.")
    all_blogs = BlogPost.objects.order_by("-created_at")
    template = loader.get_template("blogs/index.html")
    context = {
        "all_blogs": all_blogs,
    }
    # output = "\n".join([bp.title for bp in all_blogs])
    return HttpResponse(template.render(context, request))

    ''' # NON VERBOSE VERSION - ish:
    all_blogs = BlogPost.objects.order_by("-created_at")
    context = {
        "all_blogs": all_blogs,
    }
    return render(request, "polls/index.html", context)
    '''

def detail(request, blogpost_id):
    
    ''' NON VERBOSE-ish
    try:
        blog = BlogPost.objects.get(pk = blogpost_id)
    except BlogPost.DoesNotExist:
        raise Http404("BlogPost does not exist.")
    return render(request, "blogs/detail.html", {"blogpost": blogpost})
    '''
    blogpost = get_object_or_404(BlogPost, pk=blogpost_id)
    return render(request, "blogs/detail.html", {"blogpost":blogpost})

def vote(request, blogpost_id):
    return HttpResponse("You are voting on blogpost %s" % (blogpost_id))