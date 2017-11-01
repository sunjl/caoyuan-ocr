exports.convert = function (req, callback) {
    var page = 0;
    var size = 10;

    var reqPage = req.query.page;
    var reqSize = req.query.size;

    if (typeof reqPage != 'undefined') {
        page = reqPage;
    }
    if (typeof reqSize != 'undefined') {
        size = reqSize;
    }
    callback(page, size);
};