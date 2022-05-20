// Function Scopes
// *****************

function rainbow () {
    const colors = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet'];
    for (color of colors) {
        console.log(color)
    }
}
rainbow()

try {
    console.log(colors)
} catch {
    console.log('Error!')
    console.log('You cannot reach a variable scoped to a function')
}


// Block Scopes
// *****************
console.log('')

const blockScopeNum = 5;

if (blockScopeNum > 0) {
    let blockColor =  'Red';
    console.log(blockColor)
}

try {
    console.log(blockColor);
} catch {
    console.log('Error!')
    console.log('You cannot reach a variable scoped to a block of code')
}

// Lexical Scopes
// *****************
console.log('')

function plants () {
    const plantList = ['Basil', 'Cucumber', 'Zuccini', 'Avocado', 'Chili', 'Kale'];
    function myPlants (){
        for (let i = 0; i < plantList.length; i++) {
            console.log(`We have ${plantList[i]}`)
        }
    }
    myPlants();
}
plants();

try {
    console.log(plantList);
} catch {
    console.log('Error!')
    console.log('You cannot call a lexical scoped varaible')
}

// Function Expressions
// *****************
console.log('')

const collectEggs = function () {
    return 'EGG'
}

// Higher Order Functions - Functions as Arguments
// *****************
console.log('')

function dice (func) {
    func();
    func();
}

function singleDie () {
    console.log(Math.round(Math.random() * 6));
}

dice(singleDie);

// Higher Order Functions - Returning Functions
// *****************
console.log('')

// Return a random function
function giveMeARandomFunc () {
    const randomGen = Math.round(Math.random() * 2)
    if (randomGen === 0) {
        return function () {
            console.log('This is a Happy Function');
        }
    } else if (randomGen === 1) {
        return function () {
            console.log('You found Spice, becareful of the worm!')
        }
    } else {
        return function () {
            console.log('This is desert power!')
        }
    }
}

// Factory Function
function factoryFunction (min, max) {
    return function (num) {
        return num >= min && num <= max;
    }
}

// Defining Methods
// *****************
console.log('')

const bunny1 = {
    name: 'Harry the Bunny',
    breed: 'Siberian',
    says() {
        return 'Feed me, I am hungry!';
    }
}

// The "this" Keyword
// *****************

console.log('myBunny.')
console.log('name, breed, says(), health, searchForFood(), sleep()')

const myBunny = {
    name: 'Harry the Bunny',
    breed: 'Siberian',
    says() {
        while (this.health < 100) {
            return 'Feed me, I am hungry!';
            break;
        }
        return 'I am full, I want to sleep now';
    },
    health: 10,
    searchForFood() {
        let random = Math.round(Math.random() * 3)
        while (this.health < 100) {
            if (random === 0) {
                this.health += 5;
                return `${this.name} has found a carrot and gained 5 health. ${this.name}'s health is now ${this.health}`;
            } else if (random === 1) {
                this.health -= 2;
                return `${this.name} is being chased by a crazed hunter with an axe. ${this.name} has lost 2 health. ${this.name}'s health is now ${this.health}`;
            } else if (random === 2) {
                this.health += 15;
                return `${this.name} has found a delicious cabbage and gained 15 health. ${this.name}'s health is now ${this.health}`;
            } else if (random === 3) {
                let scopeRandom = Math.round(Math.random() * 10)
                if (scopeRandom > 0) {
                    return `${this.name} is in the scopes of a hunter, the hunter missed`
                } else {
                    this.health = 0;
                    return `${this.name} is in the scopes of a hunter, the hunter hit and ${this.name} is dead. Start Over. ${this.name}'s health is now ${this.health}`
                } 
            }
        }
        return `${this.name} is full, try to sleep to reset your game`
    },
    sleep() {
        let sleepRandom = Math.round(Math.random() * 1);
        if (sleepRandom > 0) {
            this.health = 10;
            return `${this.name} has slept well, and its health is back to ${this.health}`
        } else {
            this.health = 5;
            return `${this.name} had a terrible sleep, The wind had woken him up, ${this.name}'s health is now ${this.health}`
        }
    }
}