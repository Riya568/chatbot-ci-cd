def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"My Chatbot" in response.data


def test_chat_hello(client):
    response = client.post(
        "/chat",
        json={"message": "hello"}
    )
    data = response.get_json()
    assert response.status_code == 200
    assert "Hello" in data["reply"]


def test_chat_unknown(client):
    response = client.post(
        "/chat",
        json={"message": "random text"}
    )
    data = response.get_json()
    assert response.status_code == 200
    assert "Sorry" in data["reply"]
