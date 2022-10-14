from django.http import HttpResponse
from django.template.loader import render_to_string
from django.views.generic import TemplateView

def index(request):
    return HttpResponse(render_to_string('index.html'))

class AboutView(TemplateView):
    template_name = 'about-us.html'

class BlogView(TemplateView):
    template_name = 'blog.html'