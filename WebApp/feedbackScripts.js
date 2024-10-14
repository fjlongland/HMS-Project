document.addEventListener("DOMContentLoaded", async function(){
    const video = document.getElementById("vidPlayer");
    const source = document.getElementById("videoSource");
    const token = getJWT();
    const id = getCookie("post_id");

    const response = await fetch("http://127.0.0.1:8000/posts/video_url/"+id, {
        method: "GET",
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': 'Bearer '+token
        },
    });

    if(!response.ok){
        throw new Error("HTTP error! Status: "+response.status);
    }

    const data = await response.json();
    console.log("raw data: "+ JSON.stringify(data));

    if (data.post_url){
        const usable_url = JSON.stringify(data.post_url);
        console.log(usable_url);

        source.src = data.post_url;

        video.load();
        video.play();
    }
    else {
        console.log("wtf");
    }
})

document.getElementById("btnSubmit").addEventListener('click', async function(){
    const feedback = document.getElementById("txtFeedback").value;
    const post_id = getCookie("post_id");
    const token = getJWT();

    try{
        const formdata = new URLSearchParams();
        formdata.append("content", feedback);
        formdata.append("post_id_fk", post_id);

        const response = await fetch("http://127.0.0.1:8000/feedback",{
            method: "POST",
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'Authorization': 'Bearer '+token,
            },
            body: formdata
        });

        if(!response.ok){
            const errorData = await response.json();
            console.error("Error response: ", errorData);
            throw new Error("Network response was not ok: "+ response.statusText);
        }

        const data = await response.json();

        if (data.feedback_id){
            console.log(data.feedback_id);
            alert("Feedback posted succesfully!");
        }
    }
    catch (error){
        console.error("there was an error creating feedback:", error);
        alert("an error occured while trying to post feedback.")
        return null;
    }
})

function getJWT(){

    const value = '; '+document.cookie;
    const parts = value.split('; JWT=');

    if (parts.length === 2) return parts.pop().split(';').shift();
    return null;
}
function getCookie(name){
    const value = "; "+document.cookie;
    const parts = value.split("; "+name+"=");

    if (parts.length === 2){
        return parts.pop().split(";").shift();
    }
    return null;
}