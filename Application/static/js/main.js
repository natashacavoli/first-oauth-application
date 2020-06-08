$(document).ready(function(){

    $("#show").click(function(event){

        event.preventDefault();

        $("#secret").toggle("slow");
    });

    $("#opener").click(function(event){

        event.preventDefault();

        $("#alert").toggle("slow");

    });

});
