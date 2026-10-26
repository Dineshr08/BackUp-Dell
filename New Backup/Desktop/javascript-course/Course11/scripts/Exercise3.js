
function findIndex(array, word) {

  for (let i = 0; i < array.length; i++ ) {

    const tempData = array[i];
    console.log(tempData);

    if (tempData === word) {
      return i;
    }

  }
  return -1;
  
}


function removeEgg(foods) {
  const result = [];
  foodCopy = foods.slice();
  reversedFood = foodCopy.reverse();
  let count = 0;
  for (let i = 0; i < reversedFood.length; i++) {
    if (reversedFood[i] === 'egg') {
      count++;
      if (count <= 2) {
        continue;
      }
      result.push(reversedFood[i]);
    } else {
      result.push(reversedFood[i]);
    }
  }
  return result;

}

for (let i = 1; i <= 20; i++) {

  if ( i % 3 === 0) {
    console.log('Fizz');
  } else if (i % 5 === 0) {
    console.log('Buzz');
  } else if (i % 3 === 0 && i % 5 === 0) {
    console.log(FizzBuzz);
  }

}


function unique(array) {

  const result = [];

  for (let i = 0; i < array.length; i++ ) {
    const tempData = array[i];

    if (findIndex(result, tempData) === -1 ) {

      result.push(tempData);

    }
  }

  return result;
  
}

console.log(unique(['hello', 'world', 'search', 'good', 'hello']));
// console.log(findIndex(['hello', 'world', 'search', 'good'], 'world'));
// console.log(removeEgg(['egg', 'apple', 'egg', 'egg', 'ham']));