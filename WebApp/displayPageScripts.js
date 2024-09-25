document.getElementById("doit").addEventListener('click', function(event) {
    event.preventDefault();
    console.log("button press");
});

document.addEventListener("DOMContentLoaded", async function(){

    const list = await fetchItems();


    
    const listElement = document.getElementById('videoList');
    listElement.innerHTML = '';

    list.forEach(item => {
        const li = document.createElement('li');
        li.textContent = item;

        li.addEventListener('click', function(){
            alert('you clicked on '+item);
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