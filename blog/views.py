from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from .forms import CustomUserCreationForm

from .models import Topic, Blog, User


# Create your views here.
class CustomLogin(LoginView):
    template_name = 'blog/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('blog')

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('blog')
        return super(CustomLogin, self).get(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CustomLogin, self).get_context_data(**kwargs)
        context['topics'] = Topic.objects.all()
        return context


class RegisterUser(FormView):
    template_name = 'blog/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('blog')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterUser, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('blog')
        return super(RegisterUser, self).get(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(RegisterUser, self).get_context_data(**kwargs)
        context['topics'] = Topic.objects.all()
        return context


class BlogList(ListView):
    model = Blog
    context_object_name = 'blogs'

    def get_context_data(self, **kwargs):
        context = super(BlogList, self).get_context_data(**kwargs)

        query = self.request.GET.get('query') or ''
        if query:
            context['blogs'] = context['blogs'].filter(topic__topic_title=query)

        search_blog = self.request.GET.get('search_blog') or ''
        if search_blog:
            context['blogs'] = context['blogs'].filter(blog_title__startswith=search_blog)
        context['search_blog'] = search_blog

        context['topics'] = Topic.objects.all()
        return context


class BlogDetail(DetailView):
    model = Blog
    context_object_name = 'blog'

    def get_context_data(self, **kwargs):
        context = super(BlogDetail, self).get_context_data(**kwargs)
        context['topics'] = Topic.objects.all()
        return context


class BlogCreate(LoginRequiredMixin, CreateView):
    model = Blog
    fields = ['topic', 'blog_title', 'blog_image', 'blog_description']
    success_url = reverse_lazy('blog')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(BlogCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(BlogCreate, self).get_context_data(**kwargs)
        context['topics'] = Topic.objects.all()
        return context


class BlogUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'blog/blog_edit_form.html'
    model = Blog
    fields = ['topic', 'blog_title', 'blog_image', 'blog_description']
    success_url = reverse_lazy('blog')

    def get_context_data(self, **kwargs):
        context = super(BlogUpdate, self).get_context_data(**kwargs)
        context['topics'] = Topic.objects.all()
        return context


class BlogDelete(LoginRequiredMixin, DeleteView):
    model = Blog
    context_object_name = 'blog'
    success_url = reverse_lazy('blog')

    def get_context_data(self, **kwargs):
        context = super(BlogDelete, self).get_context_data(**kwargs)
        context['topics'] = Topic.objects.all()
        return context


class UserDetail(DetailView):
    model = User
    context_object_name = 'current_user'

    def get_context_data(self, **kwargs):
        context = super(UserDetail, self).get_context_data(**kwargs)
        context['topics'] = Topic.objects.all()
        return context


class UserUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'blog/user_form.html'
    model = User
    fields = ['username', 'name', 'email', 'bio', 'user_avatar']
    success_url = reverse_lazy('blog')

    def get_context_data(self, **kwargs):
        context = super(UserUpdate, self).get_context_data(**kwargs)
        context['topics'] = Topic.objects.all()
        return context
