function makeRainbow () {
    const colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'];
    const rainbow = [...colors, ...colors, ...colors]
    const h2 = document.querySelectorAll('h2');

    for (let i = 0; i < h2.length; i++) {
        h2[i].style.color = rainbow[i]
    }
}

makeRainbow()