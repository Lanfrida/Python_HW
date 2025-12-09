import requests
import pytest


BASE_URL = "https://ru.yougile.com/api-v2"
TOKEN = ""
HEADERS = {"Authorization": f"Bearer {TOKEN}"}

def test_create_project_post():
    payload = {
        "title": "autotest"
    }
    r = requests.post(
        f"{BASE_URL}/projects",
        json=payload,
        headers=HEADERS,
    )
    assert r.status_code == 201, r.text
    body = r.json()
    assert isinstance(body.get("id"), str)
    assert body["id"]


def test_create_project_post_negative():
    payload = {
        "title": "autotest"
    }
    r = requests.post(
        f"{BASE_URL}/projects",
        json=payload,
    )
    assert r.status_code == 401, r.text

def test_change_project_post():
    payload = {
         "title": "autotest"
    }
    r = requests.post(
        f"{BASE_URL}/projects",
        json=payload,
        headers=HEADERS,
    )
    assert r.status_code == 201, r.text
    body = r.json()
    assert isinstance(body.get("id"), str)
    assert body["id"]
    project_id = r.json()["id"]
    new_title = "new tittle"
    r_put = requests.put(
        f"{BASE_URL}/projects/{project_id}",
        json={"title": new_title},
        headers=HEADERS,
    )
    assert r_put.status_code == 200, r_put.text
    assert r_put.json().get("id") == project_id

def test_change_project_post_negative():
    payload = {
         "title": "autotest"
    }
    r = requests.post(
        f"{BASE_URL}/projects",
        json=payload,
        headers=HEADERS,
    )
    assert r.status_code == 201, r.text
    body = r.json()
    assert isinstance(body.get("id"), str)
    assert body["id"]
    project_id = r.json()["id"]
    new_title = ""
    r_put = requests.put(
        f"{BASE_URL}/projects/{project_id}",
        json={"title": new_title},
        headers=HEADERS,
    )
    assert r_put.status_code == 400, r_put.text

def test_get_project_post():
    payload = {
         "title": "autotest"
    }
    r = requests.post(
        f"{BASE_URL}/projects",
        json=payload,
        headers=HEADERS,
    )
    assert r.status_code == 201, r.text
    body = r.json()
    assert isinstance(body.get("id"), str)
    assert body["id"]
    project_id = r.json()["id"]
    r_get = requests.get(
        f"{BASE_URL}/projects/{project_id}",
        headers=HEADERS,
    )
    assert r_get.status_code == 200, r_get.text
    assert r_get.json().get("id") == project_id

def test_get_project_post_negative():
    project_id = "46483929272"
    r_get = requests.get(
        f"{BASE_URL}/projects/{project_id}",
        headers=HEADERS,
    )
    assert r_get.status_code == 404, r_get.text