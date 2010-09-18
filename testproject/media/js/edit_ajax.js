$(document).ready(function() {
    var options = { 
        target:        '#person-edit-form',
        url:            '/edit_ajax/',
        beforeSubmit:  beginAjax,  
        success:       endAjax
    };  
    $('#person-edit-form').ajaxForm(options);

    addDatePicker();
});

function addLoader() {
    $('#person-edit-form').append('<img id="ajax-loader" src="/static_media/img/ajax-loader.gif"/>');
}

function removeLoader() {
    $('#ajax-loader').remove();
}

function disableInput(index) {
    $(this).attr('disabled', 'disabled');
}

function disableForm() {
    $('#person-edit-form').find('input').each(disableInput);
    $('#person-edit-form').find('textarea').each(disableInput);
}

function enableForm() {
    $('#person-edit-form').find('input').removeAttr('disabled');
    $('#person-edit-form').find('textarea').removeAttr('disabled');
}

function beginAjax(formData, jqForm, options) {
    disableForm();
    addLoader();
    return true;
}

function endAjax(responseText, statusText, xhr, $form) {
    enableForm();
    removeLoader();
    addDatePicker();
}

