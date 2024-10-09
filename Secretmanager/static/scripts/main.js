// static/scripts/main.js

// Simple script to convert the navbar to a hamburger menu
// in case the user is on phone, tablet or any smaller screen
document.addEventListener('DOMContentLoaded', () => {
    const menuToggle = document.getElementById('menu-toggle');
    const navLinks = document.querySelector('.nav-links');

    menuToggle.addEventListener('click', () => {
        navLinks.classList.toggle('active');
    });
});

function toggleChat() {
    const chatWindow = document.getElementById('chatbot-window');
    chatWindow.classList.toggle('active');
}

document.getElementById('send-message').addEventListener('click', async function() {
    const userInput = document.getElementById('chatbot-input').value;
    if (userInput.trim() === "") return;

    displayMessage(userInput, 'user');

    try {
        const response = await fetch('http://localhost:5000/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ message: userInput }),
        });

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const data = await response.json();
        displayMessage(data.message, 'bot');
    } catch (error) {
        console.error('There was a problem with the fetch operation:', error);
        displayMessage("Error: Unable to get a response from the bot.", 'bot');
    }

    document.getElementById('chatbot-input').value = "";
});

function displayMessage(message, sender) {
    const chatWindow = document.querySelector('.chat-messages');  // Use class selector correctly
    const messageElement = document.createElement('div');

    // Add appropriate class depending on who sent the message
    if (sender === 'user') {
        messageElement.classList.add('user-message');
    } else if (sender === 'bot') {
        messageElement.classList.add('bot-message');
    }

    // Set the message content
    messageElement.textContent = message;

    // Append the message to the chat window
    chatWindow.appendChild(messageElement);

    // Optionally scroll to the latest message
    chatWindow.scrollTop = chatWindow.scrollHeight;
}
