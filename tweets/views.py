from django.http.response import Http404, HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.conf import settings
import random
from django.utils.http import is_safe_url

from tweets.models import Tweet
from tweets.serializers import TweetSerializer
from .forms import TweetForm


ALLOWED_HOSTS = settings.ALLOWED_HOSTS


def home_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Home Page<h1>")
    return render(request, 'pages/home.html', context={}, status=200)


def tweet_create_view(request, *args, **kwargs):
    serializer = TweetSerializer(data=request.POST or None)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return JsonResponse(serializer.data, status=201)
    return JsonResponse({}, status=400)


def tweet_create_view_pure_django(request, *args, **kwargs):
    '''
    REST API Create View -> DRF(Django Rest Framework)
    '''
    user = request.user
    if not user.is_authenticated:
        if request.is_ajax():
            return JsonResponse({}, status=401)
        return redirect(settings.LOGIN_URL)
    form = TweetForm(request.POST or None)
    next_url = request.POST.get("next") or None  # AnonymousUser
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = user
        obj.save()
        if request.is_ajax():
            # 201 == created items
            return JsonResponse(obj.serialize(), status=201)
        if next_url != None and is_safe_url(next_url, ALLOWED_HOSTS):
            return redirect(next_url)
        form = TweetForm()
    if form.errors:
        if request.is_ajax():
            return JsonResponse(form.errors, status=400)
    return render(request, 'components/form.html', context={"form": form})


def tweet_list_view(request, *args, **kwargs):
    qs = Tweet.objects.all()
    tweets_list = [x.serialize() for x in qs]
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
