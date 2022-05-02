// Global Database
const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

const names = ['Andre Coetzer', 'Vanya Coetzer', 'Colt Steele', 'Jeanette Coetzer', 'Sam Fisher', 'Micheal Western']

const movies = [
    {
        title: 'Top Gun',
        score: 94
    },
    {
        title: 'Harry potter',
        score: 97
    },
    {
        title: 'Flash Dance',
        score: 95
    },
    {
        title: 'Terminator',
        score: 90
    },
    {
        title: 'Dune',
        score: 98
    }
]

// The forEach Method
console.log('       .forEach() Practice w/Num Array')
console.log('       ----------')
const evenOdd = numbers.forEach(num => {
    if (num % 2 === 0) {
        console.log(`${num} is Even`);
    } else {
        console.log(`${num} is Odd`)
    }
})

console.log('')
console.log('       .forEach() Practice w/Array Object')
console.log('       ----------')
const titles = movies.forEach(movie => {
    console.log(`${movie.title} - ${movie.score / 10}/10`)
})

// The map Method
console.log('')
console.log('       .map() Practice w/Str Array')
console.log('       ----------')
const uppercase = names.map(name => {
        return name.toUpperCase()
})
for (people of uppercase) {
    console.log(people)
}

console.log('')
console.log('       .map() Practice w/Num Array')
console.log('       ----------')
const double = numbers.map(num => {
    return num + num;
})
for (num of double) {
    console.log(num)
}

console.log('')
console.log('       .map() Practice w/Array Object')
console.log('       ----------')
const movieTitles = movies.map(movie => {
    return movie.title.toUpperCase()
})
for (movie of movieTitles) {
    console.log(movie)
}

// Arrow Functions
console.log('')
console.log('       Defining a Function')
console.log('       ----------')

function isEven1 (num) {
    return num % 2 === 0;
}
console.log(`${isEven1}`)
console.log(`Is the #1 Even?: ${isEven1(1)}`)

console.log('')
console.log('       A Function Expression')
console.log('       ----------')

const isEven2 = function (num) {
    return num % 2 === 0;
}
console.log(`const isEven2 = ${isEven2}`)
console.log(`Is the #2 Even?: ${isEven1(2)}`)

console.log('')
console.log('       Arrow Functions')
console.log('       ----------')
const isEven3 = (num) => {
    return num % 2 === 0;
}
console.log(`const isEven3 = ${isEven3}`)
console.log(`Is the #3 Even?: ${isEven1(3)}`)

console.log('')
console.log('       Arrow Functions without Parenthesis')
console.log('       when its a single argument or parameter.')
console.log('       ----------')
const isEven4 = num => {
    return num % 2 === 0;
}
console.log(`const isEven4 = ${isEven4}`)
console.log(`Is the #4 Even?: ${isEven1(4)}`)

console.log('')
console.log('       Arrow Functions Impicit Returns')
console.log('       with Parenthesis when its a single')
console.log('       statement')
console.log('       ----------')
const isEven5 = num => (
    num % 2 === 0
)
console.log(`const isEven5 = ${isEven5}`)
console.log(`Is the #5 Even?: ${isEven1(5)}`)

console.log('')
console.log('       Arrow Functions Impicit Returns')
console.log('       without Parenthesis on a single line')
console.log('       ----------')
const isEven6 = num => num % 2 === 0;
console.log(`const isEven6 = ${isEven6}`)
console.log(`Is the #6 Even?: ${isEven1(6)}`)

// The filter Method
console.log('')
console.log('       .filter() Practice w/Num Array')
console.log('       ----------')
const onlyEven = numbers.filter(num => {
    return num % 2 === 0;
})
for (num of onlyEven) {
    console.log(num)
}

console.log('')
console.log('       .filter() + .map() Practice w/Array Object')
console.log('       ----------')
const  goodMovies = movies
    .filter(movie => movie.score >= 95)
    .map(movie => movie.title);
for (movie of goodMovies) {
    console.log(movie)
}

// some & every Methods
console.log('')
console.log('       .some() Practice w/Num Array')
console.log('       ----------')
const someAbove = numbers.some(num => {
    return num > 5;
})
console.log(`Is 'some' of numbers above 5? ${someAbove}`)

console.log('')
console.log('       .every() Practice w/Num Array')
console.log('       ----------')
const everyEven = numbers.every(num => {
    return num % 2 === 0;
})
console.log(`Is 'every' of numbers even? ${everyEven}`)

// some & every Methods
console.log('')
console.log('       .reduce() Practice w/Num Array')
console.log('       ----------')
const total = numbers.reduce((acc, curr) => {
    return acc + curr;
})
console.log(`The total for Numbers is: ${total}`)

console.log('')
console.log('       .reduce() Practice w/Str Array')
console.log('       ----------')
const smallestName = names.reduce((min, curr) => {
    if (curr.length > min.length) {
        return min;
    }
    return curr
})
console.log(smallestName)

console.log('')
console.log('       .reduce() Practice w/Array Object')
console.log('       ----------')
const bestMovieEver = movies.reduce((best, curr) => {
    if (curr.score < best.score) {
        return best.title;
    }
    return curr.title;
})
console.log(bestMovieEver)

// setTimeout, setInterval & clearInterval
console.log('')
console.log('       setInterval(func, time)')
console.log('       random numbers will appear every 3 seconds')
console.log('       for 9 seconds')
console.log('       ----------')

const randomInterval = setInterval(msg => {
    console.log(`A random Number: (${Math.round(Math.random() * 10)}) after 3 seconds`)
}, 3000)

setTimeout(stop => {
    clearInterval(randomInterval)
}, 9000)

console.log('')
console.log('       setTimeout(func, time)')
console.log('       will appear near the end after 11 seconds')
console.log('       ----------')

setTimeout(msg => {
    console.log('Hello, this is setTimeout message will appear after the random numbers.')
}, 11000)