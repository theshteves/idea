var express = require('express');
var path = require('path');
//var db = require('./database.js');
var app = express();
var PythonShell = require('python-shell');

app.use(express.static(path.join(__dirname, '../site')));

app.get('/', function(req, res) {
    res.sendFile('index.html');
});
app.listen(8888);

app.get('/female', function(req, res) {
    PythonShell.run('generate.py', {scriptPath: 'profile', args: ['0']}, function (err, results) {
	if (err) throw err;
	console.log(JSON.parse(results));
    });
});

app.get('/male', function(req, res) {
    PythonShell.run('generate.py', {scriptPath: 'profile', args: ['1']}, function (err, results) {
	if (err) throw err;
	console.log(JSON.parse(results));
    });
});

console.log("Server created at localhost:8888");
