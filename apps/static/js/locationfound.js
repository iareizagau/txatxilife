map.on('locationfound', function (e) {
    console.log('Location found:', e);
    var km = 150;
    var km2m = km * 1000;
    circle = new L.circle(e.latlng, km2m).setStyle({color: 'green'}).addTo(map);
});