const progressBar = document.querySelector('#progressBar')
const prev = document.querySelector('#prev')
const next = document.querySelector('#next')
const circle = document.querySelectorAll('.circle')

let currentActive = 1

next.addEventListener('click', function () {
    currentActive++

    if (currentActive > circle.length) {
        currentActive = circle.length
    }

    update()
})

prev.addEventListener('click', function () {
    currentActive--

    if (currentActive < 1) {
        currentActive = 1
    }

    update()
})

function update () {
    for (let i = 0; i < circle.length; i++) {
        if (i < currentActive) {
            circle[i].classList.add('active')
        } else {
            circle[i].classList.remove('active')
        }
    }

    const actives = document.querySelectorAll('.active')

    progressBar.style.width = (actives.length - 1) / (circle.length -1) * 100 + '%'

    if (currentActive === 1) {
        prev.disabled = true
    } else if (currentActive === circle.length) {
        next.disabled = true
    } else {
        prev.disabled = false
        next.disabled = false
    }
}