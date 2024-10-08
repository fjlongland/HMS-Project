document.getElementById("btnCreate").addEventListener('click', async function(){
    const title = document.getElementById("assTitle").value;
    const content = document.getElementById("assContent").value;
    const token = getJWT();

    try{
        const formdata = new URLSearchParams();
        formdata.append('title', title);
        formdata.append('content', content)

        const response = await fetch("http://127.0.0.1:8000/assignment", {
            method: "POST",
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'authorization': "Bearer "+ token
            },
            body: formdata
        });

        if (!response.ok){
            const errorData = await response.json();
            console.error("Error response: ", errorData);
            throw new Error("Network response was not ok: "+ response.statusText);
        }

        const data = await response.json();

        if(data.ass_id){
            alert("Assignment was created successfuly!")
        }
    }
    catch (error){
        console.error("there was an error creating assignment:", error);
        alert("an error occured while trying to create assignment.")
        return null;

    }

    function getJWT(){
        const value = '; '+document.cookie;
        const parts = value.split('; JWT=');
    
        if (parts.length === 2) return parts.pop().split(';').shift();
        return null;
    }
})