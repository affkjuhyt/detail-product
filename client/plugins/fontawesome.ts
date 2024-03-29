import { library, config } from '@fortawesome/fontawesome-svg-core';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import { faStar, faStarHalfStroke, faChevronDown, faChevronUp, faXmark } from '@fortawesome/free-solid-svg-icons';
import { faCheckCircle } from '@fortawesome/free-regular-svg-icons';

config.autoAddCss = false;

library.add(faStar, faStarHalfStroke, faChevronDown, faChevronUp, faXmark);

library.add(faCheckCircle);

export default defineNuxtPlugin((nuxtApp) => {
    nuxtApp.vueApp.component('font-awesome-icon', FontAwesomeIcon);
});
