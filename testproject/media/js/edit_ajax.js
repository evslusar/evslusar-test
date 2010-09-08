$(document).ready(function() {
    var options = { 
        target:        '#person-edit-form',
        url:            '/edit_ajax/',
        beforeSubmit:  disableForm,  
        success:       enableForm
    };  
    $('#person-edit-form').ajaxForm(options);

    addDatePicker();
});

function disableInput(index) {
    $(this).attr('disabled', 'disabled');
}

function disableForm(formData, jqForm, options) {
    $('#person-edit-form').find('input').each(disableInput);
    $('#person-edit-form').find('textarea').each(disableInput);
    return true;
}

function enableForm(responseText, statusText, xhr, $form) {
    $('#person-edit-form').find('input').removeAttr('disabled');
    $('#person-edit-form').find('textarea').removeAttr('disabled');

    addDatePicker();
}
