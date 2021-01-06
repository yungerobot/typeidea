from django.db.models import Q  # 引入Django提供的条件表达式conditional expression，用来完成复杂的操作
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic import ListView

from .models import Post,Tag,Category
# from comment.forms import CommentForm
# from comment.models import Comment
from config.models import SideBar

# Create your views here.
class CommonViewMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'sidebars':SideBar.get_all(),
        })
        context.update(Category.get_navs())
        return context



class IndexView(CommonViewMixin, ListView):
#    queryset = Post.latest_posts()
    queryset = Post.objects.filter(status=Post.STATUS_NORMAL)
    paginate_by = 5
    context_object_name = 'post_list'
    template_name = 'blog/list.html'


class CategoryView(IndexView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_id = self.kwargs.get('category_id')
        category = get_object_or_404(Category, pk=category_id)
        context.update({
            'category':category,
        })
        return context

    def get_queryset(self):
        """ 重写queryset,根据分类过滤 """
        queryset = super().get_queryset()
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category_id=category_id)


class TagView(IndexView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag_id = self.kwargs.get('tag_id')
        tag = get_object_or_404(Tag, pk=tag_id)
        context.update({
            'tag':tag,
        })
        return context

    def get_queryset(self):
        """ 重写queryset,根据标签过滤 """
        queryset = super().get_queryset()
        tag_id = self.kwargs.get('tag_id')
        return queryset.filter(tag_id=tag_id)



class PostListView(CommonViewMixin, ListView):
#    queryset = Post.latest_posts()
    queryset = Post.objects.filter(status=Post.STATUS_NORMAL)
    paginate_by = 1
    context_object_name = 'post_list'   # 如果不设置此项，在模板中需要使用object_list变量
    template_name = 'blog/list.html'



class PostDetailView(CommonViewMixin, DetailView):
#    queryset = Post.latest_posts()
    # model = Post
    queryset = Post.objects.filter(status=Post.STATUS_NORMAL)
    template_name = 'blog/detail.html'
    context_object_name = 'post'
    pk_url_kwarg = 'post_id'

"""
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'comment_form':CommentForm,
            'comment_list':Comment.get_by_target(self.request.path),
        })
        return context
"""



class SearchView(IndexView):
    def get_context_data(self):
        context = super().get_context_data()
        context.update({
            'keyword':self.request.GET.get('keyword', '')
        })
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        keyword = self.request.GET.get('keyword')
        if not keyword:
            return queryset
        return queryset.filter(Q(title__icontains=keyword) | Q(desc__icontains=keyword))



class AuthorView(IndexView):
    def get_queryset(self):
        queryset = super().get_queryset()
        author_id = self.kwargs.get('owner_id')
        return queryset.filter(owner_id=author_id)

