import json
import pytest
import requests
import time
from jsonschema import validate


class TestMoveAilments:
    def setup_method(self):
        self.base_url = "https://pokeapi.co/api/v2/move-ailment/"
        with open("./schemas/move_ailment_schema", "r") as f:
            self.json_schema = json.load(f)


# TODO:
# - Add scenarios for id and move aliment name
# - Add scenario for schema validation
# - Add scenario for contract  tests
