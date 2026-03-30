async function sendMessage(){

    let input = document.getElementById("user-input");
    let message = input.value;

    if(message === "") return;

    let chatBox = document.getElementById("chat-box");

    chatBox.innerHTML += `<div class="message user">${message}</div>`;

    input.value = "";

    let response = await fetch("http://127.0.0.1:8000/chat",{
        method:"POST",
        headers:{
            "Content-Type":"application/json"
        },
        body:JSON.stringify({
            message:message
        })
    });

    let data = await response.json();

    chatBox.innerHTML += `<div class="message bot">${data.response}</div>`;

    chatBox.scrollTop = chatBox.scrollHeight;
}