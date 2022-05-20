// // FOR LOOPS PRACTICE
// // *****************

// console.log('--- Basic For Loop ---');
// for (let i = 1; i <= 5; i++) {
//     console.log(`${i} iteration`);
// }
// console.log('--- END ---');

// console.log(' ');
// console.log('--- Basic For Loop in Reverse ---');
// for (let i = 5; i >= 1; i -= 1) {
//     console.log(`${i} iteration`);
// }
// console.log('--- END ---');

// // BASIC FOR LOOP ODDS & EVEN COUNT PRACTICE
// // *****************

// console.log(' ');
// console.log('--- Basic For Loop Even Count ---');
// for (let i = 2; i <= 10; i += 2) {
//     console.log(`EVEN: ${i}`)
// }
// console.log('--- END ---');

// console.log(' ');
// console.log('--- Basic For Loop Odds Count ---');
// for (let i = 1; i <= 10; i += 2) {
//     console.log(`EVEN: ${i}`)
// }
// console.log('--- END ---');

// // FOR LOOPS OVER AN ARRAY PRACTICE
// // *****************

// console.log(' ');
// console.log('--- For Loop Iterating Over an Array ---');

// const students = ['Colt', 'Brian', 'Jerry', 'Sam'];

// for (let i = 0; i < students.length; i++) {
//     console.log(`Present students are: ${students[i]}`)
// }
// console.log('--- END ---');

// console.log(' ');
// console.log('--- For Loop Iterating Over an Array in Reverse ---');

// for (let i = students.length - 1; i >= 0; i--) {
//     console.log(`Students starting from the back are: ${students[i]}`)
// }
// console.log('--- END ---');

// // NESTED FOR LOOPS PRACTICE
// // *****************

// console.log(' ');
// console.log('--- Basic Nested For Loop ---');

// for (let i = 1; i <= 3; i++) {
//     console.log(`Outer: ${i}`)
//     for (let j = 1; j <= 2; j++) {
//         console.log(`   Inner: ${i}.${j}`)
//     }
// }
// console.log('--- END ---');

// console.log(' ');
// console.log('--- Basic Nested For Loop in Reverse ---');

// for (let i = 3; i >= 1; i--) {
//     console.log(`outer: ${i}`)
//     for (let j = 2; j >= 1; j--) {
//         console.log(`   Inner: ${i}.${j}`)
//     }
// }
// console.log('--- END ---');

// // NESTED FOR LOOPS OVER NESTED ARRAYS PRACTICE
// // *****************

// console.log(' ');
// console.log('--- Basic Nested For Loop over Nested Arrays ---');

// const classroom = [
//     ['Colt', 'Brain', 'Sam'],
//     ['Andre', 'Vanya', 'Dary'],
//     ['Tom', 'Jerry', 'Scooby']
// ]

// for (let i = 0; i < classroom.length; i++) {
//     const row = classroom[i];
//     console.log(`Row ${i + 1} students are:`)
//     for (let j = 0; j < row.length; j++) {
//         console.log(`   ${i + 1}.${j + 1} ${row[j]}`)
//     }
// }
// console.log('--- END ---');

// console.log(' ');
// console.log('--- Basic Nested For Loop over Nested Arrays in Reverse ---');

// for (let i = classroom.length - 1; i >= 0; i--) {
//     const row = classroom[i];
//     console.log(`Row ${i + 1} students are:`)
//     for (let j = row.length - 1; j >= 0; j--) {
//         console.log(`   ${i + 1}.${j + 1} ${row[j]}`)
//     }
// }
// console.log('--- END ---');

// // FOR LOOP TO DETERMINE EVEN || ODD FROM USER INPUT
// // *****************

// console.log(' ');
// console.log('--- For Loop to Determine Even || Odd from User Input ---');

// let userNum = parseInt(prompt(`Pick a number for Even & Odds iteration`));
// while (!userNum) {
//     alert('DO NOT ENTER TEXT');
//     userNum = parseInt(prompt(`Pick a number for Even & Odds iteration`));
// }
// alert('Check Console for Iteration Outcome')

// for (i = 0; i <= userNum; i++) {
//     if (i % 2 === 0) {
//         console.log(`${i} is Even`);
//     } else {
//         console.log(`${i} is Odd`);
//     }
// }
// console.log('--- END ---');

// // FOR LOOP TO PRINT UPPER AND LOWER CASE LETTERS OF USERS NAME
// // *****************

// console.log(' ');
// console.log('--- For Loop to Print Upper and Lower Case of Users name ---');

// let userName =  prompt('Enter your name...');

// const storedName = userName;

// for (let i = 0; i < storedName.length; i++) {
//     if (i % 2 === 0) {
//         console.log(storedName[i].toUpperCase())
//     } else {
//         console.log(storedName[i].toLowerCase())
//     }
// }
// console.log('--- END ---');


// // BASIC WHILE LOOP
// // *****************

// console.log(' ');
// console.log('--- Basic While Loop ---');

// let count = 1;

// while (count <= 5) {
//     console.log(`${count} iteration`);
//     count++;
// }
// console.log('--- END ---');

// console.log(' ');
// console.log('--- Basic While Loop in Reverse ---');

// let countRev = 5;

// while (countRev >= 1) {
//     console.log(`${countRev} iteration`);
//     countRev--;
// }
// console.log('--- END ---');

// // BASIC WHILE LOOP GUESS CODE
// // *****************

// console.log(' ');
// console.log('--- Basic While Loop Code Guess ---');

// const secretCode = 'let me in';

// let userInput = prompt('Enter the secret code...');
// while (userInput !== secretCode) {
//     userInput = prompt('Enter the secret code...');
// }
// console.log('--- END ---');

// // WHILE LOOP GUESSING GAME
// // *****************

// console.log(' ');
// console.log('--- Guessing Game ---');

// let userChoice = parseInt(prompt('Pick a maximum number for a guessing game...'));
// while (!userChoice) {
//     alert('DO NOT INPUT TEXT!')
//     userChoice = parseInt(prompt('Pick a Maximum number for a guessing game...'));
// }

// const randomNum = Math.round(Math.random() * userChoice);

// let userGuess = parseInt(prompt(`Take a guess between 0 and ${userChoice}`));
// while (!userGuess) {
//     alert('DO NOT INPUT TEXT!')
//     userGuess = parseInt(prompt(`Take a guess between 0 and ${userChoice}`));
// }

// let scoreKeeper = 1;
// const tries = [];

// while (userGuess !== randomNum) {
//     scoreKeeper++;
//     tries.push(userGuess)
//     if (userGuess > randomNum) {
//         userGuess = parseInt(prompt('Too High, Guess again...'));
//     } else {
//         userGuess = parseInt(prompt('Too Low, Guess again...'));
//     }
// }
// alert(`Correct, The Random Number was ${randomNum} and your guess was ${userGuess}.`)
// alert(`It took you, ${scoreKeeper} times before guessing correctly, and your previous guesses were ${tries}.`)

// console.log(`User Choice was: ${userChoice}`)
// console.log(`Random Number was: ${randomNum}`)
// console.log(`User Guess was: ${userGuess} on ${scoreKeeper} tries`)
// console.log(`User's Guess history is: ${tries}`)
// console.log('--- END ---');

// // WHILE LOOP GUESSING GAME PRACTICE
// // *****************

// console.log(' ');
// console.log('--- Guessing Game Practice ---');

// // let theUsersChoice = parseInt(prompt('Select a maximum Num for a guessing game'));
// // while (!theUsersChoice) {
// //     alert('PLEASE ENTER A DIGIT NOT TEXT FOR THE INITIAL VALUE!');
// //     theUsersChoice = parseInt(prompt('Select a maximum Num for a guessing game'));
// // }

// // const theRandomNum = Math.round(Math.random() * theUsersChoice);

// // let theUsersGuess = parseInt(prompt('Take a guess...'));
// // while (!theUsersGuess) {
// //     alert('FOR THE GUESS PLEASE ENTER A NUMBER AND NOT TEXT');
// //     theUsersGuess = parseInt(prompt('Take a guess...'));
// // }

// // const theHistory = [];
// // let attempts = 0;

// // while (theUsersGuess !== theRandomNum) {
// //     theHistory.push(theUsersGuess);
// //     attempts++;
// //     if (theUsersGuess > theRandomNum) {
// //         theUsersGuess = parseInt(prompt('Too High, Take a guess...'));
// //     } else {
// //         theUsersGuess = parseInt(prompt('Too Low, Take a guess...'));
// //     }
// // }

// // alert(`Weldone, you guessed correctly. Random Number was : ${theRandomNum}, Your Guess was : ${theUsersGuess}. It took you ${attempts} attempts and your guess history was: ${theHistory}`)
// console.log('--- END ---');

// // FOR ... OF LOOP PRACTICE
// // *****************

// console.log(' ');
// console.log('--- For ... Of Loops ---');

// let n = 0;

// for (let i of 'Andre') {
//     if (n % 2 === 0) {
//         console.log(i.toUpperCase())
//     } else {
//         console.log(i.toLowerCase())
//     }
//     n++ 
// }

// console.log('--- END ---');

// // FOR ... IN LOOP PRACTICE
// // *****************

// console.log(' ');
// console.log('--- For ... In Loops ---');

// const personObject = {
//     Name: 'Andre',
//     Surname: 'Coetzer',
//     Age: 32,
//     Sex: 'Male',
// }

// for (let data in personObject) {
//     console.log(data, personObject[data])
// }

// console.log('--- END ---');

// FOR ... IN LOOP PRACTICE
// *****************

// console.log(' ');
// console.log('--- ToDo List Program ---');

// let userInput = prompt('What would you like to do? (new, list, delete or quit)').toLowerCase();

// const list = [];

// while (userInput !== 'quit' && userInput !== 'q') {
//     if (userInput === 'new') {
//         while (userInput !== 'q') {
//             userInput = prompt('Enter a New ToDo? (q to leave)');
//             list.push(userInput);
//             if (list.includes('q') === true) {
//                 list.pop('q')
//             }
//             console.log(`"${userInput}" was added to the ToDo list.`);
//         }
//     } else if (userInput === 'list') {
//         console.log('***************')
//         for (let i = 0; i < list.length; i++) {
//             console.log(`${i + 1}. ${list[i]}`)
//         }
//         console.log('***************')
//     } else if (userInput === 'delete') {
//         console.log('***************')
//         for (let i = 0; i < list.length; i++) {
//             console.log(`${i + 1}. "${list[i]}"`)
//         }
//         console.log('***************')
//         userInput = parseInt(prompt('Which ToDo Would you like to delete?'));
//         while (!userInput) {
//             alert('PLEASE ENTER A DIGIT NOT A NUMBER!')
//             userInput = parseInt(prompt('Which ToDo Would you like to delete?'));
//         }
//         let deletion = list.splice(userInput - 1, 1);
//         console.log(`-- "${deletion}" was deleted from the list!`)
//     }
//     userInput = prompt('What would you like to do? (new, list, delete or quit)').toLowerCase();
// }
// console.log('You quit the program')
// console.log('--- END ---');