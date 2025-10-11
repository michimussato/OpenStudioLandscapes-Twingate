[![ Logo OpenStudioLandscapes ](https://github.com/michimussato/OpenStudioLandscapes/raw/main/media/images/logo128.png)](https://github.com/michimussato/OpenStudioLandscapes)

***

1. [Feature: OpenStudioLandscapes-Twingate](#feature-openstudiolandscapes-twingate)
   1. [Brief](#brief)
   2. [Requirements](#requirements)
   3. [Install](#install)
      1. [This Feature](#this-feature)
   4. [Add to OpenStudioLandscapes](#add-to-openstudiolandscapes)
   5. [Testing](#testing)
      1. [pre-commit](#pre-commit)
      2. [nox](#nox)
   6. [Variables](#variables)
      1. [Feature Configs](#feature-configs)
2. [Community](#community)
3. [Official Resources](#official-resources)
   1. [Twingate Connector](#twingate-connector)
      1. [Twingate Connector Setup](#twingate-connector-setup)

***

This `README.md` was dynamically created with [OpenStudioLandscapesUtil-ReadmeGenerator](https://github.com/michimussato/OpenStudioLandscapesUtil-ReadmeGenerator).

***

# Feature: OpenStudioLandscapes-Twingate

## Brief

This is an extension to the OpenStudioLandscapes ecosystem. The full documentation of OpenStudioLandscapes is available [here](https://github.com/michimussato/OpenStudioLandscapes).

You feel like writing your own Feature? Go and check out the [OpenStudioLandscapes-Template](https://github.com/michimussato/OpenStudioLandscapes-Template).

## Requirements

- `python-3.11`
- `OpenStudioLandscapes`

## Install

### This Feature

Clone this repository into `OpenStudioLandscapes/.features`:

```shell
# cd .features
git clone https://github.com/michimussato/OpenStudioLandscapes-Twingate.git
```

Create `venv`:

```shell
# cd .features/OpenStudioLandscapes-Twingate
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip setuptools
```

Configure `venv`:

```shell
# cd .features/OpenStudioLandscapes-Twingate
pip install -e "../../[dev]"
pip install -e ".[dev]"
```

For more info see [VCS Support of pip](https://pip.pypa.io/en/stable/topics/vcs-support/).

## Add to OpenStudioLandscapes

Add the following code to `OpenStudioLandscapes.engine.features.FEATURES`:

```python
FEATURES.update(
    "OpenStudioLandscapes-Twingate": {
        "enabled": True|False,
        # - from ENVIRONMENT VARIABLE (.env):
        #   "enabled": get_bool_env("ENV_VAR")
        # - combined:
        #   "enabled": True|False or get_bool_env(
        #       "OPENSTUDIOLANDSCAPES__ENABLE_FEATURE_OPENSTUDIOLANDSCAPES_TWINGATE"
        #   )
        "module": "OpenStudioLandscapes.Twingate.definitions",
        "compose_scope": ComposeScope.DEFAULT,
        "feature_config": OpenStudioLandscapesConfig.DEFAULT,
    }
)
```

## Testing

### pre-commit

- https://pre-commit.com
- https://pre-commit.com/hooks.html

```shell
pre-commit install
```

### nox

#### Generate Report

```shell
nox --no-error-on-missing-interpreters --report .nox/nox-report.json
```

#### Re-Generate this README

```shell
nox -v --add-timestamp --session readme
```

#### Generate Sphinx Documentation

```shell
nox -v --add-timestamp --session docs
```

#### pylint

```shell
nox -v --add-timestamp --session lint
```

##### pylint: disable=redefined-outer-name

- [`W0621`](https://pylint.pycqa.org/en/latest/user_guide/messages/warning/redefined-outer-name.html): Due to Dagsters way of piping arguments into assets.

#### SBOM

Acronym for Software Bill of Materials

```shell
nox -v --add-timestamp --session sbom
```

We create the following SBOMs:

- [`cyclonedx-bom`](https://pypi.org/project/cyclonedx-bom/)
- [`pipdeptree`](https://pypi.org/project/pipdeptree/) (Dot)
- [`pipdeptree`](https://pypi.org/project/pipdeptree/) (Mermaid)

SBOMs for the different Python interpreters defined in [`.noxfile.VERSIONS`](https://github.com/michimussato/OpenStudioLandscapes-Twingate/tree/main/noxfile.py) will be created in the [`.sbom`](https://github.com/michimussato/OpenStudioLandscapes-Twingate/tree/main/.sbom) directory of this repository.

- `cyclone-dx`
- `pipdeptree` (Dot)
- `pipdeptree` (Mermaid)

Currently, the following Python interpreters are enabled for testing:

- `python3.11`

## Variables

The following variables are being declared in `OpenStudioLandscapes.Twingate.constants` and are accessible throughout the [`OpenStudioLandscapes-Twingate`](https://github.com/michimussato/OpenStudioLandscapes-Twingate/tree/main/src/OpenStudioLandscapes/Twingate/constants.py) package.

| Variable           | Type   |
| :----------------- | :----- |
| `DOCKER_USE_CACHE` | `bool` |
| `ASSET_HEADER`     | `dict` |
| `FEATURE_CONFIGS`  | `dict` |

### Feature Configs

#### Feature Config: default

| Variable                     | Type   | Value                                     |
| :--------------------------- | :----- | :---------------------------------------- |
| `DOCKER_USE_CACHE`           | `bool` | `False`                                   |
| `HOSTNAME`                   | `str`  | `twingate`                                |
| `TELEPORT_ENTRY_POINT_HOST`  | `str`  | `{{HOSTNAME}}`                            |
| `TELEPORT_ENTRY_POINT_PORT`  | `str`  | `{{DAGSTER_DEV_PORT_HOST}}`               |
| `TWINGATE_LABEL_DEPLOYED_BY` | `str`  | `docker`                                  |
| `TWINGATE_NETWORK`           | `str`  | `[Secret - managed via .env (mandatory)]` |
| `TWINGATE_ACCESS_TOKEN`      | `str`  | `[Secret - managed via .env (mandatory)]` |
| `TWINGATE_REFRESH_TOKEN`     | `str`  | `[Secret - managed via .env (mandatory)]` |
| `TWINGATE_LOG_ANALYTICS`     | `str`  | `v2`                                      |
| `TWINGATE_LOG_LEVEL`         | `str`  | `3`                                       |

# Community

| Feature                             | GitHub                                                                                                                                     | Discord                                                                |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------- |
| OpenStudioLandscapes                | [https://github.com/michimussato/OpenStudioLandscapes](https://github.com/michimussato/OpenStudioLandscapes)                               | [# openstudiolandscapes-general](https://discord.gg/F6bDRWsHac)        |
| OpenStudioLandscapes-Ayon           | [https://github.com/michimussato/OpenStudioLandscapes-Ayon](https://github.com/michimussato/OpenStudioLandscapes-Ayon)                     | [# openstudiolandscapes-ayon](https://discord.gg/gd6etWAF3v)           |
| OpenStudioLandscapes-Dagster        | [https://github.com/michimussato/OpenStudioLandscapes-Dagster](https://github.com/michimussato/OpenStudioLandscapes-Dagster)               | [# openstudiolandscapes-dagster](https://discord.gg/jwB3DwmKvs)        |
| OpenStudioLandscapes-Kitsu          | [https://github.com/michimussato/OpenStudioLandscapes-Kitsu](https://github.com/michimussato/OpenStudioLandscapes-Kitsu)                   | [# openstudiolandscapes-kitsu](https://discord.gg/6cc6mkReJ7)          |
| OpenStudioLandscapes-RustDeskServer | [https://github.com/michimussato/OpenStudioLandscapes-RustDeskServer](https://github.com/michimussato/OpenStudioLandscapes-RustDeskServer) | [# openstudiolandscapes-rustdeskserver](https://discord.gg/nJ8Ffd2xY3) |
| OpenStudioLandscapes-Template       | [https://github.com/michimussato/OpenStudioLandscapes-Template](https://github.com/michimussato/OpenStudioLandscapes-Template)             | [# openstudiolandscapes-template](https://discord.gg/J59GYp3Wpy)       |
| OpenStudioLandscapes-Twingate       | [https://github.com/michimussato/OpenStudioLandscapes-Twingate](https://github.com/michimussato/OpenStudioLandscapes-Twingate)             | [# openstudiolandscapes-twingate](https://discord.gg/tREYa6UNJf)       |

To follow up on the previous LinkedIn publications, visit:

- [OpenStudioLandscapes on LinkedIn](https://www.linkedin.com/company/106731439/).
- [Search for tag #OpenStudioLandscapes on LinkedIn](https://www.linkedin.com/search/results/all/?keywords=%23openstudiolandscapes).

***

# Official Resources

[![ Logo Twingate ](https://help.twingate.com/hc/theming_assets/01HZKY9WB60MKN9FS7R4KP0J80.png)](https://www.twingate.com/)

## Twingate Connector

Twingate Information:

- [Github](https://github.com/Twingate-Labs)
- [Twingate on Docker Hub](https://hub.docker.com/u/twingate)
- [Twingate Connector (Docker Hub)](https://hub.docker.com/r/twingate/connector)
- [How to deploy a Connector](https://www.twingate.com/docs/quick-start#deploy-a-connector)
- [Documentation](https://www.twingate.com/docs/)
- [Twingate API](https://www.twingate.com/docs/api-overview)
- [Deploy Docker Compose](https://www.twingate.com/docs/deploy-connector-with-docker-compose)
- [Documentation](https://rustdesk.com/docs/en/self-host/rustdesk-server-oss/docker/)
- [Tutorial/Overview (Network Chuck)](https://www.youtube.com/watch?v=IYmXPF3XUwo&ab_channel=NetworkChuck)

### Twingate Connector Setup

#### Sign Up

- [https://auth.twingate.com/signup-v2](https://auth.twingate.com/signup-v2)

#### Add Remote Network

- [https://openstudiolandscapes.twingate.com/networks](https://openstudiolandscapes.twingate.com/networks)

1. On Premise
2. Set Remote Network name
3. Add Remote Network name to `.env` (`OPENSTUDIOLANDSCAPES_TWINGATE__TWINGATE_NETWORK`)

#### Add Connector

For redundancy, Twingate sets up two Connectors. We'll continue with one for now.

- [https://openstudiolandscapes.twingate.com/connectors](https://openstudiolandscapes.twingate.com/connectors)

1. Docker
2. Generate New Tokens
3. Add Access Token to `.env` (`OPENSTUDIOLANDSCAPES_TWINGATE__TWINGATE_ACCESS_TOKEN`)
4. Add Refresh Token to `.env` (`OPENSTUDIOLANDSCAPES_TWINGATE__TWINGATE_REFRESH_TOKEN`)

![Not yet connected ](media/images/not_yet_connected.png)

#### Create and Launch Landscape (OpenStudioLandscapes-Twingate)

```generic
[...]
twingate--2025-09-09-09-50-23-9369549baddf4d81b9e37d9fed4ca5ce  | State: Offline
twingate--2025-09-09-09-50-23-9369549baddf4d81b9e37d9fed4ca5ce  | State: Authentication
twingate--2025-09-09-09-50-23-9369549baddf4d81b9e37d9fed4ca5ce  | State: Authentication
twingate--2025-09-09-09-50-23-9369549baddf4d81b9e37d9fed4ca5ce  | State: Online
[...]            
```

![Connected ](media/images/connected.png)