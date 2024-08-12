document.getElementById('btnLogin').addEventListener('click', function(){
    
    const userInput = document.getElementById('UserName').value;

    fetch('http://127.0.0.1:8000/test', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({input: userInput})
    })
    .then(response => response.json())
    .then(data=>{
        console.log('Success', data);
    })
    .catch((error)=>{
        console.error('Error:', error);
    });
});