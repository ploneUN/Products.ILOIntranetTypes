jq(document).ready(function () {
    var attendeeSelect = $('#event-attendee-select input');
    var update_input = function () {
        $('#event-invite-form [name=invited_users]').val($('.as-values').val());
    }
    attendeeSelect.autoSuggest(attendeeSelect.attr('rel'), {
        selectedItemProp: "name", 
        searchObjProps: "name",
        selectionAdded: update_input,
        selectionRemoved: update_input
    });
})
