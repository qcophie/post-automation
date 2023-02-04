from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .utils import tweepy_fn, validate_post_content, error_response, success_response
from rest_framework.status import HTTP_201_CREATED, HTTP_200_OK, HTTP_400_BAD_REQUEST


# Create your views here.
class PostContent(APIView):
    
    def post(self, request, *args, **kwargs):
        content = request.data.get('content', '')
        my_response = validate_post_content(request)
        
        if my_response.get("error"):
            return Response(error_response(my_response.get("error_message"), my_response.get("error_code")), status=HTTP_400_BAD_REQUEST)
        
        # Call Fortune's Function
        tweet = tweepy_fn(content="")
        
        # For success response
        return Response(success_response("Post Created Successfully"), status=HTTP_200_OK)
    
        # For error response
        return Response(error_response("Post not Created"), status=HTTP_400_BAD_REQUEST)
        
    
