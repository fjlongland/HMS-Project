document.addEventListener("DOMContentLoaded", async function(){

    const list = await fetchItems();

    const listElements = document.getElementById('assList');
    listElements.innerHTML = '';

    list.forEach(item => {
        const li = document.createElement('li');
        li.textContent = item;

        li.addEventListener('click', async function(){
            const assTitle = item;
            document.cookie = "assignmentTitle="+assTitle+"; path=/";
            const title = getTitle();
            const token = getJWT();
            try{
                const formdata = new URLSearchParams();
                formdata.append("title", title)
                const response = await fetch("http://127.0.0.1:8000/assignment/content/"+title, {
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
                if (data.content){
                    console.log("success: "+ data.content);
                    const display = document.getElementById("displayContent");
                    display.textContent = data.content;
                    const id = data.ass_id;
                    document.cookie = "ass_id="+id+"; path=/";
                    console.log(document.cookie);
                }
            }
            catch (error){
                console.error("oops something went wrong: ", error);
                alert("Oops something went wrong with displaying the content.");
                return null;
            }
        })

        listElements.appendChild(li);
    });
});


function getTitle(){
    const value = "; "+document.cookie;
    const parts = value.split("; assignmentTitle=");
    if (parts.length === 2) return parts.pop().split(";").shift();
    return null;
}


function getJWT(){

    const value = '; '+document.cookie;
    const parts = value.split('; JWT=');

    if (parts.length === 2) return parts.pop().split(';').shift();
    return null;
}

async function fetchItems(){
    try{

        const token = getJWT();
        const response = await fetch("http://127.0.0.1:8000/assignment/list/", {
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

        const arr = data.map(item => item.title);
        console.log("full array: ", arr);

        return arr;
    }
    catch(error){
        console.error("Error fething items: ", error);
    }
}