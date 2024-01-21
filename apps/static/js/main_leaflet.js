var map = L.map('map').setView([latitude, longitude], zoom_map);

// google street
var googleStreets = L.tileLayer('http://{s}.google.com/vt/lyrs=m&x={x}&y={y}&z={z}', {
    maxZoom: 20,
    subdomains: ['mt0', 'mt1', 'mt2', 'mt3']
});

//google satellite
var googleSat = L.tileLayer('http://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}', {
    maxZoom: 20,
    subdomains: ['mt0', 'mt1', 'mt2', 'mt3']
});

var CartoDB_Positron = L.tileLayer('https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png', {
	maxZoom: 20
});

var CartoDB_Voyager = L.tileLayer('https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png', {
	maxZoom: 20
}).addTo(map);


var baseMaps = {
    'Positron': CartoDB_Positron,
    'Voyager': CartoDB_Voyager,
    'Street': googleStreets,
    "Satellite": googleSat,
};


const layersControl = L.control.layers(baseMaps, null, { collapsed: false }).addTo(map);

var locateControl = L.control.locate({
    flyTo: true,
    keepCurrentZoomLevel: true,
    initialZoomLevel: 10
    }).addTo(map);

