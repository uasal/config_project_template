import config_project_template as config_package
import warnings

import logging

logger = logging.getLogger(__name__)


def verify(verify_cls, config_values, silent=False):
    """This routine is for verification of the values in the config file.
    It is only available if the package is installed in a dev mode.

    The routine is imported by the config_verify package
    and should not be called directly.

    Parameters
    ----------

    verify_cls: class
        Class that is constructed with the appropriate references
        (e.g. specs, budgets) using the config_verify package.
    """

    # Start with the common params
    k1 = "common_params"
    k2 = "Pupils"
    k3 = "aper_clear_OD"
    vals, full = verify_cls.get_spec("L3-0003")
    assert config_values[k1][k2][k3]["value"] == vals["id1"]["value"], (
        f"expected {config_values[k1][k2][k3]['value']}, got {vals['id1']['value']}"
    )
    assert config_values[k1][k2][k3]["unit"] == vals["id1"]["unit"], (
        f"expected {config_values[k1][k2][k3]['unit']}, got {vals['id1']['unit']}"
    )

    # note an issue here that may be a bug
    # detils are found at https://github.com/uasal/utils_config/issues/29
    k3 = "m1_psd_B"
    got = verify_cls.budgets["wavefront"]["M1_PSD_B"]
    assert config_values[k1][k2][k3] == verify_cls.budgets["wavefront"]["M1_PSD_B"], (
        f"expected {config_values[k1][k2][k3]}, got {got}"
    )

    # Now do astrophysics
    k1 = "astrophysics"
    k2 = "zodi"
    k3 = "mag"
    vals, full = verify_cls.get_spec("L3-0007")
    assert config_values[k1][k2][k3]["value"] == vals["id1"]["value"], (
        f"expected {config_values[k1][k2][k3]['value']}, got {vals['id1']['value']}"
    )
    assert config_values[k1][k2][k3]["unit"] == vals["id1"]["unit"], (
        f"expected {config_values[k1][k2][k3]['unit']}, got {vals['id1']['unit']}"
    )

    return True
