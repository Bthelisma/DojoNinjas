# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def index(request):
    context = {"dojos": Dojo.objects.all()}
    return render (request, "dojo_ninjas/index.html", context)
