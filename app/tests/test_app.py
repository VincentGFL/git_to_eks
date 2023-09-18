import pytest
import requests

from flask import url_for
from app import app

def get_page(search_url):
  page = requests.get(search_url)
  return page

def test_page_response():
   test_url = "http://localhost:5000/"
   response = get_page(test_url)
   assert response.status_code == 200

def test_content():
    test_url = "http://localhost:5000/"
    response = get_page(test_url)
    assert b"Hello World 2" in response

# def test_content_2():
#     test_url = "http://localhost:5000/"
#     response = get_page(test_url)
#     assert b"Hello World!!!" in response