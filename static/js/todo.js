function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function (xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrfToken);
        }
    }
});

function updateTask(taskId, data) {
    return $.ajax({
        url: '/tasks/' + taskId + '/',
        method: 'patch',
        data: data,
    })
}

$(document).ready(function () {
    $('.js-add-note-button').keyup(function (e) {
        if (e.which != 13) {
            return
        }
        $('#task_form').submit()
    })
    $('.js-task-checkbox input').click(function (e) {
        updateTask($(e.target).data('id'), { is_done: e.target.checked }).fail(function (response) {
            console.log(response)
        })
    })
    $('.js-datepicker').datepicker({
        format: 'dd-mm-yyyy HH:MM',
        timepicker: true,
        language: 'en',
        minDate: new Date(),
        onChangeView: function() {
            alert('aaa')
        },
        onSelect: function (formattedDate, date, inst) {
            var taskId = $(inst.$el).data('id')
            updateTask(taskId, { due_at: date.toISOString() }).fail(function (response) {
                console.log(response)
            })
        }
    })

    $('.js-remove-task').click(function(){
        $.ajax({
            url: '/tasks/' + $(this).data('id') + '/',
            method: 'delete',
        }).done(function(){
            window.location.href = window.location.href
        })
    })
    $('.js-labels').change(function(e){
        console.log(e.target.value)

        $.ajax({
            url: '/tasks/' + $(this).data('id') + '/labels/',
            method: 'post',
            data: {
                labels: e.target.value,
            }
        })
    })
})
