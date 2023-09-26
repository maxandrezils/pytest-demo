import pytest
import requests


class TestPokemonMoves:
    def setup_method(self):
        self.base_url = "https://pokeapi.co/api/v2/move/"

    def test_get_move_by_id(self):
        """ """
        response = requests.get(f"{self.base_url}/1")
        assert response.status_code == 200
        data = response.json()
        assert data["name"] == "pound"
