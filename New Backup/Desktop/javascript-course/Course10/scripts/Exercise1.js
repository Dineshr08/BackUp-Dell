const buttonElement = document.querySelector('.js-uber-button');
console.log(buttonElement);
console.log(buttonElement.classList.contains('uber-button-request'));

function isToggled(button) {
  let status = false;
  const gameButtonElement = document.querySelector(button);
  // gameButtonElement.classList.add('isToggled');
  if (!gameButtonElement.classList.contains('isToggled')) {
    turnOffPreviousButton();
    gameButtonElement.classList.add('isToggled');

  } else {
    gameButtonElement.classList.remove('isToggled');
  }
}

function turnOffPreviousButton() {
  const previousButton = document.querySelector('.isToggled');
  if (previousButton) {
    previousButton.classList.remove('isToggled');
  }
}

