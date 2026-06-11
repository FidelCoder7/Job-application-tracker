# Create Application
def test_create_application(client, auth_token):

    response = client.post(
        "/applications",
        headers={
            "Authorization":
            f"Bearer {auth_token}"
        },
        json={
            "company_name": "Google",
            "job_title": "Backend Intern"
        }
    )

    assert response.status_code == 201


# Get Applications
def test_get_applications(client, auth_token):

    response = client.get(
        "/applications",
        headers={
            "Authorization":
            f"Bearer {auth_token}"
        }
    )

    assert response.status_code == 200
