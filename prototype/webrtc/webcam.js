
(function(){
  var mediaOptions = { audio: false, video: true };

  if (!navigator.getUserMedia) {
      navigator.getUserMedia = navigator.getUserMedia || navigator.webkitGetUserMedia || navigator.mozGetUserMedia || navigator.msGetUserMedia;
  }

  if (!navigator.getUserMedia){
    return alert('getUserMedia not supported in this browser.');
  }

  navigator.getUserMedia(mediaOptions, success, function(e) {
    console.log(e);
  });

  function success(stream){
		var video = document.querySelector("#player");
    video.srcObject = stream;
		document.getElementById('button').addEventListener('click', function(ev){
			show_image(takepicture(video));
			ev.preventDefault();
		}, false);
  }
	function takepicture(video){

		canvas = document.getElementById('canvas');
		canvas.width = video.srcObject.width + 100;
		canvas.height = video.srcObject.height + 100;
		canvas.getContext('2d').drawImage(video, 0, 0, video.srcObject.width, video.srcObject.height);
	    // This is the image we need to upload
	    var data = canvas.toDataURL('image/png');

	    return data;
		}
		function show_image(url) {
		  document.getElementById('photo').src = url;
		}
})();
