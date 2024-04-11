//import * as io from 'socket.io-client';

// Import the necessary modules

// Connect to the Socket.IO server
const io = require('socket.io')(server, {
    cors: {
      origin: 'http://127.0.0.1:5000',
    },
  });
  
socket.on('connect', () => {
    console.log('Connected to the server');
});

socket.on('disconnect', () => {
    console.log('Disconnected from the server');
}); 

socket.on('message', (data) => {
    console.log(data);
    sendMessage(data);
});

// Function to add messages to the UI
function addMessage(message) {
    const messageElement = document.createElement("div");
    messageElement.innerText = message;
    document.getElementById("messages").appendChild(messageElement);
}

// Function to send a message
function sendMessage() {
    const inputElement = document.getElementById("message-input");
    const message = inputElement.value.trim();

    if (message !== "") {
        // Emit the "new_message" event to the server
        socket.emit("new_message", { message });

        // Clear the input field
        inputElement.value = "";
    }
}

// Event listener for the "send" button
document.getElementById("send").addEventListener("click", sendMessage);

// Event listener for the "Enter" key press
document.getElementById("message-input").addEventListener("keydown", (event) => {
    if (event.key === "Enter") {
        event.preventDefault();
        sendMessage();
    }
});

// Event listener for the "new_message" event from the server
socket.on("new_message", (data) => {
    const message = data.message;
    addMessage(message);
});