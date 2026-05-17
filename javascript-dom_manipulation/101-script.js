document.addEventListener('DOMContentLoaded', function () {
  const languageSelect = document.querySelector('#language_code');
  const translateButton = document.querySelector('#btn_translate');
  const helloDiv = document.querySelector('#hello');

  translateButton.addEventListener('click', function () {
    const langCode = languageSelect.value;

    if (langCode === '') {
      helloDiv.textContent = '';
      return;
    }

    fetch('https://hellosalut.stefanbohacek.com/?lang=' + langCode)
      .then(function (response) {
        return response.json();
      })
      .then(function (data) {
        helloDiv.textContent = data.hello;
      });
  });
});
