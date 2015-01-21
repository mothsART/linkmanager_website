function getNumber(element){
    var number;
    $.each(element.parent().children(), function(index, value) {
        if ($(value).is(element)) {
            var td = element.parent().parent().parent();
            var pre = $(td.prev().children()[0]).children()[0];
            number = $(pre).children().eq(index);
            return false;
        }
    });
    return number;
}


function getLine(element){
    var line;
    $.each(element.parent().children(), function(index, value) {
        if ($(value).is(element)) {
            var td = element.parent().parent().parent();
            var pre = $(td.next().children()[0]).children()[0];
            line = $(pre).children().eq(index);
            return false;
        }
    });
    return line;
}

$(document).ready(function(){
    /* highligths line correpondant to his number */
    $('.linenodiv a').hover(function(){
        getLine($(this)).addClass('highlight-line');
    }, function(){
        getLine($(this)).removeClass('highlight-line');
    });
    /* highligths number correpondant to his line */
    $('.highlight span').hover(function(){
        getNumber($(this)).addClass('highlight-line');
    }, function(){
        getNumber($(this)).removeClass('highlight-line');
    });
    /* if the URL's #anchor correpond to a code line, hightight it */
    var lineTarget = $('a[name="' + window.location.hash.slice(1) + '"]').parent();
    lineTarget.addClass('hash-line');
    var nbTarget = getNumber(lineTarget);
    if (nbTarget){
        nbTarget.addClass('hash-line');
    }
    $(window).on('hashchange', function() {
        if (nbTarget){
            lineTarget.removeClass('hash-line');
            getNumber(lineTarget).removeClass('hash-line');
        }
        lineTarget = $('a[name="' + window.location.hash.slice(1) + '"]').parent();
        lineTarget.addClass('hash-line');
        getNumber(lineTarget).addClass('hash-line');
    });
});
