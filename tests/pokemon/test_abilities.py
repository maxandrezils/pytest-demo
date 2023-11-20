import json
import pytest
import requests

class TestPokemonAbilities:
    def setup_method(self):
        with open("./config.json") as f:
            config = json.load(f)
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
        response = requests.get(f"{self.base_url}{id_or_name}")
        response.status_code == status_code
        data = response.json()
        assert data["name"] == ability_name, "Incorrect ability name returned."
        assert data["is_main_series"] == is_main_series, "Incorrect status for is main series is returned."
        assert data["generation"]["name"] == generation, "Incorrect generation returned."
        assert data["effect_changes"][0]["effect_entries"][1]["effect"] == effect, "Incorrect ability effect is returned." 
