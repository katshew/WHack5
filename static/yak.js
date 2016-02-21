$(document).ready(function(){

  var isUpdated = false;

  var onSuccess = function(data, status) {
    $("#sought").val("");
    $("#yakContainer").empty();
    $("#yakTemplate").tmpl(data.yaks).appendTo("#yakContainer");

    $.post("getWeightedAverages", {})
      .done(weightedAveragesSuccess)
      .error(onError);

    $.post("getKeywords", {})
      .done(keywordsSuccess)
      .error(onError);

    $("#mapContainer").empty();
    $("#mapTemplate").tmpl(data.coords).appendTo("#mapContainer");
  };

  var weightedAveragesSuccess = function(data, status) {
    console.log(data);
  }

  var keywordsSuccess = function(data, status) {
    var words = $.parseJSON(data);
    if(isUpdated) {
      $("#keywords").jQCloud('update', words);
    } else {
      $("#keywords").jQCloud(words);
      isUpdated = true;
    }
  }

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
