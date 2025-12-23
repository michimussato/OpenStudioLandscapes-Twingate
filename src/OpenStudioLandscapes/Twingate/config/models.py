import os
import pathlib

from dagster import get_dagster_logger
from pydantic import (
    Field,
    PositiveInt,
)

LOGGER = get_dagster_logger(__name__)

from OpenStudioLandscapes.engine.config.str_gen import get_config_str
from OpenStudioLandscapes.engine.config.models import FeatureBaseModel

from OpenStudioLandscapes.Twingate import dist

config_default = pathlib.Path(__file__).parent.joinpath("config_default.yml")


class Config(FeatureBaseModel):
    feature_name: str = dist.name

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
        description="Set this value in `.env` (`OPENSTUDIOLANDSCAPES_TWINGATE__TWINGATE_NETWORK`).",
    )

    TWINGATE_ACCESS_TOKEN: str = Field(
        default=os.environ.get(
            "OPENSTUDIOLANDSCAPES_TWINGATE__TWINGATE_ACCESS_TOKEN", ""
        ),
        frozen=False,
        description="Set this value in `.env` (`OPENSTUDIOLANDSCAPES_TWINGATE__TWINGATE_ACCESS_TOKEN`).",
    )

    TWINGATE_REFRESH_TOKEN: str = Field(
        default=os.environ.get(
            "OPENSTUDIOLANDSCAPES_TWINGATE__TWINGATE_REFRESH_TOKEN", ""
        ),
        frozen=False,
        description="Set this value in `.env` (`OPENSTUDIOLANDSCAPES_TWINGATE__TWINGATE_REFRESH_TOKEN`).",
    )

    TWINGATE_LOG_ANALYTICS: str = Field(
        default="v2",
        frozen=False,
    )

    TWINGATE_LOG_LEVEL: PositiveInt = Field(
        default=3,
        frozen=False,
    )


CONFIG_STR = get_config_str(
    Config=Config,
)

