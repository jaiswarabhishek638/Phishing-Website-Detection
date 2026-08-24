document.getElementById('url-form').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const url = document.getElementById('url-input').value;
    const resultElement = document.getElementById('result');
    
    resultElement.textContent = 'Checking...';
    
    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ url: url })
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            resultElement.textContent = `Error: ${data.error}`;
            resultElement.style.color = 'red';
        } else {
            resultElement.textContent = `Prediction: ${data.prediction}`;
            if (data.prediction === 'Phishing') {
                resultElement.style.color = 'red';
            } else {
                resultElement.style.color = 'green';
            }
        }
    })
    .catch(error => {
        resultElement.textContent = 'An error occurred.';
        resultElement.style.color = 'red';
        console.error('Error:', error);
    });
});
