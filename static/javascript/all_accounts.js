function search( e ) {
    e.preventDefault();
    var myform = document.getElementById("search_form");
    var fd = new FormData( myform );
    $.ajax({
        url: "all_accounts/search",
        data: fd,
        cache: false,
        processData: false,
        contentType: false,
        type: 'POST',
        dataType: "json"

    }).done(function (data) {
        loadAccounts(data);
        // var template = '{{#data}}<tr><th>{{id}}</th><td>{{first_name}}</td><td>{{last_name}}</td><td>{{position}}</td><td>{{date_joined}}</td><td>{{salary}}</td></tr>{{/data}}';
        // var html = Mustache.to_html(template, data);

        // $( "#my_tbody" ).html(html);

    }).fail(function (data) {

    });
}
$( window ).on( "load", search );

// $( document ).ready(function() {
//
// });

function loadAccounts(data) {
  var template = $('#js_template').html();
  Mustache.parse(template);   // optional, speeds up future uses
  var rendered = Mustache.render(template, {acc_data: data});
  $('#my_tbody').html(rendered);
}

var searchTimeout = 0;

function searchWithDelay( e ) {
    clearTimeout(searchTimeout);
    searchTimeout = setTimeout(function () {
        search( e );
    }, 200);
}

$( "#search_form" ).on( "submit", search );
$( "#search_form input" ).on( "input", searchWithDelay );
$( "#search_form select" ).on( "change", search );
