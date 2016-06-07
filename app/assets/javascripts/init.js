$(document).ready(function() {
  $(".button-collapse").sideNav();
  $('.materialboxed').materialbox();

  $(".on-off-buttons").on("click", "#on", function(e) {
    e.preventDefault()

    $.ajax({
      url: "http://172.16.50.242:9009",
      method: "POST",
      data: "ONN"
    })

    .done(function(msg) {
      console.log(msg);
    })

    .fail(function(err) {
      console.log(err);
    })
  })

  $(".on-off-buttons").on("click", "#off", function(e) {
    e.preventDefault()

    $.ajax({
      url: "http://172.16.50.242:9009",
      method: "POST",
      data: "OFF"
    })

    .done(function(msg) {
      console.log(msg);
    })

    .fail(function(err) {
      console.log(err);
    })
  })
})