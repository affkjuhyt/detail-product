module.exports = {
    extends: [
        "eslint:recommended",
        "plugin:vue/vue3-essential",
        "plugin:@typescript-eslint/recommended",
    ],
    overrides: [],
    parser: "vue-eslint-parser",
    parserOptions: {
        ecmaVersion: "latest",
        sourceType: "module",
        parser: {
            ts: "@typescript-eslint/parser",
            js: "@typescript-eslint/parser",
        },
    },
    plugins: ["vue", "@typescript-eslint"],
    rules: {
        "no-undef": "off",
        "vue/no-unused-components": "off",
        "@typescript-eslint/no-explicit-any": "off",
        "@typescript-eslint/ban-ts-comment": "off",
    },
};
