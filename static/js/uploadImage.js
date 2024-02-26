function uploadImage(event) {
    var input = event.target;
    var container = $('#image-container');
    
    var file = input.files[0];
    var reader = new FileReader();
    
    reader.onload = function(e) {
        container.css('display', 'block')
      container.css('background-image', 'url(' + e.target.result + ')');
      container.css('background-size', 'cover');
      container.css('background-repeat', 'no-repeat'); 
    }
    
    reader.readAsDataURL(file);
}