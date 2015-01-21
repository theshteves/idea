var express = require('express');
var path = require('path');
var db = require('./database.js');
var app = express();

app.use(express.static(path.join(__dirname, '../site')));

app.get('/', function(req, res) {
    res.sendFile('index.html');
});
app.listen(8888);

/*
app.get('/male', function(req, res) {
req.pipe(profile/generate.py).pipe(process.stdout);
    PythonShell.run('profile/generate.py', {args: ['gender = 1']}, function(err, results) {
	if (err) throw err;
	console.log(results);
    });

});
*/
console.log("Server created at localhost:8888");
