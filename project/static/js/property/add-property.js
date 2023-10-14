let sliderInputs = document.querySelectorAll('.slider_input'); 
let grid = document.querySelectorAll('.grid'); 
let markterTypeGrid =document.querySelector('#markter-type-grid'); 
let subItems =markterTypeGrid.querySelectorAll('.sub-item'); 
let propertyInfoSection = document.querySelector('.property__info'); 
let propertyDetailsSection = document.querySelector('.property__details'); 
let propertyImgs = document.querySelector('.property__imgs');
let propertyLocation = document.querySelector('.property__location'); 
let propertyLocationNextPrev = document.querySelector('.property__location__next-prev'); 
let propertyFeatures = document.querySelector('.property__features'); 
let propertyFeaturesNextPrev = document.querySelector('.property__features__next-prev'); 
let rentTypeInput = document.querySelector("[name=rent_type_input]"); 
let advertiser_relation = document.querySelector('[name=advertiser_relation]'); 
let exclusiveInput = document.querySelector("[name=exclusive]"); 
let propertyImgsNextPrev = document.querySelector('.property__imgs__next-prev'); 
let overlayLayer = document.querySelector('.overlay-layer'); 
let noImgsPopup = document.querySelector('.on-imgs-popup');
let noImgsPopupYesBtn = document.querySelector('#no-imgs-popup-yes-btn'); 
let noImgsPopupNoBtn = document.querySelector('#no-imgs-popup-no-btn'); 
let imagesFileInput = document.querySelector('[name=property__imgs]'); 
let previewImgsContainer = document.querySelector('.preview_imgs_container'); 

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

let advertiser_relation_grid = document.querySelector('#advertiser_relation_grid') 
advertiser_relation_grid.querySelectorAll('.item').forEach((item) => {
    item.addEventListener('click', () => {
        advertiser_relation.value = item.textContent;  
        // console.log(advertiser_relation.value)
    })
})


markterTypeGrid.querySelectorAll('.sub-item').forEach((item) => {
    item.addEventListener('click', () => {
        if (item.textContent == "حصري") { 
            exclusiveInput.value = 1 
        } else { 
            exclusiveInput.value = 0 
        }
    })
 
})



let propertyInfoNextPrev = document.querySelector('.property__info__next-prev'); 
propertyInfoNextPrev.querySelector('.btn-next').addEventListener('click', () => {

    // check form validation 
    let inputs = propertyInfoSection.querySelectorAll('.input') 
    let inputsLen = inputs.length; 
    let counter = 0; 

    inputs.forEach((input) => {
        let inputElement = input.querySelector("input") 
        if (inputElement.value == "") {
            inputElement.style.border = "1px solid #dc3546"
            // console.log("نص فارغ")
        } else {
            counter = counter + 1; 
            inputElement.style.border = "1px solid #00000040"
            // console.log(inputElement.value); 
        }

        // console.log(counter) 
    })

    if (rentTypeInput.textContent == "" ) {
        rentTypeInput.parentElement.style.border= "1px solid #dc3546"; 
    } else { 
        counter += 1; 
        rentTypeInput.parentElement.style.border = "1px solid #00000040"
    }

    if (advertiser_relation.value == "") { 
        advertiser_relation_grid.style.border = '1px solid #dc3546'; 
    } else { 
        advertiser_relation_grid.style.border = '1px solid #00000040'; 
        counter +=1; 
    }

    if (counter == 5) { 
        propertyInfoSection.style.display = 'none' ; 
        propertyImgs.style.display = 'flex'; 
    }

}) 

// Handle Images Uploader
imagesFileInput.addEventListener('change', () => {
    console.log(imagesFileInput.files); 

    const files = imagesFileInput.files; 

    for (let i =0; i < files.length; i++ ) {
        
        // Get the File 
        const file = files[i]; 

        //  Create New Image Element 
        const image = document.createElement('img')
        image.classList.add('preview_img'); 

        // Read The URL of Image 
        const reader = new FileReader(); 
        reader.onload = function () {
            image.src = reader.result 
        }
        reader.readAsDataURL(file) 

        // Add Image To Container
        previewImgsContainer.appendChild(image); 

    }

}) ; 


propertyImgsNextPrev.querySelector('.btn-next').addEventListener('click', () => { 
    // GET FILE INPUT FOR PROPERTY IMAGES 
    let propertyImgsInput = document.querySelector('[name=property__imgs]'); 
    if (propertyImgsInput.files.length == 0 ) { 
        // SHOW CONFIRMATION POPUP 
        overlayLayer.style.display = 'block'; 
        noImgsPopup.style.display = 'block'; 

        
    } else { 
        // CONTINUE TO THE NEXT PAGE  
        propertyImgs.style.display = 'none'; 
        propertyLocation.style.display = 'block'; 
    }
})

noImgsPopupYesBtn.addEventListener('click', () => {
    propertyImgs.style.display = 'none'; 
    propertyLocation.style.display = 'block' ; 
    overlayLayer.style.display = 'none'; 
    noImgsPopup.style.display = 'none'; 
})

noImgsPopupNoBtn.addEventListener('click', () => {
    overlayLayer.style.display = 'none'; 
    noImgsPopup.style.display = 'none'; 
})



let propertyDetailsNextPrev = document.querySelector('.property__details__next-prev'); 
propertyDetailsNextPrev.querySelector('.btn-prev').addEventListener('click', () => {
    propertyDetailsSection.style.display = 'none' ;
    propertyLocation.style.display = 'block';
})


propertyDetailsNextPrev.querySelector('.btn-next').addEventListener('click', () => {
    propertyDetailsSection.style.display = 'none'; 
    propertyFeatures.style.display = 'block'; 
})

// propertyImgsNextPrev.querySelector('.btn-next').addEventListener('click', () => {
//     propertyImgs.style.display = 'none'; 
//     propertyLocation.style.display = 'block'
    
// })

propertyImgsNextPrev.querySelector('.btn-prev').addEventListener('click', () => {
    propertyImgs.style.display = 'none'; 
    propertyInfoSection.style.display = 'block'
    
})

propertyLocationNextPrev.querySelector('.btn-prev').addEventListener('click', () => {
    propertyLocation.style.display = 'none'; 
    propertyImgs.style.display = 'flex'
})

propertyLocationNextPrev.querySelector('.btn-next').addEventListener('click', () => {
    propertyLocation.style.display = 'none'; 
    propertyDetailsSection.style.display = 'block'
})


propertyFeaturesNextPrev.querySelector('.btn-prev').addEventListener('click', () => {
    propertyFeatures.style.display = 'none'; 
    propertyDetailsSection.style.display = 'block'
})

let roomCountGrid = document.querySelector('.room-count'); 
roomCountGrid.querySelectorAll('.item').forEach((item) => {
    item.addEventListener('click', () => {
        item.parentElement.querySelector("[name=room-input]").value = item.textContent; 
        console.log(item.parentElement.querySelector('[name=room-input]').value)
    })
})

let loungesCountGrid = document.querySelector('.lounges-count'); 
loungesCountGrid.querySelectorAll('.item').forEach((item) => {
    item.addEventListener('click', () => {
        item.parentElement.querySelector("[name=lounges-input]").value = item.textContent; 
        console.log(item.parentElement.querySelector('[name=lounges-input]').value)
    })
})


let bathroomCountGrid = document.querySelector('.bathroom-count'); 
bathroomCountGrid.querySelectorAll('.item').forEach((item) => {
    item.addEventListener('click', () => {
        item.parentElement.querySelector("[name=bathroom-input]").value = item.textContent; 
        console.log(item.parentElement.querySelector('[name=bathroom-input]').value)
    })
})


let propertyAgeGrid = document.querySelector('.property-age'); 
propertyAgeGrid.querySelectorAll('.item').forEach((item) => {
    item.addEventListener('click', () => {
        item.parentElement.querySelector("[name=property-age-input]").value = item.textContent; 
        console.log(item.parentElement.querySelector('[name=property-age-input]').value)
    })
})


let floorNumberGrid = document.querySelector('.floor-number'); 
floorNumberGrid.querySelectorAll('.item').forEach((item) => {
    item.addEventListener('click', () => {
        item.parentElement.querySelector("[name=floor-input]").value = item.textContent; 
        console.log(item.parentElement.querySelector('[name=floor-input]').value)
    })
})

let rentTypeGrid = document.querySelector('.rent-type') 
rentTypeGrid.querySelectorAll('.item').forEach((item) => {
    item.addEventListener('click', () => {
        item.parentElement.querySelector('[name=rent_type_input]').textContent = item.textContent
    })
})