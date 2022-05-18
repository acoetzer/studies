// Random Color Generator
const colorBox = document.querySelectorAll('.colorBox')
const colorText = document.querySelectorAll('.colorText')
const gradient = document.querySelector('#gradient')
const btn = document.querySelector('#colorBtn')
const historyContainer = document.querySelector('#historyContainer')
// Selecting the Element Objects

function randomColor () {
    const r = Math.floor(Math.random() * 255)
    const g = Math.floor(Math.random() * 255)
    const b = Math.floor(Math.random() * 255)
    return `rgb(${r}, ${g}, ${b})`
}
// Making the random color function

function delHistory () {
    if (history.length > 30) {
        history.shift()
        history.shift()
        history.shift()
    }
}
// History function that limit the history array and removes anthing above 30.

function createEntry (arr) {
    const colorCodes = [...arr]

    const colorBoxHistory = document.createElement('div')
    colorBoxHistory.classList.add('colorBoxHistory')
    colorBoxHistory.style.backgroundImage = `linear-gradient(90deg, ${colorCodes})`
    
    historyContainer.append(colorBoxHistory)
}

let colorList = []
const history = []
// semi-global varaibles


for (let i = 0; i < colorBox.length; i++) {
    const color = randomColor();
    const colorCodes = [...colorList]
    colorList.push(color)
    history.push(color)
    delHistory()
    
    colorBox[i].style.backgroundColor = color
    colorText[i].innerText = color
    gradient.style.backgroundImage = `linear-gradient(90deg, ${colorCodes})`
    btn.style.backgroundImage = `linear-gradient(90deg, ${colorCodes})`
    btn.style.color = color
}
createEntry(colorList)
// load in of the page, to generate random colors

btn.addEventListener('click', function () {
    colorList = []
    for (let i = 0; i < colorBox.length; i++) {
        const color = randomColor();
        const colorCodes = [...colorList]
        colorList.push(color)
        history.push(color)
        delHistory()
        
        colorBox[i].style.backgroundColor = color
        colorText[i].innerText = color
        gradient.style.backgroundImage = `linear-gradient(90deg, ${colorCodes})`
        btn.style.backgroundImage = `linear-gradient(90deg, ${colorCodes})`
        btn.style.color = color
    }
    createEntry(colorList)
})

historyContainer.addEventListener('click', function (e) {
    e.target.className === 'colorBoxHistory' && e.target.remove()
})