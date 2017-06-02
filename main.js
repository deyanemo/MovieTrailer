$(document).ready(function(){
    $(".item", this).click(function(event) {
        // var theSource = $(".movieimg").attr('alt');
        // $(".model").animate({opacity: "1"}, 500);
        // $("#obj1").attr('data', theSource);

    });

    $(".close").click(function(event) {
        $(this).parent().hide(500);
        // cause i cant control the video inside of a iframe its easier way to just empty the source!
    });
});