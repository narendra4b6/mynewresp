from django.shortcuts import render,get_object_or_404,redirect
from myapp.forms import SignUpForm
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse,reverse_lazy
from django.views.generic import TemplateView,CreateView,View,UpdateView,DeleteView,ListView,DetailView
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from myapp.models import Post,Comment
from myapp.forms import PostForm,CommentForm
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    if 'q' in request.GET:
        q=request.GET['q']
        if(len(q)!=0):
            posts=Post.objects.filter(title__icontains=q)
        else:
            posts=Post.objects.filter(publish_date__lte=timezone.now()).order_by('-publish_date')
    else:
        posts=Post.objects.filter(publish_date__lte=timezone.now()).order_by('-publish_date')
    paginator=Paginator(posts,5)
    page_number=request.GET.get('page')
    posts_obj=paginator.get_page(page_number)


    return render(request,'myapp/post_list.html',{'posts':posts_obj})
class register(CreateView):
    form_class=SignUpForm
    template_name="register/registration.html"
    success_url=reverse_lazy('login')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def add(request):
    if(request.method=="POST"):
        form=PostForm(request.POST,request.FILES)
        if(form.is_valid()):
            form.save()
            messages.success(request,'Post Added Successfully')
        else:
            messages.success(request,"Please Enter Mandatory Details")

    else:
        form=PostForm()


    return render(request,"myapp/post_form.html",{'form':form})

@login_required
def drafts(request):
    posts=Post.objects.filter(publish_date__isnull=True).order_by('create_date')
    return render(request,"myapp/post_draft.html",{'posts':posts})


class PostDetail(DetailView):
    model=Post

class PostUpdate(LoginRequiredMixin,UpdateView):
    login_url='/login/'
    model=Post
    form_class=PostForm
    redirect_field_name="myapp/post_detail.html"

@login_required
def delete(request,pk):
    Post.objects.filter(pk=pk).delete()
    return HttpResponseRedirect(reverse("index"))

@login_required
def post_publish(request,pk):
    post=get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect('post_detail',pk=pk)
@login_required
def add_comment_post(request,pk):
    post=get_object_or_404(Post,pk=pk)
    if(request.method=="POST"):
        form=CommentForm(request.POST)
        if(form.is_valid()):
            comment=form.save(commit=False)
            comment.post=post
            comment.save()
            return redirect("post_detail",pk=post.pk)
    else:
        form=CommentForm()
    return render(request,'myapp/comment_form.html',{'form':form})

@login_required
def comment_approve(request,pk):
    comment=get_object_or_404(Comment,pk=pk)
    comment.approve()
    return redirect('post_detail',pk=comment.post.pk)

@login_required
def comment_delete(request,pk):
    comment=get_object_or_404(Comment,pk=pk)
    post_pk=comment.post.pk
    comment.delete()
    return redirect('post_detail',post_pk)
