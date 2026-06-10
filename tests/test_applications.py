# Helper Function
def get_token(client):
    response = client.post(
        "/auth/login",
        data={
            "username": "test1@example.com",
            "password": "password123"
        }
    )

    return (
        response.json()["access_token"]
    )


# Create Application
def test_create_application(client):
    token = get_token(client)

    response = client.post(
        "/applications",
        headers={
            "Authorization":
            f"Bearer {token}"
        },
        json={
            "company_name": "Google",
            "job_title": "Backend Intern"
        }
    )

    assert response.status_code == 201


# Get Applications
def test_get_applications(client):
    token = get_token(client)

    response = client.get(
        "/applications",
        headers={
            "Authorization":
            f"Bearer {token}"
        }
    )

    assert response.status_code == 200
