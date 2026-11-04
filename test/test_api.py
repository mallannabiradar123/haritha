import requests
def test_api():
    response=requests.get("https://jsonplaceholder.typicode.com/posts/1", timeout=10)
    assert response.status_code==200
    data=response.json()
    assert "id" in  data