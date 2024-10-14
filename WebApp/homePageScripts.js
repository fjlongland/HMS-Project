document.addEventListener("DOMContentLoaded", async function(){

    console.log("Im Working");

    const userType = await fetchType();
    document.cookie = "userType="+userType+"; path=/";

    const heading = document.getElementById("user_type");
    const assButton = document.getElementById("btnAssignments");

    if(userType){
        heading.textContent = "user type: "+userType;
    }
    else{
        heading.textContent = "Welcome guest"
    }

    if (userType == "ADMIN"){
        alert("Welcome Sir");
    }

    if (userType == "PROFESSOR"){
        

    }

    if (userType == "STUDENT"){
        assButton.style.display = 'none';
    }

    async function fetchType(){
        const token = getJWT();
        try{
            const response = await fetch('http://127.0.0.1:8000/users/type/',{
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': 'Bearer '+token,
                },
            });
    
            if (!response.ok){
                throw new Error("HTTP error! Atatus: "+response.status);
            }
    
            const data = await response.json();
            console.log("raw data: ", data);
            return data.user_type;
        }
        catch(error){
            console.error("Error fetching user type: ", error);
        }
    }

    function getJWT(){
        const value = '; '+document.cookie;
        const parts = value.split('; JWT=');
    
        if (parts.length === 2) return parts.pop().split(';').shift();
        return null;
    }
});

