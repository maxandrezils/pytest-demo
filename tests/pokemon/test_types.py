import json
import pytest
import requests


class TestPokemonTypes:
    def setup_method(self):
        with open("./config.json") as f:
            config = json.load(f)

        self.url = config["BASE_URL"]
        self.version = config["VERSION"]
        self.base_url = f"{self.url}/{self.version}/type"

    def test_get_pokemon_type_by_id(self):
        """
        Test that the PokéAPI endpoint for getting a type returns a successful response.
        """
        response = requests.get(f"{self.base_url}/1")
        assert response.status_code == 200, "Invalid request"

    @pytest.mark.parametrize("id_or_name", ["fire", 1])
    def test_get_type_with_parameters(self, id_or_name):
        """
        Test that the PokéAPI endpoint for getting a type can be used with parameters.
        Args:
        id_or_name: The ID or name of the type to get.
        """
        response = requests.get(f"{self.base_url}/{id_or_name}")
        assert response.status_code == 200, "Invalid request"
