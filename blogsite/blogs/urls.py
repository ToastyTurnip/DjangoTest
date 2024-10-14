from django.urls import path

from . import views

# This is where the url patterns for a specific app is stored (in this case the "blogs" app). You only define patterns here after removing the "top level url" i.e. someipaddr.com/blogs/5/results/ (only /5/results/ since someipaddr.com/blogs is "top level url")
urlpatterns = [
    path("", views.index, name = "index"),
    path("<int:blogpost_id>/", views.detail, name = "detail"),
    path("<int:blogpost_id>/", views.vote, name = "vote"),
]