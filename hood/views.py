from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
from .models import Project,Profile,Review
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from .forms import ProjectForm,ProfileForm,VoteForm,ReviewForm
from django.contrib.auth import logout
from rest_framework.response import Response
