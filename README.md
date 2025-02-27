# config_project_template
Example of a configuration repository that is used with a specific simulation tool (or group of tools).

The naming convention should be config_project_toolname. So a hypothetical example could be `config_hubble_acs`.

The directory structure is designed as follows:

- Configuration parameters that are common to all tools in the repository belong in the `common_params.toml` file. 
- A separate directory (should be named the same as the repo) is needed for python packaging (`config_project_template`).
- All tool configs must have an `_init.toml` file which contains the default set of parameters for that tool.
- Config files must contain both values and units. 
  - Units shall utilize the astropy format.
- Values without a unit will be marked as *unitless*.
- The origin of the values should be in a comment (for now).
- At this time, no other filenames should start with an `_`. This functionality is reserved for future feature implementation(s).
- Any added configuration file must contain the *full set* of available parameters and not just overrides for the defaults.

Configuration files may contain key valued pairs, but also utilize groupings. Such as:

```toml
OD_optic1 = '50e-3m'
[sim_settings]  # settings for simulation tool
npix = 4096 # number of pixels per frame
beamrad = 0.4 # fractional beam radius
```

## Configuration Management
Refer to the [UASAL Configuration Management Summary](https://github.com/uasal/lab_documents/blob/main/computing/development_guide/configuration_management.md) for additionally details on how analysis, simulation tools, and configuration repositories are structured within the UASAL GitHub organization.

For Configuration FAQ's, also defer to the [UASAL Configuration Management Summary](https://github.com/uasal/lab_documents/blob/main/computing/development_guide/configuration_management.md) for more information.

------------

<!-- This code uses ``pre-commit`` to check yaml file syntax, maintain ``black`` formatting, and check ``flake8`` compliance.
To enable this, run the following commands once (the first removes the previous pre-commit hook)::

    git config --unset-all core.hooksPath
    pre-commit install -->
