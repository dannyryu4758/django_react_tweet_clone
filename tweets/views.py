from django.http.response import Http404, HttpResponse, JsonResponse
from django.shortcuts import render
import random

from tweets.models import Tweet


def home_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Home Page<h1>")
    return render(request, 'pages/home.html', context={}, status=200)


def tweet_list_view(request, *args, **kwargs):
    qs = Tweet.objects.all()
    tweets_list = [{"id": x.id, "content": x.content, "likes": random.randint(0, 999)}
                   for x in qs]
    data = {
        "isUser": False,
        "response": tweets_list,
    }
    return JsonResponse(data)


def tweet_detail_view(request, tweet_id,  *args, **kwargs):
    data = {
        "id": tweet_id,
    }
    status = 200
    try:
        obj = Tweet.objects.get(id=tweet_id)
        data['content'] = obj.content
        # data['image_path'] = obj.image
    except:
        # raise Http404
        data['message'] = "Not found"
        status = 404

    # json.dumps content_type = 'application/json'
    return JsonResponse(data, status=status)
