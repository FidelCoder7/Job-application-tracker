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


# Dashboard Protected
def test_dashboard_requires_auth(
    client
):
    response = client.get(
        "/dashboard/stats"
    )

    assert response.status_code == 401


# Dashboard Works
def test_dashboard_stats(
    client
):
    token = get_token(client)

    response = client.get(
        "/dashboard/stats",
        headers={
            "Authorization":
            f"Bearer {token}"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert (
        "total_applications"
        in data
    )
