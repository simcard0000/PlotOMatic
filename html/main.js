const url = "http://plotomatic.com:8585"

const drag_text = document.getElementById('drag-text');
const image_display = document.getElementById('image-display');
const text_display = document.getElementById('text-display');
const file_input = document.getElementById('file-input');

processed_image = false

function init(){
  add_event_listeners();
}

function add_event_listeners() {
  window.addEventListener('drop', (e) => {
    e.stopPropagation();
    e.preventDefault();

	  process_files(e.dataTransfer.files);
  });

  window.addEventListener('dragover', (e) => {
    e.stopPropagation();
    e.preventDefault();

    e.dataTransfer.dropEffect = 'copy';
  });

  file_input.addEventListener('change', (e) => process_files(e.target.files));
}

function process_files(file_list){
	if (!processed_image) {
		processed_image = true;
  	image_file = file_list.item(0);
  	show_image(image_file);
  	post_image(image_file);
	}
}

function show_image(image_file) {
  var url = URL.createObjectURL(image_file);
  image_display.src = url;

	image_display.onload = function(){
		image_display.width = window.innerWidth * 0.5;
	};

	drag_text.parentNode.removeChild(drag_text)
	file_input.parentNode.removeChild(file_input)
}

function on_response(response_text){
	console.log("The server has responded! (200)")
	console.log("Response Text: "+response_text)
  text_display.textContent = response_text;
}

function post_image(image_data){
  xhr = new XMLHttpRequest();
  xhr.open('POST', url);
  xhr.setRequestHeader('Content-Type', "application/octet-stream");
  xhr.send(image_data)
	console.log("POST sent.")
  xhr.onreadystatechange = function () {
    if(xhr.readyState === 4 && xhr.status === 200) {
      on_response(xhr.response);
    }
  }
}

init()
