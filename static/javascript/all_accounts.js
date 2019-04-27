function tableNavigator() {
    let obj = {};
    obj.page = 1;
    obj.order_by = 'id';
    obj.itemsPerPage = 10;
    obj.searchTimeout = 0;
    obj.search = function (e) {
        e.preventDefault();
        let myform = document.getElementById("search_form");
        let fd = new FormData(myform);
        let page = obj.page;
        let order_by = obj.order_by;
        $.ajax({
            url: "all_accounts/search?page=" + page + "&order_by=" + order_by,
            data: fd,
            cache: false,
            processData: false,
            contentType: false,
            type: 'POST',
            dataType: "json"

        }).done(function (data) {
            console.log(page);
            obj.loadAccounts(data);
            obj.myPaginator(data['items_count']);
        });
    };

    obj.loadAccounts = function (data) {
        let template = $('#js_template').html();
        Mustache.parse(template);   // optional, speeds up future uses
        let rendered = Mustache.render(template, data);
        $('#my_tbody').html(rendered);
    };

    obj.searchWithDelay = function (e) {
        clearTimeout(obj.searchTimeout);
        obj.searchTimeout = setTimeout(function () {
            obj.search(e);
        }, 200);
    };

    obj.searchWithPage = function (e, page) {
        obj.page = page;
        obj.search(e);
    };

    obj.searchWithOrder = function (e, order_by) {
        if (obj.order_by.indexOf("+reverse") +1) {
            obj.order_by = order_by;
        } else if (obj.order_by == order_by) {
            obj.order_by = order_by + "+reverse";
        } else if (obj.order_by != order_by) {
            obj.order_by = order_by;
        }
        obj.search(e)
    };

    obj.myPaginator = function (itemsCount) {
        let template = $('#pagination_template').html();
        let pageCount = Math.ceil(itemsCount / obj.itemsPerPage);
        let myPage = [];
        if (pageCount <= 7) {
            for (let i = 1; i <= pageCount; i++) {
                myPage.push({'name': i, 'page': i});
            }
        }
        if (pageCount > 7) {
            if (obj.page > 2) {
                myPage.push({'name': 'first', 'page': 1});
            }
            if (obj.page > 1) {
                myPage.push({'name': 'prev', 'page': obj.page - 1});
            }
            if (obj.page >= 4) {
                if (obj.page + 2 <= pageCount) {
                    for (let i = obj.page - 2; i <= obj.page + 2; i++) {
                        myPage.push({'name': i, 'page': i});
                    }
                } else {
                    for (let i = obj.page - 2; i <= pageCount; i++) {
                        myPage.push({'name': i, 'page': i});
                    }
                }
            } else if (obj.page < 4) {
                for (let i = obj.page; i <= obj.page + 2; i++) {
                    myPage.push({'name': i, 'page': i});
                }
            }
        }
        if (obj.page != pageCount) {
            myPage.push({'name': 'next', 'page': obj.page + 1});
        }
        if (pageCount > 7 && obj.page + 3 <= pageCount) {
            myPage.push({'name': 'last', 'page': pageCount})
        }
        Mustache.parse(template);   // optional, speeds up future uses
        let rendered = Mustache.render(template, {'data': myPage});
        $('#pagination').html(rendered);
    };
    return obj;
}

let nav = tableNavigator();

$( "#search_form input" ).on( "input", nav.searchWithDelay );
$( "#search_form select" ).on( "change", nav.search );
$( window ).on( "load", nav.search );
$('#pagination').on( "click", ".my_pagination_btn", function( e ) {
    nav.searchWithPage(e, parseInt($(this).data("page")));
});
$('.thead-arrows__sort').on( "click", ".arrows", function( e ) {
    nav.searchWithOrder(e, $(this).data("sort"));
});

// function search( e, page = 1, order_by = 'id' ) {
//     e.preventDefault();
//     let myform = document.getElementById("search_form");
//     let fd = new FormData( myform );
//     $.ajax({
//         url: "all_accounts/search?page="+page+"&order_by="+order_by,
//         data: fd,
//         cache: false,
//         processData: false,
//         contentType: false,
//         type: 'POST',
//         dataType: "json"
//
//     }).done(function (data) {
//         loadAccounts(data);
//         myPaginator(page, data['items_count']);
//
//         // my_pag(data);
//         // let template = '{{#data}}<tr><th>{{id}}</th><td>{{first_name}}</td><td>{{last_name}}</td><td>{{position}}</td><td>{{date_joined}}</td><td>{{salary}}</td></tr>{{/data}}';
//         // let html = Mustache.to_html(template, data);
//
//         // $( "#my_tbody" ).html(html);
//     });
// }

// function loadAccounts(data) {
//   let template = $('#js_template').html();
//   Mustache.parse(template);   // optional, speeds up future uses
//   let rendered = Mustache.render(template, data);
//   $('#my_tbody').html(rendered);
// }

// let searchTimeout = 0;
//
// function searchWithDelay( e ) {
//     clearTimeout(searchTimeout);
//     searchTimeout = setTimeout(function () {
//         search( e );
//     }, 200);
// }
//
// function myPaginator(currentPage, itemsCount, itemsPerPage = 10) {
//     let template = $('#pagination_template').html();
//     let pageCount = Math.ceil(itemsCount/itemsPerPage);
//     let myPage = [];
//     if (pageCount <= 7) {
//         for (let i = 1; i <= pageCount; i++) {
//             myPage.push({'name': i, 'page': i});
//         }
//     }
//     if (pageCount > 7) {
//         if (currentPage > 2) {
//             myPage.push({'name': 'first', 'page': 1});
//         }
//         if (currentPage > 1) {
//             myPage.push({'name': 'prev', 'page': currentPage -1});
//         }
//         if (currentPage >= 4 ) {
//             if (currentPage+2 <= pageCount) {
//                 for (let i = currentPage -2; i <= currentPage+2; i++) {
//                     myPage.push({'name': i, 'page': i});
//                 }
//             }else {
//                 for (let i = currentPage -2; i <= pageCount; i++) {
//                     myPage.push({'name': i, 'page': i});
//                 }
//             }
//         }else if (currentPage < 4) {
//             for (let i = currentPage; i <= currentPage+2; i++) {
//                 myPage.push({'name': i, 'page': i});
//             }
//         }
//     }
//     if (currentPage != pageCount) {
//         myPage.push({'name': 'next', 'page': currentPage+1});
//     }
//     if (pageCount > 7 && currentPage+3 <= pageCount) {
//         myPage.push({'name': 'last', 'page': pageCount})
//     }
//     Mustache.parse(template);   // optional, speeds up future uses
//     let rendered = Mustache.render(template, {'data': myPage});
//     $('#pagination').html(rendered);
// }

// $( "#search_form" ).on( "submit", search );
// $( "#search_form input" ).on( "input", searchWithDelay );
// $( "#search_form select" ).on( "change", search );
// $( window ).on( "load", search );
// $('#pagination').on( "click", ".my_pagination_btn", function( e ) {
//     search( e, parseInt($(this).data("page")));
// });
//
// $('.thead-arrows__sort').on( "click", ".arrows", function( e ) {
//     console.log($(this).data("sort"));
//     search( e, page= 1, $(this).data("sort"));
// });