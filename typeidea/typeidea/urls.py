"""typeidea URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from blog.views import IndexView, CategoryView, TagView, PostDetailView, SearchView, AuthorView
# from config.views import links
from config.views import LinkListView
from comment.views import CommentView
from typeidea.custom_site import custom_site


urlpatterns = [
#    path('', post_list, name='index'),
#    path('category/<category_id>/', post_list, name='category-list'),
#    path('tag/<tag_id>/', post_list, name='tag-list'),
#    path('post/<post_id>.html', post_detail, name='post-detail'),
    path('', IndexView.as_view(), name='index'),
    path('category/<category_id>/', CategoryView.as_view(), name='category-list'),
    path('tag/<tag_id>/', TagView.as_view(), name='tag-list'),
    path('post/<post_id>.html', PostDetailView.as_view(), name='post-detail'),
    path('links/', LinkListView.as_view(), name='links'),
    path('super_admin/', admin.site.urls, name='super-admin'),
    path('admin/', custom_site.urls, name='admin'),
    path('search', SearchView.as_view(), name='search'),
    path('author/<owner_id>', AuthorView.as_view(), name='author'),
    path('comment/', CommentView.as_view(), name='comment'),
]
