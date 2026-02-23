import pytest

# Arrange-Act-Assert pattern for FastAPI endpoints
def test_root_endpoint(client):
    # Arrange: (nothing to arrange for root)
    # Act
    response = client.get("/")
    # Assert
    assert response.status_code == 200
    assert "Mergington" in response.text

def test_activities_list(client):
    # Arrange: (nothing to arrange)
    # Act
    response = client.get("/activities")
    # Assert
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

# Add more tests for signup, unregister, and edge cases as endpoints are implemented
