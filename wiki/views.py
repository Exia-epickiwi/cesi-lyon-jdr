# -*- coding: utf-8 -*-
import markdown
from django.http import Http404, HttpResponse
from django.shortcuts import render,redirect
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime
from wiki.models import Article, Redirection, Media
from wiki.forms import EditArticleForm, CreateArticleForm, AddMessageForm, AddMediaForm
from users import views as authViews
from django.contrib import messages

def home(request):
    """Adresse de base du wiki affichant la page avec le slug home"""

    return redirect(showArticle,"wikihome")

def showArticle(request,slug):
    """Affiche l'article demandé a l'utilisateur"""

    try:
        article = Article.objects.get(slug=slug)
    except ObjectDoesNotExist:
        try:
            redirection = Redirection.objects.get(slug=slug)
            return redirect(showArticle,slug=redirection.article.slug)
        except ObjectDoesNotExist:
            return render(request, 'wiki/notFoundArticle.html', locals())

    if request.method == "POST":
        if not request.user.is_authenticated():
            messages.warning(request,"Vous devez vous connecter pour ajouter un message à l'article")
            return redirect(authViews.connect)

        addMessageForm = AddMessageForm(request.POST)
        if addMessageForm.is_valid():
            message = addMessageForm.save(commit=False)
            message.article = article
            message.author = request.user
            message.save()
            return redirect(showArticle,slug=slug)
    else:
        addMessageForm = AddMessageForm()

    return render(request, 'wiki/showArticle.html', locals())

def createArticle(request,slug):

    if not request.user.is_authenticated():
        messages.warning(request,"Vous devez vous connecter pour creer un article")
        return redirect(authViews.connect)

    if request.method == "POST":
        form = CreateArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.refreshSlug()
            article.save()
            article.makeModification(request.user)
            print(slug)
            if article.slug != slug and slug != "None":
                redirection = Redirection()
                redirection.slug = slug
                redirection.article = article
                redirection.save()
            return redirect(showArticle,slug=article.slug)
    else:
        form = CreateArticleForm()

    return render(request, "wiki/createArticle.html", locals())

def editArticle(request,slug):

    if not request.user.is_authenticated():
        messages.warning(request,"Vous devez vous connecter pour editer l'article")
        return redirect(authViews.connect)

    try:
        article = Article.objects.get(slug=slug)

    except ObjectDoesNotExist:
        try:
            redirection = Redirection.objects.get(slug=slug)
            return redirect(showArticle,slug=redirection.article.slug)

        except ObjectDoesNotExist:
            return render(request, 'wiki/notFoundArticle.html', locals())

    if request.method == "POST":
        form = EditArticleForm(request.POST,instance=article)

        if form.is_valid():
            article = form.save(commit=False)
            article.refreshSlug()
            article.makeModification(request.user)
            article.save()

            if article.slug != slug:
                redirection = Redirection()
                redirection.slug = slug
                redirection.article = article
                redirection.save()

            return redirect(showArticle,slug=slug)

    else:

        form = EditArticleForm(instance=article)

    medias = Media.objects.all().order_by("name")
    mediaForm = AddMediaForm()
    return render(request, "wiki/editArticle.html", locals())

def addMedia(request):
    if request.method == "POST" and request.user.is_authenticated():
        form = AddMediaForm(request.POST,request.FILES)
        if form.is_valid():
            newMedia = form.save(commit=False)
            newMedia.author = request.user
            newMedia.save()
            return render(request,"wiki/newMedia.json",locals())
        else:
            invalid = HttpResponse(form.errors.as_json(),content_type="application/javascript")
            invalid.status_code = 400
            return invalid
    else:
        raise Http404()