$(function() {
  $('button').click(function() {
    //var user = $('#txtUsername').val();
    //var pass = $('#txtPassword').val();
    $.ajax({
      url: '/script',
      //data: $('form').serialize(),
      type: 'POST',
      success: function(response) {
        console.log(response);
        //document.write(response);
      },
      error: function(error) {
        console.log(error);
      }
    });
  });

  $("#searchbutton").click(function() {
    $.ajax({
      url: '/search',
      type: 'GET',
      data: {cid: $('#search').val()},
      datatype: 'json',
      success: function(response) {
        console.log(response),
        //console.log($('#search').val());
        //var obj = JSON.parse(response),
        $("#results").text(response.canonical_smiles);
        $("#results-molecular-formula").text(response.molecular_formula);
        $("#results-iupac-name").text(response.iupac_name);

        //$("#results").text(response);
      },
      error: function(error) {
        console.log(error),
        $("#results").text("Error: Not a valid CID");
        $("#results-molecular-formula").text("");
        $("#results-iupac-name").text("");
      }
    });
  });

  $("#searchbutton_b").click(function() {
    $.ajax({
      url: '/search',
      type: 'GET',
      data: {cid: $('#search_b').val()},
      datatype: 'json',
      success: function(response) {
        console.log(response),
        //console.log($('#search').val());
        //var obj = JSON.parse(response),
        $("#results_b").text(response.canonical_smiles),
        $("#results-molecular-formula_b").text(response.molecular_formula),
        $("#results-iupac-name_b").text(response.iupac_name);

        //$("#results").text(response);
      },
      error: function(error) {
        console.log(error),
        $("#results_b").text("Error: Not a valid CID"),
        $("#results-molecular-formula_b").text(""),
        $("#results-iupac-name_b").text("");
      }
    });
  });

  $("#mixbutton").click(function() {
    $.ajax({
      url: '/mix',
      type: 'GET',
      data: {chem1: $('#search').val(), chem2: $('#search_b').val()},
      success: function(response) {
        console.log(response),
        //console.log($('#search').val());
        //var obj = JSON.parse(response),
        $("#mixresults").html(response);

        //$("#results").text(response);
      },
      error: function(error) {
        console.log(error),
        $("#mixresults").text("Error");
      }
    });
  });

});

