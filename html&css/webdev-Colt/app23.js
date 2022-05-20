// Some Data

const nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
const nums2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20];

const raceResults = ['Vanya', 'Andre', 'Jeanette', 'Johan', 'Buddy', 'Mike', 'Sam', 'Fiona', 'Peter', 'Joey'];

const movieList = [
    {
        title: 'The Shawshank Redemption',
        score: 9.2,
        year: 1994
    },
    {
        title: 'The Godfather',
        score: 9.2,
        year: 1972
    },
    {
        title: 'The Dark Knight',
        score: 9.0,
        year: 2008
    },
    {
        title: '12 Angry Men',
        score: 8.9,
        year: 1957
    },
    {
        title: 'The Good, the Bad and the Ugly',
        score: 8.8,
        year: 1966
    }
];

const groupOne = {
    gold: 'Taylor',
    silver: 'Perre',
    tie: 'Sammy'
}

const groupTwo = {
    tie: 'Lexi',
    fifth: 'Andrea',
    sixth: 'Andrew'
}


const user = {
    firstName: 'Jose',
    lastName: 'Taco del Rio',
    age: 89,
    born: 1910,
    gender: 'Male',
    city: 'San Jose',
    state: 'California'
}



// Default Params
console.log('Default Params')
console.log('----------')

// Old Way
function rollDie1 (numSides) {
    if (numSides === undefined) {
        numSides = 6;
    }
    return Math.floor(Math.random() * numSides) + 1;
}
console.log(`Old way ${rollDie1()} from default 6`)
// New Way
function rollDie2 (numSides = 12) {
    return Math.floor(Math.random() * numSides) + 1;
}
console.log(`New way ${rollDie2()} from default 12`)

// Spread with Function calls
console.log('')
console.log('Spread with Function calls')
console.log('----------')

console.log(`Spread in Math.max(...nums1): ${Math.max(...nums1)}`)
console.log(`Spread in Math.min(...nums1): ${Math.min(...nums1)}`)
console.log(...nums1)
console.log(...'...Spread')

// Spread with Arrays
console.log('')
console.log('Spread with Arrays')
console.log('----------')

const nums1Copy = [...nums1, 'nums1Copy'];
const combination = [...nums1, ...nums2, 'combination'];

console.log(`This is a nums1 copy using spread: ${nums1Copy}`)
console.log(`This is a nums1 & nums2 combination using spread: ${combination}`)

// Spread with Objects
console.log('')
console.log('Spread with Objects')
console.log('----------')

const groupOneCopy = {...groupOne};
const bothGroups = {...groupOne, ...groupTwo}

console.log(`This is a copy of groupOne`)
console.log(groupOneCopy)
console.log(`This is a combination of both groups`)
console.log(bothGroups)

// Rest Params
console.log('')
console.log('Rest Params')
console.log('----------')

function race (gold, silver, bronze, ...everyoneElse) {
    console.log(`The Gold Medal goes to: ${gold}`)
    console.log(`The Silver Medal goes to: ${silver}`)
    console.log(`The Bronze Medal goes to: ${bronze}`)
    console.log(`Thank you to everyone else for participating: ${everyoneElse}`)
}
race(...raceResults)

// Destructing Arrays
console.log('')
console.log('Destructing Arrays')
console.log('----------')

const [gold, silver, bronze, ...everyoneElse] = raceResults;

console.log(`Gold goes to: ${gold}`)
console.log(`Silver goes to: ${silver}`)
console.log(`Bronze goes to: ${bronze}`)
console.log(` Thank you to everyone else: ${everyoneElse}`)

// Destructing Objects
console.log('')
console.log('Destructing Objects')
console.log('----------')

const {firstName, lastName: surname, born: birthYear, died = 'N/A'} = user;

console.log(`${firstName}, ${surname} was born ${birthYear} and death was ${died}`)

// Param Destructing
console.log('')
console.log('Destructing Objects')
console.log('----------')

// Way One
function fullNameOne (user) {
    return `${user.firstName} ${user.lastName}`
}

// Way Two
function fullNameTwo(user) {
    const {firstName, lastName: surname} = user;
    return `His first name was ${firstName} ${surname}`
}
// way Three
function fullNameThree({firstName, lastName}) {
    return `${firstName} ${lastName}`
}

console.log(fullNameOne(user))
console.log(fullNameTwo(user))
console.log(fullNameThree(user))