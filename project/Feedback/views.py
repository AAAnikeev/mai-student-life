from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import FeedbackForm

from .models import *


def community_list(request):
    template_name = 'community/list.html'
    paginator = Paginator(Community.objects.all(), 5)

    try:
        items = paginator.page(request.GET.get('page'))
    except (PageNotAnInteger, EmptyPage):
        items = paginator.page(1)

    return render(request, template_name, {"community_list": items})


def detail(request, community_id):
    template_name = 'community/detail.html'
    community = Community.objects.get(pk=community_id)
    return render(request, template_name, {"community": community})
    from django.shortcuts import render
from django.http import HttpResponseRedirect


def feedback(request):
    if request.method =='GET':
    	form = FeedbackForm()
    	return render(request, 'feedback/feedback.html', {'form': form})
    if request.method == 'POST':
    	form = FeedbackForm(request.POST)
    	if form.is_valid():
    	 	print (form.cleaned_data['text'])
    	 	text=form.cleaned_data['text']
    	form = FeedbackMessage.objects.text=text
    	return render(request, 'feedback/feedback.html', {'form': form})
