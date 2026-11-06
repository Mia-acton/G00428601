import pytest

def user_payload(
        equipment_id=1,
        sid="ST-MA4567",
        description= "Oscilloscope",
        priority=3,
        status="OPEN",
):
    return {
        "equipment_id": equipment_id,
        "student_id": sid,
        "description": description,
        "priority": priority,
        "status": status,
    }

def test_create_user_returns_201(client):
    response = client.post("/api/users", json=user_payload())
    assert response.status_code == 201
    data = response.json()
    assert data ["equipment_id"] == 1
    assert data ["student_id"] == "ST-MA4567"
    assert data ["description"] == "Oscilloscope"
    assert data ["priority"] == 3
    

def test_duplicate_user_returns_409(client):
    first_response = client.post("/api/users", json=user_payload())
    assert first_response.status_code == 201
    response = client.post("/api/users", json=user_payload())
    assert response.status_code == 409
    assert "already exists" in response.json()["detail"].lower()

@pytest.mark.parameterize(
    "bad_sid",
    [
        "BAD123",
        "dd-MA4567",
        "80-644567",
        "1r-64rt567",
    ],
)
def test_invalid_student_id_returns_422(client, bad_sid):
    response = client.post(
        "/api/users",
        json=user_payload(sid=bad_sid),
    )

    assert response.status_code == 422

def test_get_users(client):
    client.post("/api/users", json=user_payload())

    response = client.get("/api/users")

    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["student_id"] == "ST-MA4567"

def test_get_user_by_id(client):
    created = client.post(
        "/api/users",
        json=user_payload(),
    ).json()

    user_id = created["id"]
    response = client.get(f"/api/users/{user_id}")

    assert response.status_code == 200
    assert response.json()["description"] == "Oscilloscope"

def test_get_missing_user_returns_404(client):
    response = client.get("/api/users/999")

    assert response.status_code == 404
    assert "not found" in response.json()["detail"].lower()

def test_get_priority(client):
    response = client.get("/api/users/67")

    assert response.status_code == 422
    assert "invalid priority" in response.json()["detail"].lower()

def test_delete_user(client):
    created = client.post(
        "/api/users",
        json=user_payload(),
    ).json()

    user_id = created["id"]

    response = client.delete(f"/api/users/{user_id}")
    assert response.status_code == 404

def test_delete_missing_user_returns_404(client):
    response = client.delete("/api/users/999")

    assert response.status_code == 404


