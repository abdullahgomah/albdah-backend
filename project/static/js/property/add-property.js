let sliderInputs = document.querySelectorAll('.slider_input'); 
let grid = document.querySelectorAll('.grid'); 
let markterTypeGrid =document.querySelector('#markter-type-grid'); 
let subItems =markterTypeGrid.querySelectorAll('.sub-item'); 


sliderInputs.forEach((input) => {
    input.addEventListener('input', () => {
        input.parentElement.parentElement.querySelector('.value').querySelector('span').textContent = input.value ;
    })
})

subItems.forEach((item) => {
    item.addEventListener('click', () => {
        subItems.forEach((x) => {
            x.classList.remove('fill') 
        })
        item.classList.add('fill') 
    })
})

grid.forEach((grid_item) => {
    grid_item.querySelectorAll('.item').forEach((item) => {
        item.addEventListener('click', () => {
            if (item.textContent == 'مسوق') {
                document.querySelector('#markter-type-grid').style.display = 'flex'; 
            } else { 
                document.querySelector('#markter-type-grid').style.display = 'none'; 
            }
            grid_item.querySelectorAll('.item').forEach((item) => {
                item.style.background = '#eee' 
                item.style.color = '#1e2957' 
            })
            item.style.background = "#1e2957"; 
            item.style.color = '#ffffff'
        })
    })
})

