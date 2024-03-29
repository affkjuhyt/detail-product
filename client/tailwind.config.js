/** @type {import('tailwindcss').Config} */

module.exports = {
    corePlugins: {
        preflight: true,
    },
    content: [
        './components/**/*.{js,vue,ts}',
        './layouts/**/*.vue',
        './pages/**/*.vue',
        './views/**/*.vue',
        './plugins/**/*.{js,ts}',
        './nuxt.config.{js,ts}',
        './app.vue',
    ],
    important: true,
    theme: {
        screens: {
            sm: '600px',
            md: '905px',
            lg: '1240px',
            xl: '1440px',
            '2xl': '1600px',
        },
        extend: {
            colors: {
                'primary-400': '#cd7740', // rgb(205, 119, 64)
                'primary-500': '#ff7227', //rgb(255, 114, 39)
                'primary-600': '#ea4c11', // rgb(234, 76, 17)
                'primary-700': '#c74110', // rgb(199, 65, 16)
                'blue-btn': '#1b5af2', // rgb(27, 90, 242)
            },
        },
        container: {
            center: true,
        },
    },
    plugins: [],
};
