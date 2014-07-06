$(document).ready(function () {
    var postAction = 'add';
    var targetPost;
    $('.edit-post').on('click', function () {
        postAction = 'edit';
        targetPost = $(this);
        var postID = targetPost.closest('.entry').data('id');
        var postTitle = targetPost.closest('.entry').find('#post-title').text();
        var postText = $.trim(targetPost.closest('.entry').find('span').text());
        $('#title').val(postTitle);
        $('#text').val(postText);
        $('form').attr('action', '/edit/' + postID);
        $('form').removeClass('add_entry').addClass('edit_entry');
        $('#submit').val('Update');
    });
    if (postAction == 'edit') {
        $('.edit_entry').on('submit', function(changeEntry){
            changeEntry.preventDefault();
            $.ajax('/update_entry/' + postID, {
                type: 'POST',
                data: $('form').serialize(),
                success: function(entryData) {
                    console.log(entryData.id);
                    // var target = $(this).closest('#content').find(".newEntry").find(entryData.id);
                    // var target = $('.entry').first().find(".newEntry").find(entryData.id);
                    // console.log($('.entry').first().find('#entry=46'));
                    // console.log(target.find('#post-title').text());
                    // target.find('#post-title').text(entryData.title);
                    targetPost.find('#post-title').text(entryData.title);
                    // target.find('span').text(entryData.text);
                    targetPost.find('span').text(entryData.text);
                    // $('.newEntry').html(entryData);
                    // $('.edit').remove();
                    $('.edit_entry')[0].reset();
                    $('form').attr('action', '/add');
                    $('form').removeClass('edit_entry').addClass('add_entry');
                    $('#submit').val('Share');
                    // postAction = 'add'
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
    };
});