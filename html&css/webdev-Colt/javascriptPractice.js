// String Properties & Methods
// +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
let myName = 'acoetzer';
        // -> Here we made a string variable using let.

console.log(`myName length: ${myName.length}`)
        // -> We printing the length of the string.

console.log(`myName in all caps${myName.toUpperCase()}`)
        // -> We are turning the string letter to all uppercase.

console.log(`The letter o in acoetzer has an index of: ${myName.indexOf('o')}`) 
        // -> Here we are using a method to return the index of a particular letter.


// Random Number & Math Object
// +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
console.log(`A Random Number: ${Math.floor(Math.random() * 10) + 1}`)
        //-> We made a random number from 1 to 10

console.log(Math.PI)
        // -> Returning the PI value

console.log(Math.pow(2, 4))
        // -> Returning the power of some Number


// Console, Prompt, Alert, parseInt
// +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

const userPrompt =  prompt('What is your name?')
const userNameIs