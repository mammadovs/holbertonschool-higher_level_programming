document.addEventListener('DOMContentLoaded', function () {
  const myList = document.querySelector('.my_list');
  const addItem = document.querySelector('#add_item');
  const removeItem = document.querySelector('#remove_item');
  const clearList = document.querySelector('#clear_list');

  addItem.addEventListener('click', function () {
    const newItem = document.createElement('li');
    newItem.textContent = 'Item';
    myList.appendChild(newItem);
  });

  removeItem.addEventListener('click', function () {
    const lastItem = myList.lastElementChild;
    if (lastItem) {
      lastItem.remove();
    }
  });

  clearList.addEventListener('click', function () {
    myList.innerHTML = '';
  });
});
