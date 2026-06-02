import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_healthz(client):
    # test xd
    resp = client.get("/healthz/")
    assert resp.status_code == 200
    assert resp.json() == {"status": "false"}