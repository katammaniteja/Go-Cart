$(document).ready(function(){
    $('.payWithRazorpay').click(function(e){
        e.preventDefault();
        
        var fname=$("[name='fname']").val()
        var lname=$("[name='lname']").val()
        var email=$("[name='email']").val()
        var phone=$("[name='phone']").val()
        var address=$("[name='address']").val()
        var city=$("[name='city']").val()
        var state=$("[name='state']").val()
        var pincode=$("[name='pincode']").val()
        var country=$("[name='country']").val()


        if(fname=="" ||lname=="" ||email=="" ||phone=="" ||address=="" ||city=="" ||state=="" ||pincode=="" ||country=="" ){
            swal("Alert", "All fileds are mandatory", "error");
            return false;
        }
        else{

            $.ajax({
                method:"GET",
                url:"/proceed-to-pay",
                success:function(response){
                   // console.log(response);
                    var options = {
                        "key": "rzp_test_dmibPrjPhWqXSd", // Enter the Key ID generated from the Dashboard
                        "amount": response.total_price*100, // Amount is in currency subunits. Default currency is INR. Hence, 50000 refers to 50000 paise
                        "currency": "INR",
                        "name": "Maniteja",
                        "description": "Thanks for shopping",
                        "image": "https://example.com/your_logo",
                        // "order_id": "order_9A33XWu170gUtm", //This is a sample Order ID. Pass the `id` obtained in the response of Step 1
                        "handler": function (response){
                            alert(response.razorpay_payment_id);
                            // alert(response.razorpay_order_id);
                            // alert(response.razorpay_signature)
                        },
                        "prefill": {
                            "name": fname+" "+lname,
                            "email": email,
                            "contact": phone
                        },
                        // "notes": {
                        //     "address": "Razorpay Corporate Office"
                        // },
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
})