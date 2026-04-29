# config_project_template

This is a template of a configuration repository that is used with a specific simulation tool (or group of tools).

<!-- 
IMPORTANT NOTE: 

When using this template, update at least the following locations with the name of your package instead of 'config_project_template'. Files listed will have comments that guide you to what content to change.

Package Related Items (To Update Names)
- README.md (This file)
- src/config_project_template
  - Rename to your package name
- pyproject.toml
- src/config_project_template/__init__.py

Content Items:
- src/'package_name'/configs/*.toml
- src/'package_name'/support_data/*
  - When applicable 
  
-->

## Configuration Management

Refer to the [UASAL Configuration Management Summary](https://github.com/uasal/lab_documents/blob/main/computing/development_guide/configuration_management.md) for additionally details on how analysis, simulation tools, and configuration repositories are structured within the UASAL GitHub organization.

For Configuration FAQ's, also defer to the [UASAL Configuration Management Summary](https://github.com/uasal/lab_documents/blob/main/computing/development_guide/configuration_management.md) for more information.

## Dependencies

All UASAL config packages are dependent on [utils_config](https://github.com/uasal/utils_config) but will be automatically installed when installing this package.

## Installation

<!-- Verify this is correct when using this template / update if GitLab -->
ssh keys are required for the pip-based install. Verify you have ssh keys installed in GitHub, or check out this [ssh key tutorial](https://github.com/uasal/lab_documents/blob/main/ssh_key_tutorial.md)

If there is no intention of modifying any of the configuration files inside the repository and analyzing the results, you can simply pip install the package.

In the event that you wish to interact with the files in the package, which may be the case if proposing a change to the files via a Pull request, then it may be useful to install it as an editable package by adding a `-e` to the commands below.

### Pip-based install

<!-- Update pip install for your package -->
```sh
pip install git+ssh://git@github.com/uasal/config_project_template.git
```

### Installed via cloning

<!-- Update git clone cmd for your package -->
```sh
git clone git@github.com:uasal/config_project_template.git
cd config_project_template
pip install .
```

## Usage

Included in this repository is an [example notebook](notebooks/example.ipynb) of how an analysis would make use of this (and other) configuration repositories.
What is included in this readme is only a brief summary.

This package makes use of the ConfigLoader class (as *config_loader*) from utils_config via the `load_config_values` method, which accepts 'raw' 'parsed' or 'unitless' as an argument, returning a dictionary after parsing the 'configs' directory for .toml files

<!-- Update the code block for your package name -->
```python
import config_project_template
data = config_project_template.load_config_values()
print(data["observatory"]["pointing"]["jitter_rms"])
```

load_config_values() has a default argument of 'raw' or alternatively pass in one of the three viable arguments for how values should be presented: 
- `load_config_values('unitless')` -> 0.01
- `load_config_values('parsed')` -> {'value': 0.01, 'unit': 'arcsecond'}
- `load_config_values('raw')` -> 10e-3arcsecond

<!-- Update config_project_template with your package name -->
For importing data and keeping code consistent across installs, *config_project_template* will return the path to support_data with `get_data_path()`

<!-- Update config_project_template with your package name -->
```python
import config_project_template
data_path = config_project_template.get_data_path()
print(data_path)
```
