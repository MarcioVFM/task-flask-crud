import pytest
import requests

#CRUD
BASE_URL = 'http://127.0.0.1:5000'
tasks = []

def test_creat_task():
    new_task_data = {
        "title": "Titulo da nova task",
        "description": "Descricao da nova task"
    }
    response = requests.post(f"{BASE_URL}/tasks", json=new_task_data)
    assert response.status_code == 200
    response_json = response.json()
    assert "message" in response_json
    assert "id" in response_json
    tasks.append(response_json['id'])

def test_get_tasks():
    response = requests.get(f"{BASE_URL}/tasks")
    assert response.status_code == 200
    response_json = response.json()
    assert "tasks" in response_json
    assert "total_tasks" in response_json

def test_get_task():
    if tasks:
        task_id = tasks[0]
        response = requests.get(f"{BASE_URL}/task/{task_id}")
        assert response.status_code == 200
        response_json = response.json()
        assert task_id == response_json['id']

def test_updade_task():
    if tasks:
        task_id = tasks[0]
        payload = {
            "completed": False,
            "title": "Novo titulo",
            "description":"Nova descricao"
        }
        response = requests.put(f"{BASE_URL}/tasks/{task_id}", json=payload)
