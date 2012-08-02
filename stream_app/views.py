# our code
from stream_app.models import Stream, User

# other peoples libs (including buildins)
from django.shortcuts import get_list_or_404, get_object_or_404, render_to_response, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.utils import simplejson
from django.forms.models import model_to_dict
from datetime import datetime, date
import time
from operator import itemgetter


def index(request):
    return render(request, 'stream_app/index.html')

def login_landing():
    return render(request, 'stream_app/landing_page.html')
