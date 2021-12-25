document.querySelector('.decrement-btn').addEventListener('click',(event)=>{
    event.preventDefault();
    var value=document.querySelector('.qty-input').value;
    value=parseInt(value);
    if(value>1) value--;
    document.querySelector('.qty-input').value=value;
})
document.querySelector('.increment-btn').addEventListener('click',(event)=>{
    event.preventDefault();
    var value=document.querySelector('.qty-input').value;
    value=parseInt(value);
    if(value<10) value++;
    document.querySelector('.qty-input').value=value;
})