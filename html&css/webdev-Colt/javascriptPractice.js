// String Properties & Methods -----------------------------------------------------------------------------------------
console.log('String Properties & Methods:')
// ---------------------------------------------------------------------------------------------------------------------
let myName = 'acoetzer';
// Here we made a string variable using let.

let manyNames = 'Andre, Vanya, Colt, Joey, Mathew';
// Here we made a string housing many names.

console.log('1. This are escape sequences, \nAin\'t this cool?.\nWe have also tabbed this \tword.');
// Above we using escape sequences to allow for a new line to start etc...

console.log(`2. acoetzer has a length of: ${myName.length}`);
// We printing the length of the string.

console.log(`3. acoetzer in all caps is: ${myName.toUpperCase()}`);
// We are turning the string letter to all uppercase.

console.log(`4. The letter 'o' in acoetzer has an index of: ${myName.indexOf('o')}`);
// Here we are using a method to return the index of a particular letter.

console.log(`5. The first 3 letters in my surname is: ${myName.slice(1, 4)}`);
// Above , we trying to slice the string to produce on coe.

console.log(`6. My full name is: ${myName.slice(0, 1).toUpperCase()}ndre ${myName.slice(1, 2).toUpperCase()}${myName.slice(2)}`);
// Above , we trying to slice the string to produce my full name.

const manyNamesArray = manyNames.split(',')
// We used a string method to form an array based on the split mark.

console.log(manyNamesArray)





// Random Number & Math Object -----------------------------------------------------------------------------------------
console.log('')
console.log('Random Number & Math Object:')
// ---------------------------------------------------------------------------------------------------------------------
console.log(`1. Generating a Random Number between 1 & 10: ${Math.floor(Math.random() * 10) + 1}`)
// We made a random number from 1 to 10.

console.log(`2. Math.PI give you this Value: ${Math.PI}`)
// Returning the PI value.

console.log(`Math.pow(2, 4) gives us: ${Math.pow(2, 4)}`)
// Returning the power of some Number.





// Console, Prompt, Alert & parseInt -----------------------------------------------------------------------------------
console.log('')
console.log('Console, Prompt, Alert & parseInt:')
// ---------------------------------------------------------------------------------------------------------------------

// const userPrompt =  prompt('What is your name?')
// const username = userPrompt;
// console.log(`1. The username is: ${username}`)
// // Prompting a user for their name and saving it to a varaible and printed it out to the console.

// const notfication = alert('We have saved your name to a username variable. \nHave a great day!')
// // Providing an alert window.

// const favNum = parseInt(prompt('What\'s your favourite number?'))
// console.log(`2. User\'s favourite number is: ${favNum}`)





// If Statements -------------------------------------------------------------------------------------------------------
    // -> Switch Statement
    // -> Ternary Statement
console.log('')
console.log('If Statements:')
// ---------------------------------------------------------------------------------------------------------------------
const weather = 'hot';

if (weather === 'hot') {
        console.log('Don\'t forget to bring sunscreen!!')
} else if (weather === 'cold') {
        console.log('What a shame!\nI was looking forward to wearing shorts')
} else if (weather === 'perfect') {
        console.log('Yay!\n I can wear shorts today')
} else {
        console.log('I dont know what you mean!')
}
// Stupid if & else if & else statement checking the weather.

const day = 2;

switch (day) {
    case 1:
        console.log('Monday')
        console.log('Arrr, Its MONDAY!!!')
        break;
    case 2:
        console.log('Tuesday')
        console.log('Is it the Weekend yet?')
        break;
    case 3:
        console.log('Wednesday')
        console.log('Almost there, only halfway')
        break;
    case 4:
        console.log('Thursday')
        console.log('Only Thursday, come on Friday')
        break;
    case 5:
        console.log('Friday')
        console.log('We just need to make it to the end of the day!')
        break;
    case 6:
    case 7:
        console.log('Weekend')
        console.log('Yay, its the weekend!')
        break;
}
// A switch statement, holding various days.

myName === 'acoetzer' ? console.log('Yes, it is'): console.log('No, it\'s not')
// A ternary statement being used for a quick yes or no condition.





// Array ---------------------------------------------------------------------------------------------------------------
    // -> Array Access 
    // -> Array Methods & Array Callback Methods
console.log('')
console.log('Array:')
// ---------------------------------------------------------------------------------------------------------------------
const arrPeople = ['Andre', 'Vanya', 'Colt', 'Jimmy', 'Lion'];
const arrPeopleInfo = [
    ['Andre', 'Coetzer', 'Male'],
    ['Vanya', 'Coetzer', 'Female'],
    ['Colt', 'Steele', 'Male']
]
const arrNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
const arrMovies = [
    {
        title: 'Movie90',
        score: 90
    },
    {
        title: 'Movie95',
        score: 95
    },
    {
        title: 'Movie85',
        score: 85
    },
]

console.log(`At index [0] of the classroom array is: ${arrPeople[0]}`);
// Here we are accessing a single array though indicey.

console.log(`At index of [2][0] of the peopleInfo array is: ${arrPeopleInfo[2][0]}`);
// Here we are accessing a nested array by providing multiple arrays.

arrPeople.push('Sam')
// Here we are adding a person to the array but at the end.
console.log('With .push(), We just added Sam to the end of the people array:')
console.log(arrPeople)

const poppedPerson = arrPeople.pop('Sam');
// Here we removed the last entry in the array using the .pop() method.
// We also saved the popped entry to a variable.
console.log(`With .pop(), We removed Sam from the people array and saved it to another variable`)
console.log(arrPeople)
console.log(`The removed entry was: ${poppedPerson}`)

arrPeople.unshift('Sam')
// With .unshift() we added an entry to the front of the array.
console.log('With .unshift(), We just added Sam to the front of the people array:')
console.log(arrPeople)

arrPeople.shift('Sam')
// With .shift() 
console.log('With .shift(), We just removed Sam from the front of the people array:')
console.log(arrPeople)

console.log('.forEach() callback method')
let i = 0;
const individuals = arrPeople.forEach((person) => {
    console.log(`${i + 1} is: ${person}`)
    i++
})
// We are using the forEach callback method to iterate over an array and print each person out.

console.log('.map() callback method')
const peoplesCopy = arrPeople.map((person) => {
    return person.toUpperCase()
})
console.log(peoplesCopy)
// Here we made a copy of the array using the map callback method, though also changed all letters to uppercase.

console.log('.filter() callback method')
const evenNumbersOnly = arrNumbers.filter((num) => num % 2 === 0)
console.log(evenNumbersOnly)
// Above is a implicit return of the filter callback method only return back the even numbers.

console.log('.filter() & .map() callback method')
const bestMovies = arrMovies
    .filter((movie) => movie.score >= 90)
    .map((movie) => movie.title)
;
console.log(`The Best Movies are: ${bestMovies}`)
// Here we using 2 callback together filter and map, to find the best movies.

console.log('.some() & .every()')
const isSomeEven = arrNumbers.some((num) =>{
    return num % 2 === 0
})
console.log(`Is some numbers even?: ${isSomeEven}`)
// Here we checked if some numbers are even using the some callback method.

const isEveryEven = arrNumbers.every((num) => {
    return num % 2 === 0
})
console.log(`Is every number even?: ${isEveryEven}`)
// Here we checked if every number is even using the every callback method.

console.log('.reduce((min, curr))')
const smallestName = arrPeople.reduce((min, curr) => {
    if (curr.length < min.length) {
        return curr
    }
    return min
})
console.log(`The person with the shortest name is: ${smallestName}`)
// We used the reduce callback method to find the smallest name, we saw that it returns the first possible match.





// Object Literals -----------------------------------------------------------------------------------------------------
    // -> Access Data from Object Literal
    // -> Modifying Objects
console.log('')
console.log('Object Literals:')
// ---------------------------------------------------------------------------------------------------------------------
const objUser = {
    firstName: 'Vinny',
    lastName: 'del Ray',
    age: 45,
    gender: 'Male'
}
// Made a object literal.

const objUsers = {
    userOne: {
        firstName: 'Andre',
        lastName: 'Coetzer',
        age: 33,
        gender: 'Male'
    },
    userTwo: {
        firstName: 'Vanya',
        lastName: 'Coetzer',
        age: 34,
        gender: 'Female'
    }
}
// Made a nested object literal.

console.log(`${objUser.firstName}, is ${objUser.age} years old`)
// Accessed the object literal.

console.log(`${objUsers.userOne.firstName} is a ${objUsers.userOne.gender}`)
// Accessed a nested object literal.

objUser.firstName = 'Vinnie'
console.log(`We changed the value of the firstname to ${objUser.firstName}`)
// Accessed the object and changed the value.





// Loops & Nested Loops ------------------------------------------------------------------------------------------------
    // -> For Loop 
    // -> For of Loop 
    // -> For in Loop 
    // -> While loop & break; Keyword
console.log('')
console.log('Loops & Nested Loops:')
// ---------------------------------------------------------------------------------------------------------------------
const forNumbers = [1, 2, 3, 4, 5];
const forPlant = ['Basil', 'Rosemary', 'Thyme'];
const forPlants = [
    ['Basil'],
    ['Rosemary'],
    ['Thyme'],
]
const forMovies = [
    {
        title: 'Movie95',
        score: 95
    },
    {
        title: 'Movie90',
        score: 90
    },
    {
        title: 'Movie85',
        score: 85
    },
]

let sum = 0;
for (let i = 0; i < forNumbers.length; i++) {
    sum += forNumbers[i]
}
console.log(sum)
// 

for (let i = 0; i < forPlant.length; i++) {
    console.log(`Plant ${i + 1} is ${forPlant[i]}`)
}
// 

for (let i = 0; i < forPlants.length; i++) {
    const row = forPlants[i]
    for (let j = 0; j < row.length; j++) {
        console.log(`${row[j]}`)
    }
}
// 

for (let num of forNumbers) {
    if (num % 2 === 0) {
        console.log(`${num} is Even`)
    } else {
        console.log(`${num} is Odd`)
    }
}
// 

for (let movie in forMovies) {
    console.log(forMovies[movie].title)
}
// 

// let userInput = prompt('What is the new ToDo?\nType Help for options')
// const list = [];

// while (userInput.toLowerCase() !== 'quit' && userInput.toLowerCase() !== 'q') {
//     if (userInput.toLowerCase() === 'new'){
//         while (userInput.toLowerCase() !== 'q') {
//             userInput = prompt('What would you like to add?')
//             list.push(userInput)
//             if (list.includes('q')){
//                 list.pop('q')
//             } else {
//                 console.log(`'${userInput}' was added to the todo list.`)
//             }
//         }
//     } else if (userInput.toLowerCase() === 'list') {
//         console.log('_-_-_-_-_-_-_-_-_-_-')
//         for (let i = 0; i < list.length; i++) {
//             console.log(`${i + 1}. ${list[i]}`)
//         }
//         console.log('_-_-_-_-_-_-_-_-_-_-')
//     } else if (userInput.toLowerCase() === 'delete') {
//         console.log('!------------------!')
//         for (let i = 0; i < list.length; i++) {
//             console.log(`${i + 1}. ${list[i]}`)
//         }
//         console.log('!------------------!')
//         let deleteToDo = parseInt(prompt('Which line to delete?'))
//         let removedItem = list.splice(deleteToDo - 1, 1)
//         console.log(`${removedItem} was removed from the todo list`)
//     } else if (userInput.toLowerCase() === 'help') {
//         alert('New: to make a new ToDo\nList: to view your ToDo list\nDelete: to remove a ToDo')
//     }
//     userInput = prompt('What is the new ToDo?\nType Help for options')
// }

let index = 0;
while (index <= 5){
    console.log(index)
    index++
}


// Functions & Arrow Functions -----------------------------------------------------------------------------------------
    // Defining a Function 
    // Function Expression 
    // Arrow Functions
    // -> Explicit Returns with & without Parenthesis
    // -> One liners
    // Functions with Arguments
    // Factory Functions
    // -> Return Random Function
    // -> Make a Function
console.log('')
console.log('Functions & Arrow Functions:')
// ---------------------------------------------------------------------------------------------------------------------
function isEven (num) {
    return num % 2 === 0
}
console.log(isEven(22))
// Defined a function.

const isValidPass = function (pass) {
    if (pass.length >= 8 && pass.indexOf(' ') === -1) {
        return 'Correct Pass'
    }
    return 'incorrect Pass'
}
// Made a function Expression.

const isEvenOne = (num) => {
    return num % 2 === 0
}
console.log(isEvenOne(1))
// Arrow function with parenthesis around parameter.

const isEvenTwo = num => {
    return num % 2 === 0
}
console.log(isEvenTwo(2))
// arrow function with no parenthesis around parameter.
const isEvenThree = num => (
    num % 2 === 0
)
console.log(isEvenThree(3))
// Arrow Function with implicit return using parenthesis

const isEvenFour = num => num % 2 === 0
console.log(isEvenFour(4))
// Arrow Function with implicit return using one line.

function add (num1, num2) {
    return num1 + num2
}
console.log(add(10, 20))
// A function with multiple paremeters

function makeFunc (min, max) {
    return function (num) {
        return num >= min && num <= max
    }
}
// Made a function that makes a range function to see if something is between a vertain range.

function randomFunc () {
    const randomNum = Math.floor(Math.random() * 10) + 1;

    if (randomNum < 5) {
        return function () {
            console.log('This is a happy function')
        }
    } else {
        return function () {
            console.log('This is sad function')
        }
    }    
}
// Made a function that give a random function
let surpriseFunc = randomFunc();
console.log(surpriseFunc())





// Defining Methods ----------------------------------------------------------------------------------------------------
    // -> The keyword 'this'
console.log('')
console.log('Defining Methods:')
// ---------------------------------------------------------------------------------------------------------------------
const myHair = {
    color: 'Dark Brown',
    length: 0,
    grow() {
        let randomNum = Math.floor(Math.random() * 10) + 1
        this.length += randomNum
        console.log(`Your hair grew by ${randomNum},\n Your Hair length is now ${this.length}cm long`);
    },
    cut() {
        this.length = 0;
        console.log(`Your hair was cut, it is now ${this.length}cm`);
    }
}
// 




// try & catch ---------------------------------------------------------------------------------------------------------
console.log('')
console.log('try & catch:')
// ---------------------------------------------------------------------------------------------------------------------

try {
    console.log(bluePill)
} catch (e) {
    console.log('bluePill is not a variable')
}
// Here we are providing a command that will result in an error only for practice sake,
// and then rewording the error message.





// Default Params ------------------------------------------------------------------------------------------------------
console.log('')
console.log('Default Params:')
// ---------------------------------------------------------------------------------------------------------------------
function rollDie (num = 6) {
    return Math.floor(Math.random() * num) + 1;
}
// Made a rolling dice with a default parameter.




// Spread --------------------------------------------------------------------------------------------------------------
    // -> Spread in Functions
    // -> Spread in Arrays
    // -> Spread in Objects
console.log('')
console.log('Spread:')
// ---------------------------------------------------------------------------------------------------------------------
const spreadNumber = [1, 2, 3, 4, 5]
const user = {
    username: 'Jim',
    password: 'This is a password',
    email: 'JimmyJamMaBammy@GGmaail.com'
}

console.log(Math.min(...spreadNumber))
console.log(Math.max(...spreadNumber))
// Here we spread an array to function calls

const spreadNumberCopy = [...spreadNumber, ...spreadNumber]
console.log(spreadNumberCopy)
// Here we are a copying an array using spread.

const userCopy = {...user}
// Same as here, we are copying an object.


// Destructing ---------------------------------------------------------------------------------------------------------
    // -> Arrays
    // -> Objects
    // -> Params
console.log('')
console.log('Destructing:')
// ---------------------------------------------------------------------------------------------------------------------
const raceResults = ['Andre', 'Vanya', 'Colt', 'James', 'Willy', 'Si'];
const userProfile = {
    firstName: 'Billy',
    lastName: 'Bob',
    age: 32

}

const [first, second, third, ...everyoneElse] = raceResults;
console.log(first, second, third, everyoneElse)
// We are deconstructing an array, these variables correlate to the indice value, so order matters.
// We also used rest params for the last varaible, as this places the rest of the elements in the array into that.

const {firstName: fname, lastName: surname, born = 'Not Stated'} = userProfile;
console.log(fname, surname, born)
// Here we are deconstructing an object, at the same time we are renaming the variable and providing a default parameter.

const userPick = (({firstName, age}) => {
    console.log(firstName, age)
})
userPick(userProfile)
// Here we are deconstructing directly into the function.





// The World of DOM ----------------------------------------------------------------------------------------------------
    // Slecting an Element
        // -> getElementById('')
        // -> getElementsByTagName('')
        // -> getElementsByClassName('')
        // -> querySelector('')
        // -> querySelectorAll('')
    //  innerText
    //  textContext
    //  innerHTML
    //  Attributes
        // -> getAttribute()
        // -> setAttribute('Name', 'Value')
    //  style
    //  classList
        // -> add()
        // -> remove()
        // -> toggle()
    //  Parent, Child & Sibling
        // -> parentElement
        // -> children
        // -> nextSibling
            // -> nextElementSibling
        // -> previousSibling
            // -> previousElementSibling
    // craeteElement
    //  Appending
        // -> appendChild()
        // -> append()
        // -> prepend()
        // -> insertAdjacentElement()
    //  Removing
        // -> removeChild()
        // -> remove()
console.log('')
console.log('The World of DOM:')
// ---------------------------------------------------------------------------------------------------------------------
const practiceList = document.getElementById('practiceList')
const li = document.getElementsByTagName('li')
const list = document.getElementsByClassName('list')
const h1 = document.querySelector('h1')
const header = document.querySelector('header')
const h2 = document.querySelectorAll('h2')
// Using all the JavaScript Selector, we have selected a few things.


console.dir(practiceList)
console.dir(li)
console.dir(list)
console.dir(h1)
console.dir(h2)
// Here we just checking if the object was an abject

h1.innerText = 'I Changed This With JavaScript'
console.log(h1.textContent)
h1.innerHTML += '<i>:)</i>'
// Here we are manipulating the inner context of an element.

h1.setAttribute('title', 'This is an H1 Title set with JavaScript')
console.log(h1.getAttribute('title'))
// Here we set the attribute and retrieved the attribute

// h1.style.color = 'coral'
// setting the style of an object Element

h1.classList.add('notRealClass')
console.log(h1.classList)
h1.classList.remove('notRealClass')
console.log(h1.classList)
h1.classList.toggle('toggleClass')
// Here we adding removing and toggling classes for the h1 Object Element
function headerToggle () {
    h1.classList.toggle('toggleClass')
}
// Here we made a function that toggles a class for the h1

console.log(h1.parentElement)
console.log(header.children)
console.log(h1.nextSibling)
console.log(h1.nextElementSibling)
console.log(h1.nextElementSibling.previousSibling)
console.log(h1.nextElementSibling.previousElementSibling)
// Here we are traversing the DOM by using the following properties.

const img =  document.createElement('img')
img.src = 'https://images.unsplash.com/photo-1652491216339-cc924481a6b1?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=387&q=80';
img.classList.add('imageSize')
// created an image element
// added the image source
// provide the image a class

header.insertAdjacentElement('afterend', img)
// Appended the img to the html page

function remove () {
    img.remove()
}
// Made a function to remove the img element.

// setTimeout, setInterval & clearInterval -----------------------------------------------------------------------------
console.log('')
console.log('setTimeout, setInterval & clearInterval:')
// ---------------------------------------------------------------------------------------------------------------------
setTimeout (() => {
    console.log('This message will appear after 2 seconds')
}, 2000)
// Made a message appear after 2 seconds.

const intervalId = setInterval (() => {
    console.log(Math.floor(Math.random() * 10) + 1);
}, 2000)
// Made a random number generate every 3 seconds

setTimeout (() => {
    clearInterval(intervalId);
}, 5000)
// Stopped setInterval with clearInterval at a specific time.