$(()=>{
console.log('I AM READY')

$(".view-comment").click((e)=>{

  $.ajax(
    {
      type:'GET',
      url:'/comment/6',
      data:{},
      success:(data)=>{
        // alert(data)
        console.log(data.comments)
        payload=data.comments
        comments=''
        console.log(data)
        for(i=0;i<payload.length;i++){
          console.log(payload[i])
          comments+=`<p><strong>${payload[i].user}</strong></p><li>${payload[i].comment}</li>`
        }
        $("#comments").html(comments);
        
        $("#popupimage").html(`<img src="${data.imageurl}" alt="Instagram image" class="img-fluid">`);
      }
    }
  );
  return false;
})





});


// document.addEventListener('DOMContentLoaded',()=>{

//   console.log('noew loaded')
// });