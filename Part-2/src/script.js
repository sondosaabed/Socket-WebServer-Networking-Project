function submitForm(event) {
    /*
        This is a function crerated to get the ID from the Form 
        and send this using the API
        Args:
            event
        Returns:
            Nothing
    */
    
    event.preventDefault(); 

    /*
        Get the Input value from the Feild Form
    */
    const studentIdInput = document.getElementById("student_id");
    const studentId = studentIdInput.value;

    fetch("http://127.0.0.1:9955", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ student_id: studentId }),
    }).then((response) => response.json()).then((data) => {
            /*
                Handling the Response from the server
            */
            console.log(data);

        })
        .catch((error) => {
            console.error("Error:", error);
        });
}