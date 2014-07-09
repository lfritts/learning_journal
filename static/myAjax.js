$(document).ready(function () {
    var postAction = 'add';
    var targetPost;
    var targetForm = $('form');
    $('.edit-post').on('click', function () {
        postAction = 'edit';
        // changed from $(this).closest('.entry')
        targetPost = $(this);
        console.log(targetPost);
        var postID = targetPost.closest('.entry').data('id');
        var postTitle = targetPost.closest('.entry').find('#post-title').text();
        var postText = $.trim(targetPost.closest('.entry').find('span').text());
        $('#title').val(postTitle);
        $('#text').val(postText);
        targetForm.attr('action', '/edit/' + postID);
        targetForm.removeClass('add_entry').addClass('edit_entry');
        $('#submit').val('Update');
    // });
        if (postAction == 'edit') {
            $('.edit_entry').on('submit', function(changeEntry){
                changeEntry.preventDefault();
                $.ajax('/update_entry/' + postID, {
                    type: 'POST',
                    data: $('form').serialize(),
                    success: function(entryData) {
                        console.log(entryData.id);
                        targetPost.closest('.entry').find('#post-title').text(entryData.title);
                        targetPost.closest('.entry').find('span').text(entryData.text);
                        $('.edit_entry')[0].reset();
                        targetForm.attr('action', '/add');
                        targetForm.removeClass('edit_entry').addClass('add_entry');
                        $('#submit').val('Share');
                    }
                });
            });
        } else {
            $('.add_entry').on('submit', function(addEntry){
                addEntry.preventDefault();
                $.ajax('/add', {
                    type: 'POST',
                    data: $('form').serialize(),
                    success: function(entryData) {
                        $('.entry').first().prepend(entryData);
                        $('.add_entry')[0].reset();
                    }
                });
            });
        }
    });
})