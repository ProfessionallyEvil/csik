window.x_id = 'not-sup';
window.xfilr = (function() {
   var xhr = new XMLHttpRequest();
   xhr.open('GET', '$$HOST$$/id', true);
   xhr.onload = function (res) {
     window.x_id = res;
   };
   xhr.onreadystatechange = function () {
      if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
          window.x_id = JSON.parse(this.responseText).val;
      }
   };
   xhr.send();

  return function(type, payload) {
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '$$HOST$$/' + type + '?i=' + (typeof window.x_id === 'object' ? JSON.parse(window.x_id.target.responseText).val : window.x_id), true);
    xhr.send(JSON.stringify(payload));
  }
})();