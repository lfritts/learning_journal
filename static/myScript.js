
function addEntry() {
    $(".add_entry").submit(function(e)
        {
            addTitle = $(this).title.val();
            addText = $(this).text.val();
            $.ajax({
                url: $(this).attr("action"),
                type: POST,
                data: 'title': $(this).title.val(),
                      'text': $(this).text.val();
                success: function(response) {
                    $('.entry').prepend(response);
                }
            })
        })
}