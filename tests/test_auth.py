# Register User Test
def test_register_user(client):
    response = client.post(
        "/auth/register",
        json={
            "username": "testuser",
            "email": "test1@example.com",
            "password": "password123"
        }
    )

    assert response.status_code == 201

    data = response.json()

    assert data["email"] == (
        "test1@example.com"
    )
    
    

# Login Test
def test_login_user(client):
    # Register first so the user exists in this test's clean DB
    client.post(
        "/auth/register",
        json={
            "username": "testuser",
            "email": "test1@example.com",
            "password": "password123"
        }
    )

    response = client.post(
        "/auth/login",
        data={
            "username": "test1@example.com",
            "password": "password123"
        }
    )

    assert response.status_code == 200

    assert "access_token" in response.json()

# Invalid Login Test
def test_invalid_login(client):
    response = client.post(
        "/auth/login",
        data={
            "username": "wrong@example.com",
            "password": "wrongpass"
        }
    )

    assert response.status_code == 401
