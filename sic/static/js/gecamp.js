// $('input[name="csrfmiddlewaretoken"]').prop('value')

function login(){
    $('#form-login').on('submit', function(e){
        e.preventDefault();
//        var data = {
//                'username':'admin',
//                'password':'12345678a',
//                'csrfmiddlewaretoken': csrftoken,
//            }

        $.ajax({
            url: '/login/',
            type: 'POST',
            dataType: 'json',
            data: $('#form-login').serialize(),

            done: function(json){
                alert()
            },

            error: function(hxr, errormsg, status){
                console.log(hxr.status + '4646464644')
            }
        });
    })
}

//
//$(document).ready(function(){
//
//
//
////   login();
////   console.log(csrftoken)
////   console.log($('input[name="csrfmiddlewaretoken"]').prop('value'))
////   console.log($('#form-login').serialize())
//});



$('#form-login').bind('submit', function(){

    $.ajax({

        type: $(this).attr('method'),
        url: $(this).attr('action'),
        dataType: 'json',
        data: $(this).serialize(),
        success: function(data){
            $('#resultado').html(data['data'])
        },
        error: function(){
            alert('Error')
        }


    });

    return false;

});






