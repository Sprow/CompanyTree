function search( e, page = 1 ) {
    e.preventDefault();
    let myform = document.getElementById("search_form");
    let fd = new FormData( myform );
    $.ajax({
        url: "all_accounts/search?page="+page,
        data: fd,
        cache: false,
        processData: false,
        contentType: false,
        type: 'POST',
        dataType: "json"

    }).done(function (data) {
        loadAccounts(data);
        myPaginator(page, data['items_count']);

        // my_pag(data);
        // let template = '{{#data}}<tr><th>{{id}}</th><td>{{first_name}}</td><td>{{last_name}}</td><td>{{position}}</td><td>{{date_joined}}</td><td>{{salary}}</td></tr>{{/data}}';
        // let html = Mustache.to_html(template, data);

        // $( "#my_tbody" ).html(html);

    }).fail(function (data) {

    });
}

function loadAccounts(data) {
  let template = $('#js_template').html();
  // console.log(data);
  // console.log(data['data']);
  Mustache.parse(template);   // optional, speeds up future uses
  let rendered = Mustache.render(template, data);
  // console.log('render>>>', rendered);

  // console.log('template>>>>', template);
  // console.log('data>>>>', data);
  $('#my_tbody').html(rendered);
}

let searchTimeout = 0;

function searchWithDelay( e ) {
    clearTimeout(searchTimeout);
    searchTimeout = setTimeout(function () {
        search( e );
    }, 200);
}

function myPaginator(currentPage, itemsCount, itemsPerPage = 10) {
    let template = $('#pagination_template').html();
    // console.log(template);
    let pageCount = Math.ceil(itemsCount/itemsPerPage);
    let myPage = []; // MAKE DICT
    if (pageCount <= 7) {
        for (let i = 1; i <= pageCount; i++) {
            myPage.push({'name': i, 'page': i});
        }
    }
    if (pageCount > 7) {
        if (currentPage > 2) {
            myPage.push({'name': 'first', 'page': 1});
        }
        if (currentPage > 1) {
            myPage.push({'name': 'prev', 'page': currentPage -1});
        }
        if (currentPage >= 4 ) {
            if (currentPage+2 <= pageCount) {
                for (let i = currentPage -2; i <= currentPage+2; i++) {
                    myPage.push({'name': i, 'page': i});
                }
            }else {
                for (let i = currentPage -2; i <= pageCount; i++) {
                    myPage.push({'name': i, 'page': i});
                }
            }
        }else if (currentPage < 4) {
            for (let i = currentPage; i <= currentPage+2; i++) {
                myPage.push({'name': i, 'page': i});
            }
        }
    }
    if (currentPage != pageCount) {
        myPage.push({'name': 'next', 'page': currentPage+1});
    }
    if (pageCount > 7 && currentPage+3 <= pageCount) {
        myPage.push({'name': 'last', 'page': pageCount})
    }
    // return myPage;
    Mustache.parse(template);   // optional, speeds up future uses
    let rendered = Mustache.render(template, {'data': myPage});
    // console.log(rendered);
    $('#pagination').html(rendered);
}

$( "#search_form" ).on( "submit", search );
$( "#search_form input" ).on( "input", searchWithDelay );
$( "#search_form select" ).on( "change", search );
$( window ).on( "load", search );
$('#pagination').on( "click", ".my_pagination_btn", function( e ) {
    search( e, parseInt($(this).data("page")));
});
