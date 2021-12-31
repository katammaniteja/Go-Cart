$(document).ready(function(){
    $('.payWithRazorpay').click(function(e){
        e.preventDefault();
        
        var fname=$("[name='fname']").val();
        var lname=$("[name='lname']").val();
        var email=$("[name='email']").val();
        var phone=$("[name='phone']").val();
        var address=$("[name='address']").val();
        var city=$("[name='city']").val();
        var state=$("[name='state']").val();
        var pincode=$("[name='pincode']").val();
        var country=$("[name='country']").val();
        var token = $('input[name=csrfmiddlewaretoken]').val();

        if(fname=="" ||lname=="" ||email=="" ||phone=="" ||address=="" ||city=="" ||state=="" ||pincode=="" ||country=="" ){
            swal("Alert", "All fileds are mandatory", "error");
            return false;
        }
        else{
            $.ajax({
                method:"GET",
                url:"/proceed-to-pay",
                success:function(response){
                    var options = {
                        "key": "rzp_test_dmibPrjPhWqXSd",
                        "amount": response.total_price*100, 
                        "currency": "INR",
                        "name": "Maniteja",
                        "description": "Thanks for shopping",
                        "image": "https://example.com/your_logo",
                        "handler": function (response2){
                            data={
                                "fname":fname,
                                "lname":lname,
                                "email":email,
                                "phone":phone,
                                "address":address,
                                "city":city,
                                "state":state,
                                "pincode":pincode,
                                "country":country,
                                "payment_mode":"Razorpay",
                                "payment_id":response2.razorpay_payment_id,
                                csrfmiddlewaretoken: token,
                            }
                            $.ajax({
                                method:"POST",
                                url:"/place-order",
                                data:data,
                                success:function(response3){
                                    swal("Success", response3.status, "success")
                                    .then(()=>{
                                        window.location.href="/my-orders"
                                    });
                                }
                            });
                        },
                        "prefill": {
                            "name": fname+" "+lname,
                            "email": email,
                            "contact": phone
                        },
                        "theme": {
                            "color": "#3399cc"
                        }
                    };
                    var rzp1 = new Razorpay(options);
                    rzp1.open();
                }
            });
        }
    })
});