from django.urls import path

from . import views

# This is where the url patterns for a specific app is stored (in this case the "blogs" app). You only define patterns here after removing the "top level url" i.e. someipaddr.com/blogs/5/results/ (only /5/results/ since someipaddr.com/blogs is "top level url")
app_name = "blogs" # for namespacing urls in non verbose implementation of url matching in the views.py and templates methods
urlpatterns = [
    path("", views.index, name = "index"),
    path("<int:blogpost_id>/", views.detail, name = "detail"),
    path("write/", views.create_blogpost, name = "create_blogpost"),
    # path("accounts/register/", views.register, name = register),
    path("login", views.login),
    path("signup", views.signup),
    path("test_token", views.test_token),
]