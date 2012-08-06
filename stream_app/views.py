# our code
from stream_app.models import Stream, User

# django imports
from django.shortcuts               import (get_list_or_404, get_object_or_404, render_to_response,
                                            render)
from django.views.decorators.http   import require_http_methods, require_GET, require_POST
from django.http                    import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers       import reverse
from django.core                    import serializers
from django.contrib.auth.decorators import login_required
from django.utils                   import simplejson
from django.forms.models            import model_to_dict

# other imports
from datetime import datetime, date
from operator import itemgetter
import time


def index(request):
    return render(request, 'stream_app/index.html')

@login_required
def logout(request):
    logout(request)
    return render(request, 'stream_app/index.html')

@login_required
def login_landing(request):
    return render(request, 'stream_app/landing_page.html')

@require_http_methods(['GET', 'POST'])
def register(request, email, password):
    if request.method == 'GET':  return render(request, 'stream_app/register.html')
    u = User.objects.get_or_create(email=email)

@login_required
@require_POST
def show_me(request):
    # why does this not work? -> def show_me(request,entry):
    entry = request.REQUEST['entry']
    print '%%%%%%%%%%%%%%%%%%%%', entry
    return HttpResponse("GOOD ENOUGH FOR GOV'T WORK", mimetype='text/plain')

@login_required
@require_POST
def stream_save(request):
    s, was_created = Stream.objects.get_or_create(name=request.POST['stream_name'], user=request.user)
    if was_created:
        s.name        = request.POST['stream_name']
        s.start_time  = request.POST['start_time']
        s.end_time    = time.time()
        s.entries     = request.POST.getlist('words')
        print s.entries
        print request.POST.getlist('words')
        s.entry_count = len(s.entries)
        s.user        = request.user
        print dir(s)
        return HttpResponse('saved stream!', mimetype='text/plain')
    else: #already exists
        # TODO: return already made, force new name
        print 'skipped making'
        return HttpResponse('already exists', mimetype='text/plain')
    



