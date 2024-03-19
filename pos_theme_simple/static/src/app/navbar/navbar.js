/** @odoo-module */

import { Navbar } from "@point_of_sale/app/navbar/navbar";
import { patch } from "@web/core/utils/patch";

patch(Navbar.prototype, {

    /**
     * Handle the clicks from the dark mode button. Actual toggling of the functionality happens in the
     * PosStore class.
     */
    onDarkModeButtonClick() {
        this.pos.toggleDarkMode();
    }

})
