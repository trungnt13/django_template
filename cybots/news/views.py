from django.shortcuts import render_to_response
from django.template import RequestContext
from cybots.news.models import tmpnews
import cgi
# Create your views here.


def index(request):
	# if request.method == 'POST':
 #       # save new post
 #       title = request.POST['title']
 #       content = request.POST['content']

 #       post = Post(title=title)
 #       post.last_update = datetime.datetime.now()
 #       post.content = content
 #       post.save()
    news = tmpnews.objects[:20]
    return render_to_response('news/index.html', {'news': news},
                              context_instance=RequestContext(request))
