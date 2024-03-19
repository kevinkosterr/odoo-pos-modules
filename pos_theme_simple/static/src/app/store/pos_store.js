/** @odoo-module */

import { PosStore } from "@point_of_sale/app/store/pos_store";
import { patch } from "@web/core/utils/patch";

patch(PosStore.prototype, {

     async setup(env, { popup, orm, number_buffer, hardware_proxy, barcode_reader, ui }) {
        await super.setup(...arguments);
         /** Originally I wanted to use `useState` here and make it localStorage reactive.
          * however, it will throw an error saying I can only use useState in the setup function?  */
        this.darkMode = JSON.parse(localStorage.getItem('darkMode') || 'false');
        if (this.darkMode) $("body.pos").addClass('dark');
    },

    /**
     * Toggle between light and dark mode.
     */
    toggleDarkMode() {
        $("body.pos").toggleClass('dark');
        localStorage.setItem('darkMode', JSON.stringify(!this.darkMode));
        this.darkMode = !this.darkMode;
    },

    /**
     * Get the current state of dark mode.
     * @return {boolean}
     */
    darkModeEnabled() {
         return this.darkMode;
    }

});
