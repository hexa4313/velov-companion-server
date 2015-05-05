var express = require('express');
var app = express();
var exec = require('child_process').exec;

app.get('/api/route', function(req, res) {

  var from_lat = req.query.start_latitude
  var from_lon = req.query.start_longitude
  var to_lat = req.query.end_latitude
  var to_lon = req.query.end_longitude

  exec('java -jar brouter.jar segments ' + from_lon + ' ' + from_lat + ' ' + 
    to_lon + ' ' + to_lat + ' profiles/safety.brf',
    function (error, stdout, stderr) {
    
    res.send(stdout)
  });

});

app.listen(8888);