import pytest

def test_hello(client):
    """test the hello endpoint"""
    response = client.get("/hello/sean")
    assert b"Hello, sean" in response.data
    response = client.get("/hello/heather")
    assert b"Hello, heather" in response.data
