let userInput = prompt("What or who do you love the most?").toLowerCase();

if (userInput === "andre") {
    console.log("That's a good choice")
} else if (userInput === 'eso') {
    console.log("It must be those 3 Dragon's")
} else if (userInput === "myself") {
    console.log("Of course, you are the best!")
} else {
    console.log(`I don't know what or who this "${userInput}" is!`)
}