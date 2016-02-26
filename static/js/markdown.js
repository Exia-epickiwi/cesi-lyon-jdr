/**
 * Created by baptiste on 24/02/16.
 */

$(function(){
    $(".mdFormated img").each(function(index,element){
       var $img = $(element);
        var imgsrc = $img.attr("src");
        var imgTitle = $img.attr("title");
        var imgAlt = $img.attr("alt");
        var newElement = "<div class='image ";
        if(index % 2 == 0){
            newElement += "even'>";
        } else {
            newElement += "odd'>";
        }
        newElement += "<img src='"+imgsrc+"' alt='"+imgAlt;
        if(imgTitle){
            newElement +=  "title='"+imgTitle+"'/>";
            newElement += "<div class='imageInfo'>"+imgTitle+"</div>";
        } else {
            newElement += "'/>";
        }
        newElement += "</div>";
        $img.after(newElement);
        $img.remove();
    });
});