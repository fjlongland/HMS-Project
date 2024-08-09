const btnLogin = document.getElementById("btnLogin");

btnLogin.addEventListener("click", function(){
    alert("Button was clicked!");

    const username = document.getElementById("UserName").value;
    const password = document.getElementById("PassWord").value;

    console.log("Username: ", username);
    console.log("Password: ", password);

    document.getElementById("UserName").value = "";
    document.getElementById("PassWord").value = "";

});