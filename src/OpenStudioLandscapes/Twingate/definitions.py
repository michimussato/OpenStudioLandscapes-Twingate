from dagster import (
    Definitions,
    load_assets_from_modules,
)

import OpenStudioLandscapes.Twingate.assets

assets = load_assets_from_modules(
    modules=[OpenStudioLandscapes.Twingate.assets],
)


defs = Definitions(
    assets=[
        *assets,
    ],
)
