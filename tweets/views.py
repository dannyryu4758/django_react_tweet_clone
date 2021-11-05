from django.http.response import Http404, HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.conf import settings
import random
from django.utils.http import is_safe_url
from rest_framework import serializers
from rest_framework.response import Response

from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from tweets.models import Tweet
from tweets.serializers import TweetSerializer, TweetActionSerializer, TweetCreateSerializer
from .forms import TweetForm


ALLOWED_HOSTS = settings.ALLOWED_HOSTS


def home_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Home Page<h1>")
    return render(request, 'pages/home.html', context={}, status=200)


@api_view(['POST'])  # http method the client == POST
# @authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])  # REST API course
def tweet_create_view(request, *args, **kwargs):
    '''
    REST API Create View -> DRF(Django Rest Framework)
    '''
    serializer = TweetCreateSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data, status=201)
    return Response({}, status=400)


@ api_view(['GET'])
def tweet_detail_view(request, tweet_id, *args, **kwargs):
    qs = Tweet.objects.filter(id=tweet_id)
    if not qs.exists():
        return Response({}, status=404)
    obj = qs.first()
    serializer = TweetSerializer(obj)
    return Response(serializer.data, status=200)


@ api_view(['DELETE', 'POST'])
@permission_classes([IsAuthenticated])  # REST API course
def tweet_delete_view(request, tweet_id, *args, **kwargs):
    qs = Tweet.objects.filter(id=tweet_id)
    if not qs.exists():
        return Response({}, status=404)
    qs = qs.filter(user=request.user)
    if not qs.exists():
        return Response({"message": "해당 글을 삭제할 수 없습니다."}, status=401)
    obj = qs.first()
    obj.delete()
    return Response({"message": "해당 글을 삭제하였습니다."}, status=200)


@ api_view(['POST'])
@permission_classes([IsAuthenticated])  # REST API course
def tweet_action_view(request, *args, **kwargs):
    '''
    id is required.
    Action options are : like, unlike, retweet
    '''
    serializer = TweetActionSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        data = serializer.validated_data
        tweet_id = data.get("id")
        action = data.get("action")
        content = data.get("content")
        qs = Tweet.objects.filter(id=tweet_id)
        if not qs.exists():
            return Response({}, status=404)
        obj = qs.first()
        if action == "like":
            obj.likes.add(request.user)
            serializer = TweetSerializer(obj)
            return Response(serializer.data, status=200)
        elif action == "unlike":
            obj.likes.remove(request.user)
            serializer = TweetSerializer(obj)
            return Response(serializer.data, status=200)
        elif action == "retweet":
            new_tweet = Tweet.objects.create(user=request.user, parent=obj, content=content,)
            serializer = TweetSerializer(new_tweet)
            return Response(serializer.data, status=201)
    return Response({}, status=200)


@ api_view(['GET'])
def tweet_list_view(request, *args, **kwargs):
    qs = Tweet.objects.all()
    serializer = TweetSerializer(qs, many=True)
    return Response(serializer.data, status=200)


def tweet_create_view_pure_django(request, *args, **kwargs):
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


def tweet_list_view_pure_django(request, *args, **kwargs):
    qs = Tweet.objects.all()
    tweets_list = [x.serialize() for x in qs]
    data = {
        "isUser": False,
        "response": tweets_list,
    }
    return JsonResponse(data)


def tweet_detail_view_pure_django(request, tweet_id,  *args, **kwargs):
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
