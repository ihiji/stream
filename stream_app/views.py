# our code
from stream_app.models import Stream, User, Word

# django imports
from django.shortcuts               import (get_list_or_404, get_object_or_404, render_to_response,
                                            render)
from django.views.decorators.http   import require_http_methods, require_GET, require_POST
from django.http                    import HttpResponseRedirect, HttpResponse, Http404
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
    return HttpResponse("GOOD ENOUGH FOR GOV'T WORK", mimetype='text/plain')

@login_required
@require_POST
def stream_save(request):
    s, was_created = Stream.objects.get_or_create(name=request.POST['stream_name'], user=request.user)
    if not was_created:
        # TODO: return already made, force new name
        resp = HttpResponse('already exists', mimetype='text/plain')
    else: 
        s.name        = request.POST['stream_name'].strip()
        s.start_time  = request.POST['start_time'].strip()
        s.end_time    = time.time()
        s.entries     = [w.strip() for w in request.POST.getlist('words')]
        s.entry_count = len(s.entries)
        s.user        = request.user
        s.save()
        s.push_down_info()
        resp = HttpResponse('saved stream!', mimetype='text/plain')
    return resp

@login_required
def user_streams(request):
    streams = Stream.objects(user=request.user)
    streams = sorted(streams, key=lambda s: s.name)
    return render_to_response('stream_app/stream_list.html', {'streams':streams})

@login_required
def stream_viewer(request, stream_name):
    try:
        stream = Stream.objects.get(user=request.user, name=stream_name)
    except: # should catch no document
        raise Http404
    return render_to_response('stream_app/stream_inspect.html', {'entries':stream.entries})

@login_required
def word_viewer(request, word):
    print word
    try:
        word = Word.objects.get(word=word)
    except Exception, e: # should catch no document
        print e
        raise Http404
    return render_to_response('stream_app/word_inspect.html', {'word':word.word, 'hits':word.hits, 'stream_count':word.stream_count})
