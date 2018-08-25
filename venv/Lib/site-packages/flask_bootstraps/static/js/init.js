requirejs.config({
    baseUrl: "/static/bootstrap/js",
    paths: {
        'jquery': ['jquery.min'],
        'bootstrap': ['bootstrap.min']
    },
    shim: {
        /* Set bootstrap dependencies (just jQuery) */
        'bootstrap': ['jquery']
    }
});

require(['jquery', 'bootstrap'], function ($) {
    console.log("Loaded :)");
});