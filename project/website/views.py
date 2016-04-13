from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext


def index(request):
    return redirect(reverse('community:list'))


def about(request):
    template_name = 'website/about.html'
    return render_to_response(template_name, context_instance=RequestContext(request))
