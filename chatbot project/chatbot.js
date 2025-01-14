// We make first some sample responded

// We make a variable that will link with input
// We make a variable that will link with response
// We make a variable that will link with all content

const chatBox = document.getElementById("chat-box");
const userInput = document.getElementById("user-input");
const sendBtn = document.getElementById("send-btn");


// make repsonsed on saying hi

const responses = { "hello": "Hi there! How can I help you?",
     "how are you": "I'm just a bot, but I'm functioning as expected!",
    "weather":  "Good day! How can I help you with the weather?",
      "bye": "Goodbye! Have a great day!" ,
      "tell my name": "hi dont know your name sorry"
    };


// When i click button from html javascript should trigger a function to take input and to return back output to 
function handleInput() {
    const userInput = document.getElementById("user-input").value;
    const botResponse = responses[userInput.toLowerCase()] || "I'm sorry, I don't understand.";
    chatBox.innerHTML += `<p><strong>You:</strong> ${userInput}</p><p><strong>Bot:</strong> ${botResponse}</p>`;
    userInput.value = "";
}

sendBtn.addEventListener("click", handleInput);


