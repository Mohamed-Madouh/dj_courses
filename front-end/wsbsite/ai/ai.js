  function toggleDarkMode() {
    var body = document.body;
    var modeIcon = document.getElementById("mode-icon");
    
    body.classList.toggle("dark-mode");
    
    // Toggle icon between moon and sun
    if (body.classList.contains("dark-mode")) {
      modeIcon.classList.remove("fa-moon");
      modeIcon.classList.add("fa-sun");
    } else {
      modeIcon.classList.remove("fa-sun");
      modeIcon.classList.add("fa-moon");
    }
  }
  




  function toggleNotificationMenu() {
    var menu = document.getElementById("notificationMenu");
    if (menu.style.display === "block") {
      menu.style.display = "none";
    } else {
      menu.style.display = "block";
    }
  }
  
  // Close the notification menu if clicked outside of it
  window.onclick = function(event) {
    var menu = document.getElementById("notificationMenu");
    if (event.target !== menu && !event.target.closest('.notification-icon')) {
      menu.style.display = "none";
    }
  }
  


  var audioContext = new (window.AudioContext || window.webkitAudioContext)();
  var isRecording = false;
  
  function toggleRecording() {
    if (!isRecording) {
      startRecording();
    } else {
      stopRecording();
    }
  }
  
  function startRecording() {
    navigator.mediaDevices.getUserMedia({ audio: true })
      .then(function(stream) {
        var mediaRecorder = new MediaRecorder(stream);
        var chunks = [];
  
        mediaRecorder.ondataavailable = function(event) {
          chunks.push(event.data);
        }
  
        mediaRecorder.onstop = function() {
          var blob = new Blob(chunks, { type: 'audio/wav' });
          var audioURL = window.URL.createObjectURL(blob);
          var audio = new Audio(audioURL);
          audio.play();
        }
  
        mediaRecorder.start();
        isRecording = true;
      })
      .catch(function(error) {
        console.error('Error accessing microphone:', error);
      });
  }
  
  function stopRecording() {
    isRecording = false;
  }

     function scrollToTop() {
    window.scrollTo({
        top: 0,
        behavior: "smooth"
    });
}

window.addEventListener("scroll", function() {
    var backToTopBtn = document.getElementById("backToTopBtn");
    if (document.body.scrollTop > 20 
    || document.documentElement.scrollTop > 20) {
        backToTopBtn.style.display = "block";
    } else {
        backToTopBtn.style.display = "none";
    }
});
