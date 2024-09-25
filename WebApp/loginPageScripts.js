

document.getElementById('btnLogin').addEventListener('click', async function(){
    

    const userName = document.getElementById('UserName').value;
    const userPassword = document.getElementById('PassWord').value;

    const token = await loginUser(userName, userPassword);

    if(token){
        document.cookie = "JWT="+token;
        console.log(document.cookie)
    }

    window.location.href = "./displayPAge.html"
    
});
async function loginUser(username, password){

    try{
        const formData = new URLSearchParams();
        formData.append('username', username);
        formData.append('password', password);

        const response = await fetch('http://127.0.0.1:8000/login/',{
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: formData
        });

        if (!response.ok){
            throw new Error("Network response was not ok");
        }

    const data = await response.json();

    if (data.token){
        console.log(data.token)
        return data.token;
    }
 
    } 
    catch (error){
        console.error("there was an error validating user:", error);
        alert("an error occured while trying to validate user.")
        return null;
    }
}

document.getElementById('fileInput').addEventListener('change', function(event){
    
    const file = event.target.files[0];

    if (file){
        alert("File chosen: ${file.name}, size: ${file.size} bytes");
    }
});

document.getElementById('uploadButton').addEventListener('click', async function() {
    const fileInput = document.getElementById('fileInput');
    const file = fileInput.files[0];

    if (file) {
        if (file.type !== 'video/mp4') {
            alert('Please select a .mp4 file.');
            return;
        }

        const formData = new FormData();
        formData.append('file', file);

        //const token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjozLCJleHAiOjE3MjU1Mzc1NzF9.jmBpiyPP5OJcscbAmMMqR6HjhtENzPIH5lkmLyEygs4"
        var token = await loginUser("user1", "user1")

        try {
            const response = await fetch('http://127.0.0.1:8000/posts/upload/', {
                method: 'POST',
                headers: {
                    'Authorization': 'Bearer '+token,
                }, 
                body: formData
            });

            if (response.ok) {
                const result = await response.json();
                alert(`File was uploaded successfully: ${result.filename}`);
            } else {
                alert('File upload unsuccessful');
            }
        } catch (error) {
            console.error('Error:', error);
            alert('An error occurred during the file upload');
        }
    } else {
        alert('Please select a file first.');
    }
});

document.getElementById("videoList").addEventListener("DOMContentLoaded", async function(){

    const items = await fetch("http://127.0.0.1:8000/posts/video/", {
        method: 'GET',
        headers: {
            'Authorization': 'Bearer'+document.cookie
        }
    })
});

function getJWT(){
    const value = '; '+document.cookie;
    const parts = value.split('; JWT=');

    if (parts.length === 2) return parts.pop().split(';').shift();
    return null;
}

document.getElementById("doit").addEventListener('click', function(){
const token = getJWT();

console.log("button pressed")
console.log(token);

})