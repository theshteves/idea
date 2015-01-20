$(document).ready( function() {
    $("#wallpaper").fadeOut(1);
    $("main").toggle("slide", {direction: "up"}, 1);

    $("#wallpaper").delay(2000).fadeIn(2000);
    $("main").delay(3000).toggle("slide", {direction: "down", distance: 100}, 500);

    $(window).on("scroll", function() {
	var navHeight = $(window).height() - 80;
	if ($(window).scrollTop() > navHeight) {
	    $("#toolbar").css("position","fixed");
	}
	else {
	    $("#toolbar").css("position","absolute");
	}
    });

});
