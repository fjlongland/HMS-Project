
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

document.getElementById('fileInput').addEventListener('change', function(event){
    
    const file = event.target.files[0];

    if (file){
        alert("File chosen: ${file.name}, size: ${file.size} bytes");
    }
});



document.getElementById('uploadButton').addEventListener('click', async function() {
    const fileInput = document.getElementById('fileInput');
    const file = fileInput.files[0];

    if (file) {
        if (file.type !== 'video/mp4') {
            alert('Please select a .mp4 file.');
            return;
        }

        const formData = new FormData();
        formData.append('file', file);

        try {
            const response = await fetch('http://127.0.0.1:8000/posts/upload/', {
                method: 'POST',
                body: formData
            });

            if (response.ok) {
                const result = await response.json();
                alert(`File was uploaded successfully: ${result.filename}`);
            } else {
                alert('File upload unsuccessful');
            }
        } catch (error) {
            console.error('Error:', error);
            alert('An error occurred during the file upload');
        }
    } else {
        alert('Please select a file first.');
    }
});