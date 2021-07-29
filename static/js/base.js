//typing effect
document.addEventListener("DOMContentLoaded", function() {
  keys()
});
  var i = 0;
  var txt = 'Welcome To the Online Quiz Portal.';
  var speed = 100;
  function keys() {

    if (i < txt.length) {
      document.getElementById("type_effect").innerHTML += txt.charAt(i);
      i++;
      setTimeout(keys, speed);
  }
}
