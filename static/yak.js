var isUpdated = false;

$(document).ready(function(){

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

  var weightedAverageError = function(data, status) {
    console.log("Weighted Average Function")
    console.log("status", status);
    console.log("error", error);
  }

  var keywordsFailure = function(data, status) {
    console.log("Keywords Function")
    console.log("status", status);
    console.log("error", error);
  }

  var weightedAveragesSuccess = function(data, status) {
    if(data.message == "Neutral") {
      alert("Could not find any yaks for that school");
    }
    $("#positivity").html("<h2 style='" + data.style + "'>" + data.percent + "% " + data.message + "</h2>");
  }

  var keywordsSuccess = function(data, status) {
    var words = $.parseJSON(data);
    $("#keywords").jQCloud(words);
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
