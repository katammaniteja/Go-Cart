document.querySelector('.decrement-btn').addEventListener('click', (event) => {
    event.preventDefault();
    var value = document.querySelector('.qty-input').value;
    value = parseInt(value);
    if (value > 1) value--;
    document.querySelector('.qty-input').value = value;
})
document.querySelector('.increment-btn').addEventListener('click', (event) => {
    event.preventDefault();
    var value = document.querySelector('.qty-input').value;
    value = parseInt(value);
    if (value < 10) value++;
    document.querySelector('.qty-input').value = value;
})
$(document).ready(function () {
    $('.addtoCartBtn').click(function (e) {
        e.preventDefault();
        var prod_id = $(this).closest('.product_view').find('.prod_id').val();
        var prod_qty = $(this).closest('.product_view').find('.qty-input').val();
        console.log(prod_qty, prod_id);
        var token = $('input[name=csrfmiddlewaretoken]').val();
        $.ajax({
            method: "POST",
            url: "/add-to-cart",
            data: {
                'product_id': prod_id,
                'product_qty': prod_qty,
                csrfmiddlewaretoken: token,
            },
            success: function (response) {
                var tag=response.tag;
                if(tag=="success"){
                    alertify.success(response.status);
                }
                else if(tag=="warning"){
                    alertify.warning(response.status);
                }
                else if(tag=="error"){
                    alertify.error(response.status);
                }
                else{
                    alertify.notify(response.status)
                }
            }
        });
    });
});