$(document).ready(function(){

  var onSuccess = function(data, status) {
    $("#yakContainer").empty();
    $("#yakTemplate").tmpl(data.yaks).appendTo("#yakContainer");
    $("#mapContainer").empty();
    $("#mapTemplate").tmpl(data.coords).appendTo("#mapContainer");
  };

  var onError = function(data, status) {
    console.log("status", status);
    console.log("error", data);
  };

  $("#searchschool").submit(function(event) {
    event.preventDefault();

    var school = $("#searchschool").find("[name='sought']").val();

    $.post("searchSchool", {
      school: school
    })
      .done(onSuccess)
      .error(onError);

  });
});
