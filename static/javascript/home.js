function tree(e, parent_id = 1, level = 1) {
    e.preventDefault();
    let myform = document.getElementById("home_page");
    console.log(myform);
    let fd = new FormData(myform);
    console.log(fd);
    $.ajax({
        // url: "tree",
        url: "tree?parent_id=" + parent_id,
        data: fd,
        cache: false,
        processData: false,
        contentType: false,
        type: 'POST',
        dataType: "json"

    }).done(function (data) {
        console.log(data);
        firstAndSecondLevels(data);
    });
}

function firstAndSecondLevels(data) {
    let template = $('#js_template').html();
    console.log(template);
    console.log(data);
    Mustache.parse(template);   // optional, speeds up future uses
    let rendered = Mustache.render(template, data);
    $('#tree').html(rendered);
}


$( window ).on( "load", tree );
$('#tree').on( "click", ".tree_element", function( e ) {
    tree(e, parseInt($(this).data("id")));
});