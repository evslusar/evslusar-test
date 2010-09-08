$(document).ready(function() {
    var options = { 
        target:        '#person-edit-form',
        url:            '/edit_ajax/',
        beforeSubmit:  disableForm,  
        success:       enableForm
    }; 
 
    $('#person-edit-form').ajaxForm(options);
});

function disableForm(formData, jqForm, options) {
    return true
}

function enableForm(responseText, statusText, xhr, $form) {
}
