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
    
    // Get the student ID from the form
    var studentId = document.getElementById("student_id").value;

    // Perform any additional client-side validation if needed

    // Send the student ID to the server using your Python client script
    sendStudentIdToServer(studentId);
}

function sendStudentIdToServer(studentId) {
    // You can use XMLHttpRequest or fetch API to send data to the server
    // Example using fetch:
    fetch('/server.py', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ student_id: studentId }),
    })
    .then(response => response.json())
    .then(data => {
        // Handle the response from the server if needed
        console.log(data);
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
