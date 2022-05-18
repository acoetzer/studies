const ul = document.querySelector('#todoList');
const form = document.querySelector('#form')

function createEntry (username, comment) {
    const newLi = document.createElement('li')
    const bTag = document.createElement('b')

    bTag.append(username)
    newLi.append(bTag)
    newLi.append(`: ${comment}`)
    ul.append(newLi)

}

form.addEventListener('submit', function (e) {
    e.preventDefault();
    const uName = this.elements.username
    const uComm = this.elements.comment

    createEntry(uName.value = 'defaultUser', uComm.value)
    uName.value = ''
    uComm.value = ''
})

ul.addEventListener('click', function (e) {
    e.target.nodeName === 'LI' && e.target.remove()
})
