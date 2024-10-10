document.addEventListener("DOMContentLoaded", async function(){
    const heading = document.getElementById("heading2");
    const title = getCookie('assignmentTitle');

    heading.textContent = "Submissions for: "+title;

    const list = await fetchItems();

    const listElements = document.getElementById("displayList");
    listElements.innerHTML = '';

    list.forEach(item => {
        const li = document.createElement('li');
        li.textContent = item;

        li.addEventListener('click', async function(){
            try{
                const token = getJWT();
                const post_title = item;
                const response = await fetch("http://127.0.0.1:8000/posts/video_id/"+post_title, {
                    method: "GET",
                    headers: {
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
                if(data.post_id){
                    console.log("Post is: "+ data.post_id);
                    const pid = data.post_id;
                    document.cookie = "post_id="+pid+"; path=/";
                    window.location.href = "./feedback.html"
                }
                
            }
            catch (error){
                console.error("oops something went wrong: ", error);
                alert("Oops something went wrong with selecting the content.");
                return null;
            }
        });
        listElements.appendChild(li);
    });
    

});
function getCookie(name){
    const value = "; "+document.cookie;
    const parts = value.split("; "+name+"=");

    if (parts.length === 2){
        return parts.pop().split(";").shift();
    }
    return null;
}

async function fetchItems(){
    try{
        const id = getCookie("ass_id")
        const token = getJWT();
        const response = await fetch("http://127.0.0.1:8000/posts/video/"+id, {
            method: "GET",
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer '+token,
            },
        });

        if(!response.ok){
            throw new Error("HTTP error! Status: "+response.status);
        }
        const data = await response.json();
        console.log("raw data: ", data);

        const arr = data.map(item=> item.title);
        console.log("full array: ", arr);
        
        return arr;
    }
    catch(error){
        console.error("Error fetching items: ", error)

    }
}
function getJWT(){

    const value = '; '+document.cookie;
    const parts = value.split('; JWT=');

    if (parts.length === 2) return parts.pop().split(';').shift();
    return null;
}