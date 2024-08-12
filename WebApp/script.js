
//add event listener to the login button
document.getElementById('btnLogin').addEventListener('click', function(){
    
    //saves the value in the field into a variable
    const username = document.getElementById('UserName').value;
    const userPW = document.getElementById('PassWord').value;
    //starts the api call by specifying the url and the method(POST)
    fetch('http://127.0.0.1:8000/test', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        //changes the input to correct datatype
        body: JSON.stringify({
            username: username,
            password: userPW
        })
    })
    //sends the api response
    .then(response => response.json())
    .then(data=>{
        console.log('Success', data);
    })
    //catch for when errors occure
    .catch((error)=>{
        console.error('Error:', error);
    });
});