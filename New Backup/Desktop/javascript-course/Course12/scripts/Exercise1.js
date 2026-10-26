const add = function() {
  console.log(2+3);
};

add();
add();

function runTwice(fun) {
  fun();
}

 runTwice(function() {
  console.log('Hello');
 })

function change() {
  document.querySelector('.js-change').innerHTML = 'Laoding...';
  setTimeout(function() {
    document.querySelector('.js-change').innerHTML = 'Finished';
  }, 1000);
  
}

let clicked = false;
let time;

function added() {
  if(!clicked) {
    document.querySelector('.js-msg').innerHTML = 'Added';
    time = setTimeout(function() {
      document.querySelector('.js-msg').innerHTML = '';
    }, 2000);
    clicked = true;
  } else {
    clicked = false;
    clearTimeout(time);
    setTimeout(function() {
      document.querySelector('.js-msg').innerHTML = '';
    }, 2000);
  }
}



let messages = 2;

setInterval(function() {
  if(messages > 0) {

    if (document.title === 'App') {
    document.title = `${messages} New messages`;
  } else {
    document.title = 'App';
  }

  } else {
    document.title = 'App';
  }
  
}, 2000);





