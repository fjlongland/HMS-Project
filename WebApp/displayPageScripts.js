document.addEventListener("DOMContentLoaded", async function(){

    const list = await fetchItems();

    const listElement = document.getElementById('videoList');
    listElement.innerHTML = '';

    list.forEach(item => {
        const li = document.createElement('li');
        li.textContent = item;

        li.addEventListener('click', async function(){
            const display = document.getElementById("feedback");
            const title = item;
            const token = getJWT()

            try{
                const response = await fetch("http://127.0.0.1:8000/posts/video_id/"+title, {
                    method: "GET",
                    headers:{
                        'Content-Type': 'application/x-www-form-urlencoded',
                        'Authorization': 'Bearer '+token,
                    },
                });

                if (!response.ok){
                    const errorData = await response.json();
                    console.error("error response: ", errorData);
                    throw new Error("Network response was not ok: "+response.status);
                }

                const data = await response.json();
                if (data.post_id){
                    console.log("success: "+ data.post_id);
                    const disp = await getFeedback(data.post_id);
                    display.textContent = disp;
                }
            }
            catch (error){
                console.error("oops something went wrong: ", error);
                alert("Oops something went wrong with selecting the content.");
                return null;
            }
            
        })

        listElement.appendChild(li);
    });

});

function getJWT(){
    const value = '; '+document.cookie;
    const parts = value.split('; JWT=');

    if (parts.length === 2) return parts.pop().split(';').shift();
    return null;
}

async function fetchItems(){
    try{
        const token = getJWT();
        const response = await fetch('http://127.0.0.1:8000/posts/video/', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer '+token,
            },
        });

        if (!response.ok){
            throw new Error("HTTP error! Status: "+response.status);
        }

        const data = await response.json();
        console.log("raw data: ", data);

        const titleArray = data.map(item => item.title);

        console.log("video Title Array: ", titleArray);

        return titleArray;
    }
    catch(error){
        console.error("Error fething items: ", error);
    }
}

async function getFeedback(id){
    try{
        const response = await fetch("http://127.0.0.1:8000/feedback/display/"+id, {
            method: "GET"
        })
        if (!response.ok){
            const errorData = await response.json();
            console.error("error response: ", errorData);
            throw new Error("Network response was not ok: "+response.status);
        }

        const data = await response.json();
        if(data.content){
            console.log("success: ", data.content);
            return data.content;
        }
    }
    catch (error){
        console.error("oops something went wrong: ", error);
        alert("Oops something went wrong with selecting the content.");
        return null;
    }
}