document.getElementById('uploadButton').addEventListener('click', async function(){
    const fileInput = document.getElementById('fileInput');
    const file = fileInput.files[0];

    if (file) {
        if (file.type !== 'video/mp4'){
            alert('please select a .mp4 file.');
            return;
        }

        const formData = new FormData();
        formData.append('file', file);

        const token = getJWT();

        try{
            const response = await fetch('http://127.0.0.1:8000/posts/upload/', {
                method: 'POST',
                headers: {
                    'Authorization': 'Bearer '+ token,
                },
                body: formData
            });

            if (response.ok){
                const result = await response.json();
                alert('File was uploaded successfuly!');
            }
            else{
                const errorText = await response.text();
                alert('file upload was unsuccessful :C' + errorText);
            }
        }
        catch (error){
            console.error('Error: ', error);
            alert('an error occured during file upload.');
        }
    }
    else{
        alert('please select a file first.')
    }
});

function getJWT(){
    const value = '; '+document.cookie;
    const parts = value.split('; JWT=');

    if (parts.length === 2) return parts.pop().split(';').shift();
    return null;
}