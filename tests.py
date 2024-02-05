import json
from fastapi.testclient import TestClient
from main import app  # Replace 'your_main_module' with the actual module name where your FastAPI app is defined

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Message": "Welcome to the assignment"}

def test_fetch_wikipedia_summary():
    # Test with valid data
    query_data = {
        "title": "Python (programming language)",
        "count": 5
    }
    response = client.post("/wikipedia-count/", json=query_data)
    assert response.status_code == 200
    assert "title" in response.json()
    assert "count" in response.json()
    assert "result" in response.json()

    # Test with invalid data (missing 'title' field)
    invalid_query_data = {
        "count": 5
    }
    response = client.post("/wikipedia-count/", json=invalid_query_data)
    assert response.status_code == 422  # 422 Unprocessable Entity for validation error

def test_get_search_results():
    response = client.get("/search-results/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_fetch_wikipedia_summary_invalid_count():
    # Test case where 'count' is not a positive integer
    query_data = {
        "title": "Python (programming language)",
        "count": "invalid"
    }
    response = client.post("/wikipedia-count/", json=query_data)
    assert response.status_code == 422  # 422 Unprocessable Entity for validation error
