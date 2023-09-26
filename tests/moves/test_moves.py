import pytest
import requests


class TestPokemonMoves:
    def setup_method(self):
        self.base_url = "https://pokeapi.co/api/v2/move/"

    def test_get_move_by_id(self):
        """
        Tests that the PokéAPI endpoint for getting a move by ID returns a successful response with the correct data.

        Args:
            self: The test instance.
        """
        response = requests.get(f"{self.base_url}/1")
        assert response.status_code == 200
        data = response.json()
        assert data["name"] == "pound"

    # TODO: add the following scenarios
    # - move by name
    # - move schema
    # -
