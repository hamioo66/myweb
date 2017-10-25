# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.template import loader,Context
from django.http import HttpResponse
from  blog.models import BlogPost

# Create your views here.
def archive(request):
    posts=BlogPost.objects.all()
    
