// let forecast = 'rainy day';

// function weather () {
//     let forecast = 'sunny weather';
//     console.log(forecast);
// }
// weather();
// console.log(forecast);


// let sky = 'blue';

// if (sky === 'blue') {
//     let pi = Math.PI;
//     let color = 'light Blue';
// }

// console.log(pi);
// console.log(color);
// console.log(sky);


// function bankRobbery () { 
//     const heroes = ['Spiderman', 'Batman', 'Superman', 'Daredevil', 'Dead Pool']; 
//     function callForHelp () { 
//         for (let i = 0; i < heroes.length; i++) {
//             console.log(`Help Me ${heroes[i]}`)
//         }
//     }
//     callForHelp();
// }

// function callTwice (func) {
//     func();
//     func();
// }

// function laugh () {
//     console.log('Ha Ha')
// }

// callTwice(laugh);

// function callTenTimes (f) {
//     for (let i = 1; i <= 10; i++) {
//         f()
//     }
// }

// function random () {
//     const randNum = Math.round(Math.random() * 10)
//     console.log(randNum)
// }

// callTenTimes(random)

// function makeMysteryFunc() {
//     const randomNum = Math.round(Math.random() * 10);
//     if (randomNum > 5) {
//         return function () {
//             console.log('This is a Happy Function')
//             console.log('You understand how to write this shit')
//         }
//     } else {
//         return function () {
//             console.log('This is a Sad Function')
//             console.log('But at least you understand this shit!')
//         }
//     }
// }

// function makeBetweenAge (min, max) {
//     return function (num) {
//         return num >= min && num <= max;
//     }
// }

// const myMath = {
//         PI: 3.14,
//         add: function (x, y) {
//             return x + y;
//         },
//         multiply(x, y) {
//             return x * y;
//         },
//         divide(x, y) {
//             return x / y;
//         }
// }

const wife = {
    name: 'Vanya',
    age: 33,
    favWords1: 'Go to Scott',
    favWords2: 'Stiga ce yel!',
    saying1: function () {
        return `${this.name} says ${this.favWords1}`
    },
    saying2: function () {
        return `${this.name} says ${this.favWords2}`
    }
}