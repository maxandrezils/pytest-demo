import json
import pytest
import requests
from jsonschema import validate


class TestPokemonMoves:
    def setup_method(self):
        self.base_url = "https://pokeapi.co/api/v2/move/"
        with open("./schemas/move_schema.json", "r") as f:
            self.json_schema = json.load(f)

    @pytest.mark.parametrize(("id_or_name", "move_name"), [(1, "pound")])
    def test_get_move_by_id_or_name(self, id_or_name, move_name):
        """
        Tests that the PokéAPI endpoint for getting a move by ID returns a successful response with the correct data.
        """
        response = requests.get(f"{self.base_url}/{id_or_name}")
        assert response.status_code == 200
        data = response.json()
        assert data["name"] == move_name

    def test_validate_move_response_with_schema(self):
        """
        Tests that the JSON response from the PokéAPI endpoint for getting a move by ID validates against the saved schema file.
        """
        response = requests.get(f"{self.base_url}/1")
        data = response.json()
        validate(data, self.json_schema)

    # TODO: add the following scenarios
    # - move by name
    # - move schema
    # -
