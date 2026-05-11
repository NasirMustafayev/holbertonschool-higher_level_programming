fetch('https://hellosalut.stefanbohacek.com/?lang=fr')
    .then(response => response.json())
    .then(data => {
        const helloElement = document.getElementById('hello');
        helloElement.textContent = data.hello;
    })
    .catch(error => console.error('Error fetching data:', error));
