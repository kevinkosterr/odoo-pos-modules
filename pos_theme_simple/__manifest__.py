# -*- coding: utf-8 -*-
# noinspection PyStatementEffect
{
    "name": "Simple POS Theme",
    "summary": "A simple POS theme",
    "description": """
        A simple POS theme that includes some tweaks to the POS UI.
    """,
    "author": "Kevin Koster",
    "website": "https://kevinkoster.nl",
    "category": "Customizations",
    "version": "0.1",
    "depends": ["point_of_sale"],
    "assets": {
        # "web.assets_backend": [
        # ],
        "point_of_sale._assets_pos": [
            "/pos_theme_simple/static/src/**/*",
        ],
    }
}
