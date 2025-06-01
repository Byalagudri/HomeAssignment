import pytest

from lib import get_cad_api_data

@pytest.mark.smoke
def test_cad_api_response_status():
    response = get_cad_api_data()
    assert response.status_code == 200

@pytest.mark.smoke
def test_cad_api_contains_expected_fields():
    response = get_cad_api_data()
    json_data = response.json()
    assert "signature" in json_data
    assert "fields" in json_data
    assert isinstance(json_data["fields"], list) and len(json_data["fields"]) > 0
