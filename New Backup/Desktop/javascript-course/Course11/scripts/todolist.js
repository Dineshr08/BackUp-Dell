let toDoArray = [];
function toDoList() {
  let nameElement = document.querySelector('.js-input');
  let name = nameElement.value;
  let dateElement = document.querySelector('.js-date-class');
  let date = dateElement.value;
  toDoArray.push({name:name,
    date:date
  });
  nameElement.value = '' //To make the input box as empty
  dateElement.value = '' //To make the input box as empty/
  console.log(toDoArray);
  toDoDisplay();
}

function toDoDisplay() {
  let list = '';
  for (let i=0; i<toDoArray.length;i++) {
    const todoObject = toDoArray[i];
    name = todoObject.name;
    date = todoObject.date;
    const html = `<p>
    ${name} ${date}
    <button onclick="toDoArray.splice(${i},1); toDoDisplay();">Delete</button>
    </p>`;
    list += html;
    console.log(list);
  }
  document.querySelector('.js-container').innerHTML = list;
}