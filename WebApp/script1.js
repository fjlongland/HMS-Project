document.getElementById("btnSubmit").addEventListener("click", async function(event){
    event.preventDefault();

    const newUserName = document.getElementById("newUserName").value;
    const newPassword = document.getElementById("newPassword").value;
    const newEmail = document.getElementById("newEmail").value;

    let selectedOption;
    const radios = document.getElementsByName("user_type");

    for (let radio of radios){
        if (radio.checked){
            selectedOption = radio.value;
            break;
        }
    }

    if (!selectedOption){
        selectedOption = "no user type selected!";
    }

    document.getElementById("result").innerHTML = 
    "Username: " + newUserName + "<br>" +
    "Password: " + newPassword + "<br>" +
    "Email: " + newEmail + "<br>" +
    "Type: " + selectedOption;

    try{
        const formData = new URLSearchParams();
        formData.append('username', newUserName);
        formData.append('password', newPassword);
        formData.append('user_email', newEmail);
        formData.append('user_type', selectedOption);

        
        const response = await fetch("http://127.0.0.1:8000/users", {
            method: "POST",
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: formData
        });

        if (!response.ok){
            const errorData = await response.json();
            console.error("Error response: ", errorData);
            throw new Error("Network response was not ok: "+ response.statusText);
        }

        const data = await response.json();

        if (data.user_id){
            console.log(data.user_id)
            alert("user was created successfully!")

        }
    }
    catch (error){
        console.error("there was an error creating user:", error);
        alert("an error occured while trying to create user.")
        return null;
    }
});