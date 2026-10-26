let calculation = '';
localStorage.getItem('calculation');
displayResult();
if (!calculation) {
  calculation = '';
}

function updateCalculation(strValue) {

  calculation+=strValue;
  console.log(calculation);
  localStorage.setItem('calculation', calculation);
  displayResult();

}

function displayResult() {
  document.querySelector('.js-display').innerHTML = localStorage.getItem('calculation');
}