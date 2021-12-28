$(document).ready(function () {
    $(document).on('click', '.decrement-btn', function (e) {
        e.preventDefault();

        var value = $(this).closest('.product_data').find('.qty-input').val();
        value = parseInt(value);
        if (value > 1) value--;
        $(this).closest('.product_data').find('.qty-input').val(value);
    })

    $(document).on('click', '.increment-btn', function (e) {
        e.preventDefault();

        var value = $(this).closest('.product_data').find('.qty-input').val();
        value = parseInt(value);
        if (value < 10) value++;
        $(this).closest('.product_data').find('.qty-input').val(value);
    })

    $(document).on('click', '.addtoCartBtn', function (e) {
        e.preventDefault();
        var prod_id = $(this).closest('.product_view').find('.prod_id').val();
        var prod_qty = $(this).closest('.product_view').find('.qty-input').val();
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
                var tag = response.tag;
                if (tag == "success") {
                    alertify.success(response.status);
                }
                else if (tag == "warning") {
                    alertify.warning(response.status);
                }
                else if (tag == "error") {
                    alertify.error(response.status);
                }
                else {
                    alertify.notify(response.status)
                }
            }
        });
    });
    $(document).on('click', '.changeQuantity', function (e) {
        e.preventDefault();
        var prod_id = $(this).closest('.product_data').find('.prod_id').val();
        var prod_qty = $(this).closest('.product_data').find('.qty-input').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();
        $.ajax({
            method: "POST",
            url: "/update-cart",
            data: {
                'product_id': prod_id,
                'product_qty': prod_qty,
                csrfmiddlewaretoken: token,
            },
            success: function (response) {
                
            }
        });
    });
    $(document).on('click', '.delete-cart-item', function (e) {
        e.preventDefault();
        var prod_id = $(this).closest('.product_data').find('.prod_id').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();
        $.ajax({
            method: "POST",
            url: "/delete-cart-item",
            data: {
                'product_id': prod_id,
                csrfmiddlewaretoken: token,
            },
            success: function (response) {
                alertify.notify(response.status);
                $('#cartdata').load(location.href + " #cartdata")
            }
        });
    });
    $(document).on('click', '.addtoWishlist', function (e) {
        e.preventDefault();
        var prod_id = $(this).closest('.product_view').find('.prod_id').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();
        $.ajax({
            method: "POST",
            url: "/add-to-wishlist",
            data: {
                'product_id': prod_id,
                csrfmiddlewaretoken: token,
            },
            success: function (response) {
                var tag = response.tag;
                if (tag == "success") {
                    alertify.success(response.status);
                }
                else if (tag == "warning") {
                    alertify.warning(response.status);
                }
                else if (tag == "error") {
                    alertify.error(response.status);
                }
                else {
                    alertify.notify(response.status)
                }
            }
        });
    });
    $(document).on('click', '.delete-wishlist-item', function (e) {
        e.preventDefault();
        var prod_id = $(this).closest('.product_data').find('.prod_id').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();
        $.ajax({
            method: "POST",
            url: "/delete-wishlist-item",
            data: {
                'product_id': prod_id,
                csrfmiddlewaretoken: token,
            },
            success: function (response) {
                alertify.notify(response.status);
                $('#whislistdata').load(location.href + " #whislistdata")
            }
        });
    });
});