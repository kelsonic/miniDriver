$(document).ready(function() {
  $(".button-collapse").sideNav();
  $('.materialboxed').materialbox();

  $("#on").on("click", function(e) {
    e.preventDefault()

    $.ajax({
      url: "192.16.51.218",
      method: "POST",
      data: "ON"
    }).done(function(msg) {
      console.log(msg);
    }).fail(function(err) {
      console.log(err);
    })
  })

  $("#off").on("click", function(e) {
    e.preventDefault()
    
    $.ajax({
      url: "192.16.51.218",
      method: "POST",
      data: "OFF"
    }).done(function(msg) {
      console.log(msg);
    }).fail(function(err) {
      console.log(err);
    })
  })
})