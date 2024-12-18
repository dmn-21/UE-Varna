const body = document.querySelector('body')
// body.classList.add('dark')
// body.classList.remove('light')
body.className = 'dark'
body.style.textAlign = 'center'

const h1 = document.querySelector('h1')
h1.style.fontSize = '3rem'
h1.style.color = 'orange'
h1.innerHTML = 'Това е страница написана с JavaScript'

const p = document.querySelector('p')
p.textContent = 'от студент с ф.н. 117122'

const img = document.createElement('img')
img.src = 'https://e-learn.ue-varna.bg/pluginfile.php/1/theme_moove/sliderimage1/1733761672/parade-entry-building.jpg'
img.width = 600
img.height = 400
p.after(img)

const newP = document.createElement('p')
newP.innerHTML = 'Обучаващ се в <b>ИУ ВАРНА</b>'
img.after(newP)