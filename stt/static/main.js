if (! "webkitSpeechRecognition" in window) {
    alert("Speech Recognition Not Available")
  }
  
  let SpeechRecognition = window.SpeechRecognition || webkitSpeechRecognition;
  let SpeechGrammarList = window.SpeechGrammarList || webkitSpeechGrammarList;
  let SpeechRecognitionEvent = window.SpeechRecognitionEvent || webkitSpeechRecognitionEvent;
  
  let recognition = new SpeechRecognition();
  
  recognition.continuous = true;
  recognition.interimResults = true;
  recognition.lang = 'id-ID';
  
  recognition.onError = () => {
    console.log('Error...')
  };
  
  recognition.onresult = function (event) {
    console.log(event.results)
  
    let textResult = ''
    for (let i = 0; i < event.results.length; i++) {
      textResult += event.results[i][0].transcript
    }
  
    console.log(textResult)
    document.querySelector("#result").innerHTML = textResult
    
    // Show the save transcript button when the user stops speaking
    let saveButton = document.querySelector("#save");
    if (!saveButton) {
      saveButton = document.createElement("button");
      saveButton.id = "save";
      saveButton.textContent = "Save Transcript";
      saveButton.style = "font-size: 1rem; padding: 0.5rem 1rem; border-radius: 4px; border: none; color: white; background-color: #2196f3; cursor: pointer; margin: 1rem;"
      saveButton.onclick = () => {
        // Get the text content of the result element
        let transcript = document.querySelector("#result").textContent;
    
        // Create a new Blob object with the transcript text
        let blob = new Blob([transcript], {type: "text/plain;charset=utf-8"});
    
        // Use the saveAs function to save the blob as a text file
        saveAs(blob, "transcript.txt");
      };
      
      let resultContainer = document.querySelector("#result-container");
      resultContainer.appendChild(saveButton);
    }
  };
  
  document.querySelector("#start").onclick = () => {
    // Reset the text content of the result element
    document.querySelector("#result").textContent = "";
    
    // Remove the save transcript button
    let saveButton = document.querySelector("#save");
    if (saveButton) {
      saveButton.remove();
    }
    
    // Start the recognition
    recognition.start();
  };
  
  document.querySelector("#stop").onclick = () => {
    recognition.stop();
  };