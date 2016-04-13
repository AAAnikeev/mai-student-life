from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render_to_response
from django.template import RequestContext

from .models import *


def community_list(request):
    template_name = 'community/list.html'
    paginator = Paginator(Community.objects.all(), 5)

    try:
        items = paginator.page(request.GET.get('page'))
    except (PageNotAnInteger, EmptyPage):
        items = paginator.page(1)

    return render_to_response(template_name, {"community_list": items}, context_instance=RequestContext(request))


def detail(request, community_id):
    template_name = 'community/detail.html'
    community = Community.objects.get(pk=community_id)
    return render_to_response(template_name, {"community": community}, context_instance=RequestContext(request))
