from django.shortcuts import render
from django.template import loader
from django.http import HttpResponseRedirect
from django.urls import reverse

from django_sorcery.shortcuts import get_object_or_404
# Create your views here.
from taxonomies.models import Taxonomy


def index(request):
    taxonomies = Taxonomy.objects.all()
    context = {'taxonomies': taxonomies}
    return render(request, 'taxonomies/index.html', context)
