let score = JSON.parse(localStorage.getItem('score'));

      
      if(score === null) {
        score = {
          win : 0,
          loss : 0,
          tie: 0
        } 
      }

      //Step2 why we called here is as soon the webpasge load the js loads and assign the values to the paragraph with last updated value which is in local storage

      updateScoreElement();

      

      function playGame(playerMove) {

        const computerMove = pickComputerMove();
        let result = '';
        

        if (playerMove === 'rock'){

          if (computerMove === 'rock')
          {
            result = 'tie';
          }
          else if (computerMove === 'paper')
          {
            result = 'You Lost';
          }
          else if (computerMove === 'scissors')
          {
            result = 'You Won';
          }

        } else if (playerMove === 'paper') {

            if (computerMove === 'rock')
            {
              result = 'You Won';
            }
            else if (computerMove === 'paper')
            {
              result = 'Tie';
            }
            else if (computerMove === 'scissors')
            {
              result = 'You Lost';
            }
            
        } else if (playerMove === 'scissors') {

          if (computerMove === 'rock')
          {
            result = 'You Lost';
          }
          else if (computerMove === 'paper')
          {
            result = 'You Won';
          }
          else if (computerMove === 'scissors')
          {
            result = 'Tie';
          }
          
        }

        if (result === 'You Won') {
          score.win += 1;
        } else if (result === 'You Lost') {
          score.loss += 1;
        } else if (result === 'Tie') {
          score.tie += 1;
        }
      


        localStorage.setItem('score', JSON.stringify(score));

        //Step3: To store the recent value , we have called here as well

        updateScoreElement();

        //Step6: we do below to store the data to paragraph element ie our result

        document.querySelector('.js-result').innerHTML = result;
        
        //Step7: we do below to store the data to paragraph element ie our moves to our move and computer move

        document.querySelector('.js-moves').innerHTML = `You
<img src="images/${playerMove}-emoji.png" class="move-icon">
<img src="images/${computerMove}-emoji.png" class="move-icon">
Computer`;

        //Step8 As we dont want to see the alert so commenting

        /*
        alert(`You picked ${playerMove}, computer picked ${computerMove}, ${result}
Win: ${score.win}, Loss: ${score.loss}, Tie: ${score.tie}`);
*/


      }

      function updateScoreElement() {
        document.querySelector('.js-score')
          .innerHTML = `Win: ${score.win}, Loss: ${score.loss}, Tie: ${score.tie}`;
      }
      function pickComputerMove(){
        const randomNum = Math.random();
        let computerMove = '';
        if ( randomNum >= 0 && randomNum < 1 / 3 )
        {
          computerMove = 'rock'
        }
        else if ( randomNum >= 1 / 3 && randomNum < 2 / 3 )
        {
          computerMove = 'paper'
        }
        else if ( randomNum >= 2 / 3 && randomNum < 1 )
        {
          computerMove = 'scissors'
        }
        return computerMove;
      }