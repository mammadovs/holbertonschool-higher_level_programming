const addItemTrigger = document.querySelector('#add_item');
const listElement = document.querySelector('.my_list');

addItemTrigger.addEventListener('click', function () {
  const newItem = document.createElement('li');
  newItem.textContent = 'Item';
  listElement.appendChild(newItem);
});
