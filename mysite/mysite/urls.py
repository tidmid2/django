
# from django.contrib import admin
# from django.urls import path
# from django.conf.urls import url, include 

# urlpatterns = [
#     # path('admin/', admin.site.urls),
#     url(r'^', include('tutorials.urls')),
# ]


from django.urls import re_path, include 
 
urlpatterns = [ 
    re_path(r'^', include('tutorials.urls')),
    # re_path(r'^', tutorials.urls),
    # re_path(r'^articles/(?P<year>[0-9]{4})/$', views.year_archive)
]
