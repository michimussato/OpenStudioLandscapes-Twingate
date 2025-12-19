import os
import pathlib

from dagster import get_dagster_logger, EnvVar
from pydantic import (
    Field,
    PositiveInt,
)

LOGGER = get_dagster_logger(__name__)

from OpenStudioLandscapes.engine.config.models import FeatureBaseModel

from OpenStudioLandscapes.Twingate import dist

config_default = pathlib.Path(__file__).parent.joinpath("config_default.yml")
CONFIG_STR = config_default.read_text()


class Config(FeatureBaseModel):
    feature_name: str = dist.name

    definitions: str = "OpenStudioLandscapes.Twingate.definitions"

    enabled: bool = False

    docker_image: str = Field(
        default="docker.io/twingate/connector:latest",
    )

    TWINGATE_LABEL_DEPLOYED_BY: str = Field(
        default="docker",
    )

    TWINGATE_NETWORK: str = Field(
        default=os.environ.get("OPENSTUDIOLANDSCAPES_TWINGATE__TWINGATE_NETWORK", ""),
        frozen=False,
        description="Set this value in `.env` (`OPENSTUDIOLANDSCAPES_TWINGATE__TWINGATE_NETWORK`)."
    )

    TWINGATE_ACCESS_TOKEN: str = Field(
        default=os.environ.get("OPENSTUDIOLANDSCAPES_TWINGATE__TWINGATE_ACCESS_TOKEN", ""),
        frozen=False,
        description="Set this value in `.env` (`OPENSTUDIOLANDSCAPES_TWINGATE__TWINGATE_ACCESS_TOKEN`)."
    )

    TWINGATE_REFRESH_TOKEN: str = Field(
        default=os.environ.get("OPENSTUDIOLANDSCAPES_TWINGATE__TWINGATE_REFRESH_TOKEN", ""),
        frozen=False,
        description="Set this value in `.env` (`OPENSTUDIOLANDSCAPES_TWINGATE__TWINGATE_REFRESH_TOKEN`)."
    )

    TWINGATE_LOG_ANALYTICS: str = Field(
        default="v2",
        frozen=False,
    )

    TWINGATE_LOG_LEVEL: PositiveInt = Field(
        default=3,
        frozen=False,
    )
