import json
import pytest
import requests
import time
from jsonschema import validate

from config import json_import


class TestPokemonMoves:
    def setup_method(self):
        config = json_import.json_import("./config.json")
        self.url = config["BASE_URL"]
        self.version = config["VERSION"]
        self.base_url = f"{self.url}/{self.version}/move/"
        self.json_schema = json_import.json_import("./schemas/move_schema.json")


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
        """
        response = requests.get(f"{self.base_url}{id_or_name}")
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
        response = requests.get(f"{self.base_url}{id_or_move_name}")
        data = response.json()
        validate(data, self.json_schema)

    @pytest.mark.parametrize(
        ("id_or_name", "message", "status_code"),
        [
            pytest.param(-1, "Not Found", 404, id="Negative id returns a 404"),
            pytest.param(
                9999,
                "Not Found",
                404,
                id="Id that exceeds number of moves returns a 404",
            ),
            pytest.param(
                "Invalidmove",
                "Not Found",
                404,
                id="Move that doesn't exist returns a 404",
            ),
        ],
    )
    def test_get_move_validation(self, id_or_name, message, status_code):
        """
        Test the validation on the moves endpoint
        """
        response = requests.get(f"{self.base_url}{id_or_name}")
        assert response.status_code == status_code
        assert response.text == message

    def test_get_move_performance(self):
        """
        Test that the moves endpoint responds in less than a second
        """
        start_time = time.time()
        response = requests.get(f"{self.base_url}1")
        end_time = time.time()
        response_time = end_time - start_time
        assert response_time < 1.0
