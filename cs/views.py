# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import Group
from django.shortcuts import redirect
from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.views.generic import View

User = get_user_model()

class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'charts.html', {"customers": 10})

def get_data(request, *args, **kwargs):
    data = {
        "sales": 100,
        "customers": 10,
    }
    return JsonResponse(data)


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        qs_count = User.objects.all().count()
        labels = ["Users", "Blue", "Yellow", "Green", "Purple", "Orange"]
        default_items = [qs_count, 23, 2, 3, 12, 2]
        data = {
                "labels": labels,
                "default": default_items,
        }
        return Response(data)


def login_success(request):
    """
    Redirects users based on whether they are in the admins group
    """
    if request.user.groups.filter(name="dg").exists():
        # user is a director general
        return redirect("dg")
    elif request.user.groups.filter(name="directors").exists():
        # user is an admin
        return redirect("nafdac")
    elif request.user.groups.filter(name="officers").exists():
        # user is an officer
        return redirect("agents")
    else:
        return redirect("index")


def home(request):
   return render_to_response('home.html')

def index(request):
   return render_to_response('index.html')

@login_required(login_url='/')
@user_passes_test(lambda u: Group.objects.get(name='dg') in u.groups.all())
def dg(request):
   return render_to_response('dg.html')

@login_required(login_url='/')
def agents(request):
   return render_to_response('agents.html')

@login_required(login_url='/')
def agents_form(request):
   return render_to_response('agents_form.html')

@login_required(login_url='/')
def nafdac(request):
   return render_to_response('nafdac.html')

@login_required(login_url='/')
#@group_required('dg','director')
def son(request):
   return render_to_response('son.html')

@login_required(login_url='/')
#@group_required('dg','director')
def others(request):
   return render_to_response('others.html')

# Create your views here.
