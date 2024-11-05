function registrar(){
    const user = document.getElementById("user").value
    const password = document.getElementById("password").value

    var object = {user:user, password:password}

    // Llamada a la API con el método GET
    fetch("https://web-test-n7rj.onrender.com/registrar", {
        method : "POST",
        headers : {"Content-Type": "application/json"},
        body: JSON.stringify(object)
    })
    .then(response => {
        return response.json()
    })
    .then(response => {
        const success = response.success
        const message = response.message

        console.log(success)

        if (success){
            console.log("exito")
            document.getElementById("estado").textContent = message
        }else{
            console.log("fracaso")
            document.getElementById("estado").textContent = message
        }
    })



}

function entrar(){
    const user = document.getElementById("user").value
    const password = document.getElementById("password").value

    var object = {user:user, password:password}

    // Llamada a la API con el método GET
    fetch("https://web-test-n7rj.onrender.com/entrar", {
        method : "POST",
        headers : {"Content-Type": "application/json"},
        body: JSON.stringify(object)
    })
    .then(response => {
        return response.json()
    })
    .then(response => {
        const success = response.success
        const message = response.message

        console.log(success)

        if (success){
            console.log("exito")
            document.getElementById("estado").textContent = message
        }else{
            console.log("fracaso")
            document.getElementById("estado").textContent = message
        }
    })



}