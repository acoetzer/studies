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

const people = ['Andre', 'Vanya', 'Dary'];

// for (let i = 0; i < people.length; i++) {
//     console.log(people[i])
// }

for (let i = people.length - 1; i >= 0; i--) {
    console.log(people[i])
}