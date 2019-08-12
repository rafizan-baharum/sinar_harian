from django.shortcuts import render
from django.template import loader
from django.http import HttpResponseRedirect
from django.urls import reverse

from django_sorcery.shortcuts import get_object_or_404

from .models import Article, Comment, db
from django.contrib.staticfiles import finders


def index(request):
    result = finders.find('css/font-face.css')
    searched_locations = finders.searched_locations
    print(searched_locations)


    articles = Article.objects.order_by(Article.published_date.desc())[:5]
    context = {'sinar_harian': articles}
    return render(request, 'articles/index.html', context)


def detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'articles/detail.html', {'article': article})


def results(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'articles/results.html', {'article': article})


def comment(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    comment = request.POST['comment']

    if not comment:
        return render(request, 'articles/detail.html', {
            'article': article,
            'error_message': "You didn't have any commnet.",
        })

    db.flush()
    return HttpResponseRedirect(reverse('article:results', args=(article.id,)))
