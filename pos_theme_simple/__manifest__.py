# -*- coding: utf-8 -*-
# noinspection PyStatementEffect
{
    "name": "Simple POS Theme",
    "summary": "A simple POS theme",
    "description": """
        This is an Odoo 17.0 module that aims to make some small improvements on the
        UI of the Odoo 17.0 `point_of_sale` module. As if right now, the module consist
        of nothing fancy. However, it does make some noticeable changes to the general lay-out
        of the POS system. 

        Some of the changes include:
        - Lay-out of several screens have been mirrored;
        - Image visibility is improved for categories and products;
        - Simplistic 'class-based' dark mode.
    """,
    "author": "Kevin Koster",
    "website": "https://kevinkoster.nl",
    "category": "Theme",
    "version": "1.0.0",
    "depends": ["point_of_sale"],
    "assets": {
        "point_of_sale._assets_pos": [
            "/pos_theme_simple/static/src/**/*",
        ],
    },
    "application": True
}
