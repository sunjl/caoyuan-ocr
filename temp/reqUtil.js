var envConfig = require('../config/envConfig');

exports.convert = function (req, callback) {
    var currentUser = {};
    var page = 0;
    var size = 10;

    var reqCookie = req.cookies[envConfig.cookieName];
    var reqPage = req.query.page;
    var reqSize = req.query.size;

    if (typeof reqCookie != 'undefined') {
        currentUser = JSON.parse(reqCookie);
    }
    if (typeof reqPage != 'undefined') {
        page = reqPage;
    }
    if (typeof reqSize != 'undefined') {
        size = reqSize;
    }
    callback(page, size, currentUser);
};