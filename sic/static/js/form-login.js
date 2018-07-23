// $('input[name="csrfmiddlewaretoken"]').prop('value')
$('#form-login').bind('submit', function(){

    $.ajax({

        type: $(this).attr('method'),
        url: $(this).attr('action'),
        dataType: 'json',
        data: $(this).serialize(), // Pega os campos do form, incluso o CSRF_TOKEN
        success: function(data){
            if(data['error'] == 'access-denied'){
                $('#resultado').html('Usuário ou senha incorretos!')
                $('#username').val('')
                $('#password').val('')
            }else
                window.location.href='/'
        },
        error: function(xhr, errormsg, status){
           if(xhr.status == 403)
              $('#resultado').html('Forbidden (CSRF token missing or incorrect.)')
           if(xhr.status == 404)
              $('#resultado').html('A pagina solicitada não foi encontrada.')
        }
    });
    return false;
});