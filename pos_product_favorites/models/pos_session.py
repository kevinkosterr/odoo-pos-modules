from odoo import models


class PosSession(models.Model):
    _inherit = "pos.session"

    def _loader_params_product_product(self):
        """
        Create search parameters for the `product.product` model.
        Extends functionality to include priority field. This determines whether a product is marked as favorite.
        """
        result = super()._loader_params_product_product()
        result['search_params']['fields'].extend(['priority'])
        return result
