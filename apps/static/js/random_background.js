document.addEventListener('DOMContentLoaded', function () {
    // Array of image URLs
    var imageArray = [
        '/media/interest_point/Jaizkibel-Mountain-1.jpg',
        '/media/interest_point/bidart-senix-1.jpg',
        '/media/interest_point/bidart-senix-1.jpg',
        '/media/interest_point/larra-belagua-1.jpg',
        '/media/interest_point/Lescun-1.jpg',
        '/media/interest_point/salies-de-bearn1.jpg',
        '/media/interest_point/saturraran.jpg',
        // Add more image URLs as needed
    ];

    // Get a random index from the imageArray
    var randomIndex = Math.floor(Math.random() * imageArray.length);

    // Set the background image
    document.body.style.backgroundImage = 'url(' + imageArray[randomIndex] + ')';
    console.log("imageArray[randomIndex]", imageArray[randomIndex]);
});
