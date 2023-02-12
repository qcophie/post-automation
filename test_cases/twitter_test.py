import json

import tweepy
import os
import requests


def test_no_content():
    # Get the base url from the environment
    base_url = os.environ.get("BASE_URL")
    
    # Specify the full URL
    url = f"{base_url}/api/v1/post/post_content/"
    
    payload = {
        "content": ""
    }
    
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    
    # Assert that 400 BAD REQUEST is returned
    assert response.status_code == 400
    

def test_available_content():
    # Get the base url from the environment
    base_url = os.environ.get("BASE_URL")
    
    # Specify the full URL
    url = f"{base_url}/api/v1/post/post_content/"
    
    payload = {
        "content": "Let's create some tweet automation with django "
    }
    
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    
    # Assert that the tweet was successfully posted.
    assert response.status_code == 200
