import os
import tempfile

import pytest
from twist import create_app

@pytest.fixture
def app():
    """Create and configure app instance for each test."""
    db_fd, db_path = tempfile.mkstemp()
    # create app with test config
    app = create_app({
        'TESTING': True,
        'DATABASE': db_path,
    })

    yield app

@pytest.fixture
def client(app):
    """test client for twist"""
    return app.test_client()

def test_hello(client):
    response = client.get("/hello/sean")
    assert b"Hello, sean" in response.data
    response = client.get("/hello/heather")
    assert b"Hello, heather" in response.data


