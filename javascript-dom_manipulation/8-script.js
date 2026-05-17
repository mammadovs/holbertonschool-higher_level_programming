document.addEventListener('DOMContentLoaded', function () {
  const helloElement = document.querySelector('#hello');

  fetch('https://hellosalut.stefanbohacek.com/?lang=fr')
    .then(function (response) {
      return response.json();
    })
    .then(function (data) {
      helloElement.textContent = data.hello;
    });
});
