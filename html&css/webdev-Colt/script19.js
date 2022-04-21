// const userInput = prompt('Enter a number');

// for (let i = 1; i <= userInput; i++) {
//     if (i % 2 === 0) {
//         console.log(`${i} isEven`)
//     } else {
//         console.log(`${i} isODD`)
//     }
// }

// for (let i = 25; i >= 0; i -= 5) {
//     console.log(i)
// }

// const people = ['Vanya', 'Andre', 'Penka', 'Ganka', 'Stanka', 'Maria'];

// for (let i = 0; i < people.length; i++) {
//     console.log(`Original was ${people[i]}.`)
//     console.log(`indexOf(${i}) is - ${people[i].toUpperCase()}`)
// }

// for (let i = 0; i <= 10; i++){
//     console.log(`outterLoop: ${i}`)
//     for (let j = 1; j <=5; j++) {
//         console.log(`        innerLoop: ${j}`)
//     }
// }

// const plants = [
//     ['Apple', 'Plum', 'Apricot'],
//     ['Basil', 'Thyme', 'Rosemary'],
//     ['Tomato', 'Kale', 'Zuccini']
// ];

// for (let i = 0; i < plants.length; i++) {
//     const type = plants[i];
//     console.log(`type of plants ${i + 1}`)
//     for (let j = 0; j < type.length; j++) {
//         console.log(`    ${type[j]}`)
//     }

// }

// const people = ['Andre', 'Vanya', 'Dary'];

// // for (let i = 0; i < people.length; i++) {
// //     console.log(people[i])
// // }

// for (let i = people.length - 1; i >= 0; i--) {
//     console.log(people[i])
// }

// Nested arrays and loops
// let persons = [
//     ['Andre', '32', 'Male'],
//     ['Vanya', '57', 'Female'],
//     ['Dary', '28', 'Female']
// ]

// for (let i = 0; i < persons.length; i++) {
//     const individual = persons[i];
//     console.log(`At indexOf ${i} is:`)
//     for (let j = 0; j < individual.length; j++){
//         console.log(`          ${individual[j]}`)
//     }
// }

// Single array

// const colors = ['lime', 'lightblue', 'yellow'];

// for (let i = colors.length - 1; i >= 0; i--) {
//     console.log(`${i + 1} ${colors[i]}`)
// }

// for (let i = 1; i <= 5; i++) {
//     console.log(`The outter loop is :${i}`)
// }

// for (let i = 1; i <= 3; i++) {
//     console.log(`The Outter loop is :${i}`)
//     for (let j = 1; j <= 3; j += 1) {
//         console.log(`    The Inner loop is : ${j}`)
//     }
// }

// const people = ['Andre', 'Vanya', 'Dary'];

// for (let i = 0; i < people.length; i++) {
//     console.log(`At index ${i} is ${people[i]}`)
// }
// console.log(`There are ${people.length} persons here.`)

// const people = [
//     ['Andre', '32'],
//     ['Vanya', '33'],
//     ['Dary', '28']
// ]

// for (let i = 0; i < people.length; i++) {
//     const row = people[i];
//     console.log(`At index ${i}, we have:`)
//     for (let j = 0; j < row.length; j++) {
//         console.log(`${row}`)
//     }
// }

// const places = [
//     ['Canada', 'Northern Americas'],
//     ['Bulgaria', 'Eastern Europe'],
//     ['Republic of South Africa', 'Southern Africa'],
// ];

// for (let i = 0; i < places.length; i++) {
//     const row = places[i];
//     console.log(`At indexOf ${i} is:`)
//     for (let j = 0; j < row.length; j++) {
//         console.log(`    ${row[j]}`)
//     }
// }

// for (let i = 0; i <= 10; i++) {
//     if (i % 2 === 0) {
//         console.log(`${i} is Even`)
//     } else {
//         console.log(`${i} is Odd`)
//     }
// }

// for (let i = 0; i <= 3; i++) {
//     console.log(`The outter loop of :${i}`);
//     for (j = 1; j <= 2; j++) {
//         console.log(`       The inner loop index is :${j}`)
//     }
// }

// const people = [
//     ['Andre', 'Vanya', 'Dary'],
//     ['Mom', 'Dad'],
//     ['Maureen', 'Mark', 'Alicia']
// ];

// for (let i = 0; i < people.length; i++) {
//     // const row = people[i];
//     console.log(i);
//     for (let j = 0; j < people[i].length; j++ ) {
//         // console.log(`   ${row[j]}`);
//         console.log(`   ${j}`);
//     }
// }

// let userInput = prompt('Say Something"')

// while (true) {
//     if (userInput.toLowerCase() === 'stop copying me') {
//         break;
//     } else {
//         userInput = prompt(userInput);
//     }
// }
// alert('Sure thing!')

// let choice = parseInt(prompt('Enter a maximun number for the game.'));
// while (!choice) {
//     choice = parseInt(prompt('Enter a Number, not Text!'));
// }
// const targetNum = Math.round(Math.random() * choice);

// let guess = parseInt(prompt('Enter your first guess?'));
// let attemps = 1;
// const history = [];
// while (parseInt(guess) !== targetNum) {
//     history.push(guess)
//     if (guess === 'q') {
//         break;
//     } 
//     attemps++;
//     if (guess > targetNum) {
//         guess = prompt('Too high, guess again');
//     }   else {
//         guess = prompt('Too low, guess again');
//     }
// }

// if (guess === 'q') {
//     alert('Ok you quit');
// } else {
//     alert(`Congratulations`);
//     alert(`The hidden number was ${targetNum} of ${choice} and your guess was ${guess} on ${attemps} attemps `);
//     alert(`Your guesses were ${history} and the final ${guess}`)
// }

// const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]; //DON'T CHANGE THIS LINE PLEASE!

// // WRITE YOUR LOOP BELOW THIS LINE:
// for (num of numbers) {
//     console.log(num * num)
// }

// let num = 1;

// while (num <= 5) {
//     console.log(num)
//     num++;
// }

// for (let i = 1; i <= 5; i++) {
//     console.log(i)
// }

// let userInput = prompt('Say something').toLowerCase();

// while (true) {
//     if (userInput === 'stop') {
//         break;
//     } else {
//         userInput = prompt(userInput);
//     }
// }

// const classroom = [
//     ['Andre', 'Vanya', 'Dary'],
//     ['Mom', 'Dad'],
//     ['Buddy', 'Diesel', 'Goofy']
// ]

// for (let i = 0; i < classroom.length; i++) {
//     const row = classroom[i];
//     console.log(i);
//     for (let j = 0; j < row.length; j++) {
//         console.log(`   ${row[j]}`);
//     }
// }

// let num = 0;

// for (let row of classroom) {
//     console.log(num)
//     num++;
//     for (let student of row) {
//         console.log(`   ${student}`)
//     }
// }

// for (let char of 'Vanya') {
//     console.log(char)
// }

// const myname = 'Andre'
// for (let i = 0; i < myname.length; i++) {
//     console.log(myname[i])
// }

// let input = prompt('Enter a Name');

// let userName = '';

// // for (let i = 0; i < input.length; i++) {
// //     if (i % 2 === 0) {
// //         userName = userName + input[i].toUpperCase();
// //     } else {
// //         userName = userName + input[i].toLowerCase()
// //     }
// // }
// alert(userName)

// const classroom = ['Andre', 'Vanya', 'Dary', 'Colt', 'Keele'];

// for (let i = 0; i < classroom.length; i++) {
//     console.log(classroom[i])
// }

// const classroom = {
//     Andre: 'Present',
//     Vanya: 'Absent',
//     Dary: 'Sleeping',
//     Buddy: 'Playing'
// }

// for (let student in classroom) {
//     console.log(`${student} is ${classroom[student]}`)
// }