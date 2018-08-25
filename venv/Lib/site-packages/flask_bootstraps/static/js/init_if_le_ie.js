/**
 * Created by yinhezhixing on 09/06/2017.
 */
requirejs.config({
    baseUrl: "/static/bootstrap/js",
    paths: {
        'html5shiv': ['html5shiv.min'],
        'respond': ['respond.min']
    }
});

require(['html5shiv', 'respond'], function ($) {
    console.log("Loaded :)");
});