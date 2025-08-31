from django.shortcuts import render,get_object_or_404
from blog.models import Post
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

# Create your views here.
def blog_view(request,**kwargs):
     posts = Post.objects.filter(status=1)
     if kwargs.get('cat_name') != None:
          posts = posts.filter(category__name=kwargs['cat_name'])
     if kwargs.get('author_username') != None:
          posts = posts.filter(author__username = kwargs['author_username'])
     posts = Paginator(posts,3)
     try:
          page_number = request.GET.get('page')
          posts = posts.get_page(page_number)
     except PageNotAnInteger:
          posts = posts.get_page(1)
     except EmptyPage:
          posts = posts.get_page(1)
     context = {'posts':posts}
     return render(request,'blog/blog-home.html',context)

def blog_single(request,pid):
     posts = Post.objects.filter(status=1)
     post = get_object_or_404(Post,pk=pid)
     context = {'post':post}
     return render(request,'blog/blog-single.html',context)

     #context = {'title':'bitcoin crashed again!', 'content': 'bitcoin was flying but now grounded as always', 'author':'somayehhosseinbeig'}
     #return render(request,'blog/blog-single.html', context)
     
""" def test(request):
     posts = Post.objects.all()
     # posts = Post.objects.filter(status=0)
     context = {'posts':posts}
     return render(request,'test.html',context) """

""" def test(request,pid):
     #post = Post.objects.get(id=pid)
     post = get_object_or_404(Post,pk=pid)
     context = {'post':post}
     return render(request,'test.html',context) """

def test(request):
     return render(request,'test.html')

def blog_category(request,cat_name):
     posts = Post.objects.filter(status=1)
     posts = posts.filter(category__name=cat_name)
     context = {'posts':posts}
     return render(request,'blog/blog-home.html',context)

def blog_search(request):
     posts = Post.objects.filter(status=1)
     if request.method == 'GET' :
          #print(request.GET.get('s'))
          if s :=request.GET.get('s'):
               posts = posts.filter(content__contains=s)
     
     context = {'posts':posts}
     return render(request,'blog/blog-home.html',context)