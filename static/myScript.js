
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
                    $(".content").prepend(
                        <article class="entry" id="entry=" + response.id>
                        <h3>response.title</h3>
      <p class="dateline">{{ entry.created.strftime('%b. %d, %Y') }}
      <div class="entry_body">
        {{ entry.text|safe }}
        <div class="select_entry">
          <a href="edit/{{entry.id}}">Edit</a>
        </div>
      </div>
    </article>);
                }
            })
        })
}