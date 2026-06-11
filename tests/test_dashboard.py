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
    client, auth_token
):

    response = client.get(
        "/dashboard/stats",
        headers={
            "Authorization":
            f"Bearer {auth_token}"
        }
    )

    assert response.status_code == 200

    assert "total_applications" in response.json()
    
