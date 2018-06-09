from django.contrib.auth import authenticate, login, logout
from django.forms import forms
from django.shortcuts import render, render_to_response, get_object_or_404, redirect, HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.contrib import messages
from Complete_Blog.text_message import send_text_message
from .models import Post, Comment, UserProfile
from .forms import BlogFrom, SuggestionForm, ReplyForm
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.

class Fun(ListView, View):
    template_name = "blog/Home.html"
    context_object_name = 'post'

    def get_queryset(self):
        return Post.objects.all()

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            print(request.POST)
            if request.POST.get('password') == request.POST.get('password_confirmation') and request.POST.get('psw') is None:
                username = request.POST.get('username')
                password = request.POST.get('password')
                email = request.POST.get('email')

                if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                    User.objects.create_user(username, email, password)
                    user = authenticate(username=username, password=password)
                    login(request, user)
                    redirect('blog:index')
                else:
                    raise forms.ValidationError('Looks like a username with that email or password already exists')

            elif request.POST.get('psw') is not None:
                username = request.POST.get('username')
                password = request.POST.get('psw')
                user = authenticate(username=username, password=password)
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        # request.user.username to get data
                        return redirect('blog:index')
                else:
                    print(request.POST)
                    return HttpResponse('<h1>signup</h1>')

        return render(request, 'blog/Home.html')


class Post_(DetailView):
    model = Post
    template_name = 'blog/details.html'

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            print(request.POST)
            if request.POST.get('password') == request.POST.get('password_confirmation') and request.POST.get('psw') is None:
                username = request.POST.get('username')
                password = request.POST.get('password')
                email = request.POST.get('email')

                if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                    User.objects.create_user(username, email, password)
                    user = authenticate(username=username, password=password)
                    login(request, user)
                    redirect('blog:index')
                else:
                    raise forms.ValidationError('Looks like a username with that email or password already exists')

            elif request.POST.get('psw') is not None:
                username = request.POST.get('username')
                password = request.POST.get('psw')
                user = authenticate(username=username, password=password)
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        # request.user.username to get data
                        return redirect('blog:index')
                else:
                    print(request.POST)
                    return HttpResponse('<h1>signup</h1>')

        return render(request, 'blog/Home.html')



@login_required
def comment_(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = BlogFrom(request.POST)
        if form.is_valid():
            comment_item = form.save(commit=False)
            comment_item.post = post
            comment_item.user_name = request.user
            comment_item.save()
            # send_text_message('{0} is commented on your post {1} Comment is {2}'.format(request.POST.get('user_name'),post,request.POST.get('comment')))
            return HttpResponse("<h1>Thank You</h1>" \
                                "<meta http-equiv='Refresh' content='0;url=/{0}'>".format(
                post.id))
    else:
        form = BlogFrom()
    return render(request, 'blog/comment_form.html', {'form': form})

def suggestion(request):
    if request.method == 'POST':
        form = SuggestionForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
            """msg = send_text_message(
                '\nsuggestion on your blog \nUser:{0}\nEmail:{1}\nTitle:{2}\nSuggestion: {3}'.format(
                    request.POST.get('user')
                    , request.POST.get('e_mail'), request.POST.get('suggestion_title'), request.POST.get('suggestion')))"""
    else:
        form = SuggestionForm()

    return render(request, 'blog/suggestion_form.html', {'form': form})


def about(request):
    return render(request, 'blog/contact.html')


@login_required
def reply(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply_item = form.save(commit=False)
            reply_item.comment = comment
            reply_item.user_name = request.user
            reply_item.save()
            messages.success(request, "Successfully commented")
            # send_text_message('{0} is Replied on Comment {1} Reply is {2}'.format(request.POST.get('user_name'),comment,request.POST.get('reply')))
            return HttpResponse("<h1>Thank You</h1>" \
                                "<meta http-equiv='Refresh' content='0;url=/{0}'>".format(
                comment.post.id))
        else:
            messages.error(request, "Not commented")
    else:
        form = ReplyForm()
    return render(request, 'blog/comment_form.html', {'form': form})

class ProfileView(DetailView,View):
    model = UserProfile
    template_name = 'blog/userprofile.html'

def profileview(request):
    return render(request,'blog/userprofile.html',{'userprofile':UserProfile})