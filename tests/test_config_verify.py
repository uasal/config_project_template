import config_project_template as config_package
import pytest

import logging

logger = logging.getLogger(__name__)


def test_config_verify(recwarn):
    """Tests config_verify template. Utilizes a mock for the class provided by the config_verify package."""

    # build a class that mocks the functionality of what would be created
    # by config verify
    class ConfigVerify_mock:
        def __init__(self):
            self.specs = {
                "L3": [
                    {
                        "id": "L3-0003",
                        "definition": "The pupil shall have an outer diameter of $id1.",
                        "vals": {"id1": {"value": 5, "unit": "m"}},
                    },
                    {
                        "id": "L3-0007",
                        "definition": "The zodi magnitude shall less than $id1 $id1_units.",
                        "vals": {"id1": {"value": 22.5, "unit": "mag"}},
                    },
                ]
            }
            self.budgets = {"wavefront": {"M1_RMS": 12.0e-3, "M1_PSD_B": 3.0}}

        def get_spec(self, id):
            """Simulates performance of get_specs.py

            Returns:

            [parameters], full_spec
            """
            if id == "L3-0003":
                return (
                    self.specs["L3"][0]["vals"],
                    self.specs["L3"][0],
                )
            elif id == "L3-0007":
                return (
                    self.specs["L3"][1]["vals"],
                    self.specs["L3"][1],
                )
            else:
                raise ValueError("No associated ID.")

    # Configure the return value of the methods on instances
    # created from the mocked class
    verify_cls_mock = ConfigVerify_mock()

    # load the configuration
    config_values = config_package.load_config_values("parsed")

    # with pytest.warns(None) as record:
    success = config_package.config_verify.verify(verify_cls_mock, config_values)
    assert success

    # Should get X warnings
    # assert len(record) == 3
    # assert len(recwarn.list) == 3
