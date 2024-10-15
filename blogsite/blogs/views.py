from django.shortcuts import render, get_object_or_404
from .models import BlogPost
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view,authentication_classes, permission_classes
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

# These functions are called when accessing specific url pages
# sequence: urls.py -> views.py -> /templates/app/xxxxx.html

# Create your views here.
def index(request):
    # VERBOSE VERSION
    # # return HttpResponse("Hello!, you are in the blogs index.")
    # all_blogs = BlogPost.objects.order_by("-created_at")
    # template = loader.get_template("blogs/index.html")
    # context = {
    #     "all_blogs": all_blogs,
    # }
    # # output = "\n".join([bp.title for bp in all_blogs])
    # return HttpResponse(template.render(context, request))

    # NON VERBOSE VERSION - ish:
    all_blogs = BlogPost.objects.order_by("-created_at")
    context = {
        "all_blogs": all_blogs,
    }
    return render(request, "blogs/index.html", context)

def detail(request, blogpost_id):
    blogpost = get_object_or_404(BlogPost, pk=blogpost_id)
    return render(request, "blogs/detail.html", {"blogpost":blogpost})

def create_blogpost(request):
    return render(request, "blogs/create_blogpost.html")



@api_view(['POST'])
def login(request):
    user = get_object_or_404(User, username=request.data['username'])
    if not user.check_password(request.data['password']):
        return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)
    token = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(user)
    return Response({"token": token[0].key, "user": serializer.data})

@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username=request.data['username'])
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return Response({"token": token.key, "user": serializer.data})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):
    """Check if auth token is still valid"""
    return Response("Passed for %s" % (request.user.email))
