function handleCostKeyDown(event) {
  if (event.key === 'Enter') {
    costCalculate();
  }
  }

  function costCalculate() {
  const inputElement = document.querySelector('.js-input');
  let cost = Number(inputElement.value)
  console.log(cost)
  if (cost < 40 && cost >= 0) {
    cost += 10;
    document.querySelector('.js-dollor-result').innerHTML = `$${cost}`;
  } else if (cost < 0) {
    console.log('cost')
    document.querySelector('.js-dollor-result').innerHTML = `<p class="error-msg">Error: cost cannot be less than $0</p>`
  }

  }