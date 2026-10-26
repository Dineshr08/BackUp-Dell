const num = [10,20,30];
num[2] = 99;
console.log(num);

// const array = [1,20,22,24,5]
const array = ['hai', 'hello', 'good'];

getLastValueArray(array);
function getLastValueArray(array) {
  console.log(array[array.length - 1]);
}

arraySwap(array);
// console.log(arraySwap(array));

function arraySwap(array) {

  const firstValue = array[0];
  const lastValue =  array[array.length-1]

  array[0] = lastValue;
  array[array.length-1] = firstValue;
  console.log(array);

  return array

}

for (let i = 0; i <= 10; i += 2) {
        console.log(i);
      }


for (let i = 5; i >= 0; i--) {
   console.log(i);
}

let i = 5;

while (i > 0) {
  i--;
  console.log(i);
}

let temp = [-2,-1, 0, 99];
let temp1 = [];
const num1 = 3;

addOne(temp);

function addOne(temp) {
  for (i = 0; i < temp.length; i++) {
    temp1[i] = temp[i] + 1;
  }
  console.log(temp1);
}

function addNum(temp, num2) {
  for (i = 0; i < temp.length; i = i + 1) {
    temp1[i] = temp[i] + num2;
  }
  console.log(temp1);

}