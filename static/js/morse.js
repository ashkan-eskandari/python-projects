const morseForm = document.getElementById("morse_form");
const morseInput = document.getElementById("floatingInput");
const morseOutput = document.getElementById("floatingMorse");


morseForm.addEventListener("submit", function (e) {
    e.preventDefault();

    // Fetch morse_output from the server
    fetch('/morse', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: new URLSearchParams({
            'text': morseInput.value,
        }),
    })
        .then(response => response.json())
        .then(data => {
            // Update the HTML content with the fetched morse_output

            morseOutput.innerText = data.morse_output

        })
        .catch(error => console.error('Error:', error));
});
const resetButton = document.getElementById("resetMorse");
resetButton.addEventListener("click", function (e) {
    e.preventDefault();

    // Reset the form and clear the morse_output content
    morseForm.reset();
    morseOutput.innerText = "";
})





