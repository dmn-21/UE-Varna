const blocks = document.querySelectorAll('.block')
const button = document.querySelector('.button')

for (let i = 0; i < blocks.length; i++) {
   blocks[i].style.marginTop = `${i + 1}rem`
}

// const input = document.querySelector('input')


button.addEventListener('click', function () {
   // console.log(input.value)
   // button.textContent = input.value
   for (let i = 0; i < blocks.length; i++) {
      let newMargin = Number(blocks[i].textContent) % 10 + 1
      // if (newMargin > 10) newMargin -= 10
      blocks[i].style.marginTop = `${newMargin}rem`
      blocks[i].textContent = newMargin
   }
})

