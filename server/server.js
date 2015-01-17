var express = require('express');
var app = express();
var path = require('path');

app.get("/", function(req, res) {
    res.sendFile('index.html', {root: path.join(__dirname, "../site")});
});

app.listen(8888);
console.log("Server created at localhost:8888");
