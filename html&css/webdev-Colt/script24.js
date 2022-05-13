// PokeDex Demo
const exampleBoard = document.querySelector('.poke')
const url = 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/'

for (let i = 1; i <= 151; i++) {
    const num = document.createElement('span');
    num.classList.add('pokeNum')
    num.append(i)
    const img = document.createElement('img');
    img.src = `${url}${i}.png`
    const span = document.createElement('span');
    span.append(num, img)
    span.classList.add('pokeSpan')

    exampleBoard.append(span)
}


// Rainbow h2's Demo
// const rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'];
// const colors = [...rainbow, ...rainbow, ...rainbow];

// const h2 = document.querySelectorAll('h2, h3');

// let i = 0;

// for (let selection of h2) {
//     selection.style.textTransform = 'uppercase'
//     selection.style.textDecoration = 'underline'
//     selection.style.color = colors[i]
//     i++
// }