

document.getElementById('btnLogin').addEventListener('click', async function(){
    

    const userName = document.getElementById('UserName').value;
    const userPassword = document.getElementById('PassWord').value;

    const token = await loginUser(userName, userPassword);

    if(token){
        document.cookie = "JWT="+token;
        console.log(document.cookie)
    }

    window.location.href = "./homePage.html"
    
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