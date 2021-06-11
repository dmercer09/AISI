$(document).ready(function () {
    $('#createPost').submit(function (e) {
        e.preventDefault();

        console.log(e)
        console.log(this);

        $.ajax({
            url: '/create_post',
            method: 'post',
            data: $(this).serialize(),
            success: function (serverResponse) {


                console.log("this is ajax working with our posts");
                console.log(serverResponse);
                $('.allposts').prepend(serverResponse);
            }
            
        })


    })

    $('#like').click(function (e) {

        var hiddenvalue = $('#hiddenvalue').attr("value");
        console.log(hiddenvalue)

        $.ajax({
      
            url: `/like/${hiddenvalue}`,
            method: 'get',
            data: $(this).serialize(),
            success: function (serverResponse) {
                console.log("this is ajax working");
                console.log(serverResponse);

                $(`#likes${hiddenvalue}`).replaceWith($(`#likes${hiddenvalue}`, serverResponse));
          

            }
        })

    });
    $('#createComment').submit(function (e) {
        e.preventDefault();

        console.log(e)
        console.log(this);
        var formAction = this.action;
    

        console.log(formAction)

        console.log()

        $.ajax({
            url: formAction,
            method: 'post',
            data: $(this).serialize(),
            success: function (serverResponse) {
                console.log("this is ajax working");
                console.log(serverResponse);
                $('.allComments').prepend(serverResponse);

            }
        })


    })




});