import json
import pytest
import requests
from jsonschema import validate


class TestPokemonMoves:
    def setup_method(self):
        self.base_url = "https://pokeapi.co/api/v2/move/"
        with open("./schemas/move_schema.json", "r") as f:
            self.json_schema = json.load(f)

    @pytest.mark.parametrize(
        ("id_or_name", "move_name", "accuracy", "power", "pp", "type"),
        [
            pytest.param(
                1,
                "pound",
                100,
                40,
                35,
                "normal",
                id="Using the move id returns its details",
            ),
            pytest.param(
                "karate-chop",
                "karate-chop",
                100,
                50,
                25,
                "fighting",
                id="Using the move name returns its values",
            ),
        ],
    )
    def test_get_move_by_id_or_name(
        self, id_or_name, move_name, accuracy, power, pp, type
    ):
        """
        Tests that the PokéAPI endpoint for getting a move by ID returns a successful response with the correct data.
        - correct move name is returned
        - correct accuracy is returned
        - correct damage class is returned
        - correct power is returned
        - correct pp is returned
        - correct type is returned
        """
        response = requests.get(f"{self.base_url}/{id_or_name}")
        assert response.status_code == 200
        data = response.json()
        assert data["name"] == move_name
        assert data["accuracy"] == accuracy
        assert data["power"] == power
        assert data["pp"] == pp
        assert data["type"]["name"] == type

    @pytest.mark.parametrize(
        "id_or_move_name",
        [
            pytest.param(1, id="Returns a valid schema when using a move id"),
            pytest.param("pound", id="Returns a valid schema when using a move name"),
        ],
    )
    def test_validate_move_response_with_schema(self, id_or_move_name):
        """
        Tests that the JSON response from the PokéAPI endpoint for getting a move by ID validates against the saved schema file.
        """
        response = requests.get(f"{self.base_url}/{id_or_move_name}")
        data = response.json()
        validate(data, self.json_schema)

    def test_get_move_validation(self):
