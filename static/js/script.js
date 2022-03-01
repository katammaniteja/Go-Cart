$(document).ready(function () {
    // Search Products
    // https://jqueryui.com/autocomplete/
    $(function () {
        var availableTags = [];
        $.ajax({
            method: "GET",
            url: "/items_list",
            success: function (response) {
                availableTags = response;
                startAutoComplete(availableTags);
            }
        });
        function startAutoComplete(availableTags) {
            $("#search_item").autocomplete({
                source: availableTags
            });
        }
    });

    // On changing the quantity of item required in input filed
    $(document).on('blur', '.qty-input', function (e) {
        var max_value = $(this).closest('.product_data').find('.max_value').val();
        var value = $(this).closest('.product_data').find('.qty-input').val();
        $(this).closest('.product_data').find('.qty-input').val(Math.min(max_value, Math.max(value, 1)));
    })

    // on decreasing the quatity of product required
    $(document).on('click', '.decrement-btn', function (e) {
        e.preventDefault();

        var value = $(this).closest('.product_data').find('.qty-input').val();
        value = parseInt(value);
        if (value > 1) value--;
        $(this).closest('.product_data').find('.qty-input').val(value);
    })

    // on increasing the quatity of product required
    $(document).on('click', '.increment-btn', function (e) {
        e.preventDefault();
        var max_value = $(this).closest('.product_data').find('.max_value').val();
        var value = $(this).closest('.product_data').find('.qty-input').val();
        value = parseInt(value);
        if (value < max_value) {
            value++;
        }
        else if (max_value == 0) {
            swal("Out of stock");
        }
        else {
            swal(`Only ${max_value} quantity are available`);
        }
        $(this).closest('.product_data').find('.qty-input').val(value);
    });

    // Adding the product to the cart
    $(document).on('click', '.addtoCartBtn', function (e) {
        e.preventDefault();
        var prod_id = $(this).closest('.product_data').find('.prod_id').val();
        var prod_qty = $(this).closest('.product_data').find('.qty-input').val();
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
                    $('#navbar').load(location.href + " #navbar");
                }
                else if (tag == "warning") {
                    alertify.warning(response.status);
                }
                else if (tag == "error") {
                    alertify.error(response.status);
                }
                else {
                    alertify.notify(response.status);
                }
            }
        });
    });

    // Updating the item quantity from cart to database
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

    // Deleting the item in the cart
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
                $('#cartdata').load(location.href + " #cartdata");
                $('#navbar').load(location.href + " #navbar");
            }
        });
    });

    // Adding items to our wishlist
    $(document).on('click', '.addtoWishlist', function (e) {
        e.preventDefault();
        var prod_id = $(this).closest('.product_data').find('.prod_id').val();
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
                    $('#navbar').load(location.href + " #navbar");
                }
                else if (tag == "warning") {
                    alertify.warning(response.status);
                }
                else if (tag == "error") {
                    alertify.error(response.status);
                }
                else {
                    alertify.notify(response.status);
                }
            }
        });
    });

    // Deleting the item from wishlist
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
                $('#whislistdata').load(location.href + " #whislistdata");
                $('#navbar').load(location.href + " #navbar");
            }
        });
    });
});