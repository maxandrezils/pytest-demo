import json
import pytest
import requests

from config import json_import

class TestPokemonAbilities:
    def setup_method(self):
        config = json_import.json_import("./config.json")
        self.url = config["BASE_URL"]
        self.version = config["VERSION"]
        self.base_url = f"{self.url}/{self.version}/ability/"

    @pytest.mark.parametrize(
        ("status_code", "id_or_name", "ability_name", "is_main_series", "generation", "effect"),
        [
            pytest.param(200, 1, "stench", True, "generation-iii", "Has no effect in battle.")
        ]
    )
    def test_get_ability_by_id_or_name(self,status_code, id_or_name, ability_name, is_main_series, generation, effect):
        """
        Tests that the PokeAPI returns a valid response when a numeric or string ability id is used as a parameter.
        """
        response = requests.get(f"{self.base_url}{id_or_name}")
        response.status_code == status_code
        self.validate_response(response.json(), ability_name, is_main_series, generation, effect)
        
    def validate_response(self, data, ability_name, is_main_series, generation, effect):
        """Used to assert the values returned in the json response when performing a get request on the ability endpoint

        Args:
            data (_type_): The response.json of the request
            ability_name (_type_): The name of the ability
            is_main_series (bool): Does the ability come from the anime or the game.
            generation (_type_): Which generation did the ability first occur in.
            effect (_type_): What is the effect of the ability.
        """
        assert data["name"] == ability_name, "Incorrect ability name returned."
        assert data["is_main_series"] == is_main_series, "Incorrect status for is main series is returned."
        assert data["generation"]["name"] == generation, "Incorrect generation returned."
        assert data["effect_changes"][0]["effect_entries"][1]["effect"] == effect, "Incorrect ability effect is returned." 
