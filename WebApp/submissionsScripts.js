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

        li.addEventListener('click', function(){
            window.location.href = ""
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