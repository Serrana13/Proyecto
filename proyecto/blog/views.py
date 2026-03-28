from django.shortcuts import render

from django.shortcuts import render

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Post


def home(request):

    return render(request,"home.html")


def about(request):

    return render(request,"about.html")


class PostList(ListView):

    model = Post
    template_name = "pages.html"


class PostDetail(DetailView):

    model = Post
    template_name = "page_detail.html"


class PostCreate(LoginRequiredMixin, CreateView):

    model = Post

    fields = ["titulo","subtitulo","contenido","imagen","fecha"]

    template_name = "create_page.html"


class PostUpdate(LoginRequiredMixin, UpdateView):

    model = Post

    fields = ["titulo","subtitulo","contenido","imagen","fecha"]

    template_name = "edit_page.html"


class PostDelete(LoginRequiredMixin, DeleteView):

    model = Post

    success_url = "/pages/"

    template_name = "delete_page.html"