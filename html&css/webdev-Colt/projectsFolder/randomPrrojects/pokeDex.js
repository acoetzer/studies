// Where are we appending this too?
const container = document.querySelector('.container');

const url = 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/';

for (let i = 1; i <= 898; i++) {
    const span = document.createElement('span');
    const img = document.createElement('img');
    const h2 = document.createElement('h2');
    span.append(h2, img);
    h2.append(`Pokemon ${i}`);
    img.src = `${url}${i}.png`;

    container.append(span)
}