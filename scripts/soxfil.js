window.x_id = 'not-sup';
window.xfilr = (function() {
  var socket = io.connect('$$HOST$$/x');
  fetch('$$HOST$$/id')
      .then(function(res) {
    return res.json();
  })
      .then(function(jsonRes) {
    window.x_id = JSON.parse(jsonRes).val;
  });
  return function(type, payload) {
    socket.emit('xfil', JSON.stringify({
      i: window.x_id,
      t: type,
      p: payload
    }));
  }
})();