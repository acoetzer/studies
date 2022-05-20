// RANDOM COLOR GENERATOR
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

/* 
function delHistory () {
    if (history.length > 30) {
        history.shift()
        history.shift()
        history.shift()
    }
}
*/
// History function that limit the history array and removes anthing above 30.

function createEntry (arr) {
    const colorBoxHistory = document.createElement('div')
    colorBoxHistory.classList.add('colorBoxHistory')
    colorBoxHistory.style.backgroundImage = `linear-gradient(90deg, ${arr[0]}, ${arr[1]}, ${arr[2]})`
    
    historyContainer.append(colorBoxHistory)
}
// to create a color box entry for history

let colorList = []
// const history = []
// semi-global varaibles


for (let i = 0; i < colorBox.length; i++) {
    const color = randomColor();

    colorList.push(color)
    /*
    history.push(color)
    delHistory()
    */
    colorBox[i].style.backgroundColor = color
    colorText[i].innerText = color
    gradient.style.backgroundImage = `linear-gradient(90deg, ${colorList[0]}, ${colorList[1]}, ${colorList[2]})`
    btn.style.backgroundImage = `linear-gradient(90deg, ${colorList[0]}, ${colorList[1]}, ${colorList[2]})`
    btn.style.color = color
}
createEntry(colorList)
// load in of the page, to generate random colors

btn.addEventListener('click', function () {
    colorList = []
    for (let i = 0; i < colorBox.length; i++) {
        const color = randomColor();
        colorList.push(color)
        /*
        history.push(color)
        delHistory()
        */
        
        colorBox[i].style.backgroundColor = color
        colorText[i].innerText = color
        gradient.style.backgroundImage = `linear-gradient(90deg, ${colorList[0]}, ${colorList[1]}, ${colorList[2]})`
        btn.style.backgroundImage = `linear-gradient(90deg, ${colorList[0]}, ${colorList[1]}, ${colorList[2]})`
        btn.style.color = color
    }
    createEntry(colorList)
})
// Click Event to generate a random color and vaious other things.

historyContainer.addEventListener('click', function (e) {
    e.target.className === 'colorBoxHistory' && e.target.remove()
})
// Event Delegation for removing color History boxes.

// END OF RANDOM COLOR GENERATOR



// GROCERY LIST
const form = document.querySelector('#gForm')
const gContainer = document.querySelector('#gApp')
const gQty = document.querySelector('#gQty')
const gList = document.querySelector('#gList')
// 

function createGList (qty, items) {
    const newQty = document.createElement('li')
    newQty.append(qty)
    gQty.append(newQty)

    const newItems = document.createElement('li')
    newItems.append(items)
    gList.append(newItems)
}
// 

form.addEventListener('submit', function (e) {
    e.preventDefault()
    const qtyInput = this.elements.qty
    const itemsInput = this.elements.items

    createGList(qtyInput.value, itemsInput.value)
    qtyInput.value = ''
    itemsInput.value = ''
})
// 

gContainer.addEventListener('click', function (e) {
    e.target.nodeName === 'LI' && e.target.remove()
})
// 

// END OF GROCERY LIST



// TODO LIST

const todoForm = document.querySelector('#todoForm');
const todoContainer = document.querySelector('#todoContainer');

function createToDo (input) {
    const newLi = document.createElement('li')
    newLi.append(input)

    todoContainer.append(newLi)
}

todoForm.addEventListener('submit', function (e) {
    e.preventDefault()
    const todoInput = this.elements.todoInput

    createToDo(todoInput.value)
    todoInput.value = ''
})

todoContainer.addEventListener('click', function (e) {
    e.target.nodeName === 'LI' && e.target.remove()
})

// END OF TODO LIST



// LIVE UPDATE
const liveText = document.querySelector('#liveText')
const liveInput = document.querySelector('#liveInput')

liveInput.addEventListener('input', function (e) {
    if (!this.value) {
        liveText.innerText = 'Live Update Text'
    } else {
        liveText.innerText = this.value
    }

})

// END OF LIVE UPDATE
