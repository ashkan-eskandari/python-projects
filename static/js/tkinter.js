function openTkinterWindow() {
        // Make an AJAX request to the Flask endpoint
        fetch('/open_tkinter_window', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({}),
        })
            .then(response => response.json())
            .then(data => {
                // Log the response from the Flask endpoint
                console.log(data);

                // You can add additional logic here to handle the response as needed
            })
            .catch(error => {
                console.error('Error:', error);
            });
    }