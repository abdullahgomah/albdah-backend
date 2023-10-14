let latInput = document.querySelector('#lat-input'); 
let lngInput = document.querySelector('#lng-input'); 


async function initMap() {

    const { AdvancedMarkerElement } = await google.maps.importLibrary("marker");

    const map = new google.maps.Map(document.getElementById("map"), {
        mapId: "6a7f4f4e7a7f5b47",
        center: { lat: 23.885942, lng: 45.079163 }, // Coordinates for Saudi Arabia
        zoom: 24, 
        zoomControl: false, 
        mapTypeId: "roadmap",
        mapTypeControl: false, 
        fullscreenControl: false, 
        gestureHandling: "greedy", 
        streetViewControl: false, 
    });

    var userMarker = new google.maps.Marker({
        map: map,
        draggable: true, 
        title: "Your Location",
        animation: google.maps.Animation.DROP, 
        position: {lat: 23.885942, lng: 45.079163}
    });


    userMarker.addListener('dragend', function () {
        const position = userMarker.position 
        const lat = position.lat(); // دوائر العرض
        const lng = position.lng(); // خطوط الطول
        latInput.value = lat ;
        lngInput.value = lng; 
        // console.log(lat)
        // console.log(lng)
    })


    document.getElementById('myLocationButton').addEventListener('click', function() {
        // Check if geolocation is available in the user's browser
        if (navigator.geolocation) {
            // Get the user's current location
            navigator.geolocation.getCurrentPosition(function(position) {
                var userLatLng = new google.maps.LatLng(position.coords.latitude, position.coords.longitude);
    
                // Set the map's center to the user's location
                map.setCenter(userLatLng);
    
                // Set the marker's position to the user's location
                userMarker.setPosition(userLatLng);
    
                // Optionally, you can open an info window or perform other actions here
            }, function(error) {
                // Handle any errors here, such as permission denied or unable to retrieve location
                console.error('Error getting user location:', error);
            });
        } else {
            // Geolocation is not supported in this browser
            alert('Geolocation is not supported in your browser.');
        }
    });
  
    // const AdvMarker = new AdvancedMarkerElement ({
    //     position: { lat: 24.7136, lng: 46.6753 }, 
    //     map: map, 
    //     content: priceTag 
    // })



    // cities.forEach((city) => {

    //     const priceTag = document.createElement("div");

    //     priceTag.className = "price-tag";
    //     priceTag.textContent = "10 مليون"
        
    //     const marker = new AdvancedMarkerElement ({
    //         map,
    //         position: { lat: city[1], lng: city[2] },
    //         content: priceTag, 
    //         // icon: './house(1).png',
    //     });


    
    //     marker.addListener('click', function () {
    //         // alert(city[0]) 
    //         infoCard.style.display = 'block'; 
    //         infoCardH3.textContent = city[0]; 

    //         mapOptions.style.display = 'none'; 
            
    //     });



    // })


    // document.querySelector("#btn_satellite").addEventListener('click', function() {
    //     map.setMapTypeId('satellite')
    // })


    // document.querySelector("#btn_roadmap").addEventListener('click', function() {
    //     map.setMapTypeId('roadmap')
    // })

    // document.querySelector("#btn_terrain").addEventListener('click', function() {
    //     map.setMapTypeId('terrain')
    // })


}



window.initMap = initMap;
// initMap(); 



