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
let videoFileInput = document.querySelector('[name=property__video]'); 
let previewVideoContainer = document.querySelector('.preview_video_container'); 

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

    if (counter == 4) { 
        propertyInfoSection.style.display = 'none' ; 
        propertyImgs.style.display = 'flex'; 
    }

}) 

// Handle Images Uploader
imagesFileInput.addEventListener('change', () => {
    
    // Remove All Images
    previewImgsContainer.innerHTML = ''; 

    const files = imagesFileInput.files; 

    const selectedFiles = Array.from(files);

    console.log(selectedFiles); 

    for (let i =0; i < files.length; i++ ) {
        
        // Get the File 
        const file = files[i]; 

        // Create New Image Container 
        const imageContainer = document.createElement('div'); 
        imageContainer.classList.add('image-container'); 
        
        // image container header 
        const imageContainerHeader = document.createElement('div'); 
        imageContainerHeader.classList.add('image-container-header'); 

        // create 'x' button 
        const delButton = document.createElement('div'); 
        delButton.classList.add('del-btn'); 
        delButton.innerHTML = '<i class="fa-solid fa-x"></i>'; 

        delButton.addEventListener('click', () => {
            // Remove Image Container From Preview Images Container
            previewImgsContainer.removeChild(imageContainer); 

            // Remove The Image From File List to Set new file list 
            // Remove the corresponding file from the selectedFiles array
            const index = selectedFiles.indexOf(file);
            if (index > -1) {
                selectedFiles.splice(index, 1);
            }

            // Update the file input's files property with the modified selectedFiles array
            const remainingFileList = new DataTransfer() ; 
            selectedFiles.forEach((file) => {
                remainingFileList.items.add(file); 
            }) 

            imagesFileInput.files = remainingFileList.files

            // console.log(imagesFileInput.files); 
        })

        imageContainerHeader.appendChild(delButton); 
        
        //  Create New Image Element 
        const image = document.createElement('img')
        image.classList.add('preview_img'); 


        imageContainer.appendChild(imageContainerHeader)
        imageContainer.appendChild(image)

        // Read The URL of Image 
        const reader = new FileReader(); 
        reader.onload = function () {
            image.src = reader.result 
        }
        reader.readAsDataURL(file) 

        // Add Image To Container
        previewImgsContainer.appendChild(imageContainer); 
    }

}) ; 

// Handle Video Uploader 
videoFileInput.addEventListener('change', () => {
    // Reset the preview video container 
    previewVideoContainer.innerHTML = ""; 

    const file = videoFileInput.files[0]; 
    const reader = new FileReader() 
    reader.onload = () => {
        const video = document.createElement('video') 
        video.classList.add("preview_video"); 
        video.setAttribute('controls', "true") 
        video.src = reader.result; 
        previewVideoContainer.appendChild(video) ; 
    }

    reader.readAsDataURL(file)
})

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