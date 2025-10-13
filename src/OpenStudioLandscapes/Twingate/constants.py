__all__ = [
    "DOCKER_USE_CACHE",
    "ASSET_HEADER",
    "FEATURE_CONFIGS",
]

import pathlib
from typing import Any, Generator, MutableMapping

from dagster import (
    AssetExecutionContext,
    AssetMaterialization,
    AssetOut,
    MetadataValue,
    Output,
    get_dagster_logger,
    multi_asset,
)

LOGGER = get_dagster_logger(__name__)

from OpenStudioLandscapes.engine.constants import DOCKER_USE_CACHE_GLOBAL
from OpenStudioLandscapes.engine.enums import OpenStudioLandscapesConfig

DOCKER_USE_CACHE = DOCKER_USE_CACHE_GLOBAL or False


GROUP = "Twingate"
KEY = [GROUP]
FEATURE = f"OpenStudioLandscapes-{GROUP}".replace("_", "-")

ASSET_HEADER = {
    "group_name": GROUP,
    "key_prefix": KEY,
}

# @formatter:off
FEATURE_CONFIGS = {
    OpenStudioLandscapesConfig.DEFAULT: {
        "DOCKER_USE_CACHE": DOCKER_USE_CACHE,
        "HOSTNAME": "twingate",
        "TWINGATE_PORT_HOST": "80",  # Todo: this is a placeholder because we don't have a port mapping here yet.
        "TELEPORT_ENTRY_POINT_HOST": "{{HOSTNAME}}",  # Either a hardcoded str or a ref to a Variable (with double {{ }}!)
        "TELEPORT_ENTRY_POINT_PORT": "{{TWINGATE_PORT_HOST}}",  # Either a hardcoded str or a ref to a Variable (with double {{ }}!)
        "TWINGATE_LABEL_DEPLOYED_BY": "docker",
        # https://www.twingate.com/docs/deploy-connector-with-docker-compose
        # Mandatory
        "TWINGATE_NETWORK": "[Secret - managed via .env (mandatory)]",
        "TWINGATE_ACCESS_TOKEN": "[Secret - managed via .env (mandatory)]",
        "TWINGATE_REFRESH_TOKEN": "[Secret - managed via .env (mandatory)]",
        # Optional
        "TWINGATE_LOG_ANALYTICS": "v2",
        # https://help.twingate.com/hc/en-us/articles/4901034540189-Twingate-Connector-Logs
        "TWINGATE_LOG_LEVEL": "3",
    }
}
# @formatter:on


# Todo:
#  - [ ] move to common_assets
@multi_asset(
    name=f"constants_{ASSET_HEADER['group_name']}",
    outs={
        "NAME": AssetOut(
            **ASSET_HEADER,
            dagster_type=str,
            description="",
        ),
        "FEATURE_CONFIGS": AssetOut(
            **ASSET_HEADER,
            dagster_type=dict,
            description="",
        ),
        "DOCKER_COMPOSE": AssetOut(
            **ASSET_HEADER,
            dagster_type=pathlib.Path,
            description="",
        ),
    },
)
def constants_multi_asset(
    context: AssetExecutionContext,
) -> Generator[
    Output[dict[OpenStudioLandscapesConfig, dict[str | Any, bool | str | Any]]]
    | AssetMaterialization
    | Output[Any]
    | Output[pathlib.Path]
    | Any,
    None,
    None,
]:
    """ """

    yield Output(
        output_name="FEATURE_CONFIGS",
        value=FEATURE_CONFIGS,
    )

    yield AssetMaterialization(
        asset_key=context.asset_key_for_output("FEATURE_CONFIGS"),
        metadata={
            "__".join(
                context.asset_key_for_output("FEATURE_CONFIGS").path
            ): MetadataValue.json(FEATURE_CONFIGS),
        },
    )

    yield Output(
        output_name="NAME",
        value=__name__,
    )

    yield AssetMaterialization(
        asset_key=context.asset_key_for_output("NAME"),
        metadata={
            "__".join(context.asset_key_for_output("NAME").path): MetadataValue.path(
                __name__
            ),
        },
    )

    docker_compose = pathlib.Path(
        "{DOT_LANDSCAPES}",
        "{LANDSCAPE}",
        f"{ASSET_HEADER['group_name']}__{'_'.join(ASSET_HEADER['key_prefix'])}",
        "__".join(context.asset_key_for_output("DOCKER_COMPOSE").path),
        "docker_compose",
        "docker-compose.yml",
    )

    yield Output(
        output_name="DOCKER_COMPOSE",
        value=docker_compose,
    )

    yield AssetMaterialization(
        asset_key=context.asset_key_for_output("DOCKER_COMPOSE"),
        metadata={
            "__".join(
                context.asset_key_for_output("DOCKER_COMPOSE").path
            ): MetadataValue.path(docker_compose),
        },
    )
