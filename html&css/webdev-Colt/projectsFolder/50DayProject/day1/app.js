const images = ['https://images.unsplash.com/photo-1589984662646-e7b2e4962f18?crop=entropy&cs=tinysrgb&fm=jpg&ixlib=rb-1.2.1&q=80&raw_url=true&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1770', 'https://images.unsplash.com/photo-1581375074612-d1fd0e661aeb?crop=entropy&cs=tinysrgb&fm=jpg&ixlib=rb-1.2.1&q=80&raw_url=true&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1771', 'https://images.unsplash.com/photo-1597975371270-cf80e4f54921?crop=entropy&cs=tinysrgb&fm=jpg&ixlib=rb-1.2.1&q=80&raw_url=true&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1770', 'https://images.unsplash.com/photo-1581375321224-79da6fd32f6e?crop=entropy&cs=tinysrgb&fm=jpg&ixlib=rb-1.2.1&q=80&raw_url=true&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1770', 'https://images.unsplash.com/photo-1581375383680-7101dc5cb5f4?ixlib=rb-1.2.1&raw_url=true&q=80&fm=jpg&crop=entropy&cs=tinysrgb&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1769'];

const panels = document.querySelectorAll('.panels')


for (let i = 0; i < panels.length; i++) {
    panels[i].style.backgroundImage = `url(${images[i]})`
    panels[i].addEventListener('click', function () {
        removeActiveClasses()
        panels[i].classList.add('active')
    })
}

function removeActiveClasses () {
    for (let panel of panels) {
        panel.classList.remove('active')
    }
}