from pathlib import Path
import unittest
import tomlkit
from config_stp import tests
import astropy

CONFIGS_PATH = Path(config_project_template.__file__).parent / "configs"

class TestConfigs(TestCase):
    "Tests for psd_utils."

    def test_tomls(self):
        # Go and read in each config file and check for syntax errors
        files = *.toml
        tests.syntax(files)
        # Also check astropy unit compatibility
        tests.astropy_units(files)
        pass


    