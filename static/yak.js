$(document).ready(function(){

  var onSuccess = function(data, status) {
    console.log(data.ave)
    $("#yakresult span").text(data.yaks)
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
