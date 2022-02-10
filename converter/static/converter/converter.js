function TextConvert() {
    var x = CKEDITOR.instances['id_body'].getData();
    var y = document.getElementById('htmldata');
    y.innerHTML = x;
}