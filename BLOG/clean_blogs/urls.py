from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve
from django.conf.urls import url


urlpatterns = [
    path('',views.BlogPostList.as_view(template_name = 'index.html'), name='home'),
    path('index/',views.BlogPostList.as_view(template_name = 'index.html'), name='home'),
    path('blogs/', views.BlogPostList.as_view(template_name = 'blogs.html'), name='blogs'),
    path('projects/', views.projects, name='projects'),
    path('books/', views.books, name='books'),
    path('contact/', views.contact, name='contact'), 
    path('<slug:slug>/', views.BlogPostDetail.as_view(), name='post'),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':     settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root':     settings.STATIC_ROOT}),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
