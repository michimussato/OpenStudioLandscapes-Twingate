from dagster import (
    Definitions,
    load_assets_from_modules,
)

import OpenStudioLandscapes.Twingate.assets
import OpenStudioLandscapes.Twingate.constants

assets = load_assets_from_modules(
    modules=[OpenStudioLandscapes.Twingate.assets],
)

constants = load_assets_from_modules(
    modules=[OpenStudioLandscapes.Twingate.constants],
)


defs = Definitions(
    assets=[
        *assets,
        *constants,
    ],
)
