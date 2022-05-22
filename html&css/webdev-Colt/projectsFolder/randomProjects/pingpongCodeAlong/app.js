const p1 = {
    button: document.querySelector('#p1Button'),
    display: document.querySelector('#p1AddScore'),
    score: 0
}

const p2 = {
    button: document.querySelector('#p2Button'),
    display: document.querySelector('#p2AddScore'),
    score: 0
}

const resetButton = document.querySelector('#resetButton');
const playto = document.querySelector('#playTo')

function pingPongGame (player, opponent) {
    if (!isGameOver) {
        player.score++
        player.display.textContent = player.score
        if (player.score === winningScore) {
            isGameOver = true
            player.display.classList.add('winner')
            opponent.display.classList.add('loser')
        }
    }
}

function reset () {
    p1.score = 0;
    p2.score = 0;

    p1.display.textContent = '0'
    p1.display.classList.remove('winner', 'loser')
    p2.display.textContent = '0'
    p2.display.classList.remove('winner', 'loser')

    isGameOver = false
}

let winningScore = 3;
let isGameOver = false;

p1.button.addEventListener('click', function () {
    pingPongGame(p1, p2)
});

p2.button.addEventListener('click', function () {
    pingPongGame(p2, p1)
});

playto.addEventListener('change', function () {
    reset()
    winningScore = parseInt(this.value)
})

resetButton.addEventListener('click', function () {
    reset()
})

// const p1Button = document.querySelector('#p1Button');
// const p2Button = document.querySelector('#p2Button');

// let p1Score = 0;
// let p2Score = 0;

// const p1Display = document.querySelector('#p1AddScore');
// const p2Display = document.querySelector('#p2AddScore');

// p1Button.addEventListener('click', function () {
//     if (!isGameOver) {
//         p1Score++
//         p1Display.textContent = p1Score
//         if (p1Score === winningScore) {
//             isGameOver = true
//             p1Display.classList.add('winner')
//             p2Display.classList.add('loser')
//         }
//     }
// });

// p2Button.addEventListener('click', function () {
//     if (!isGameOver) {
//         p2Score++
//         p2Display.textContent = p2Score
//         if (p2Score === winningScore) {
//             isGameOver = true
//             p2Display.classList.add('winner')
//             p1Display.classList.add('loser')
//         }
//     }
// });