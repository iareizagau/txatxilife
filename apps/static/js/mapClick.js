map.on('click', function (e) {
    console.log("click", e);
    if (circle) {
        map.removeLayer(circle);
        circle = new L.circle();
        }
    if (markersSearch) {
        map.removeLayer(markersSearch);
        markersSearch = new L.markerClusterGroup();
    }
    if (click_mark) {
        map.removeLayer(click_mark);
        click_mark = new L.markerClusterGroup();
    }
    var location_ = e.latlng;

    L.esri.Geocoding
        .reverseGeocode({
            apikey: "AAPK045ad3a5e5244010b70c93dd7bbe7a7dmtDT8iQfEQ9WzIZUJ_gQ-A9vgKJ-DX8wRmZO6C7TLTWhWK7DTgtWqYOw6qOzVusD"
        })
        .latlng(e.latlng)
        .language("eu")
        .run(function (error, result) {
            console.log("result", result);
            console.log("CountryCode", result['address']['CountryCode']);
            document.getElementById('id_country_code').value = result['address']['CountryCode'];
            document.getElementById('id_country_name').value = result['address']['CntryName'];
            document.getElementById('id_region').value = result['address']['Region'];
            document.getElementById('id_region_abbr').value = result['address']['RegionAbbr'];
            document.getElementById('id_subregion').value = result['address']['Subregion'];
            document.getElementById('id_city').value = result['address']['City'];
            document.getElementById('id_postal').value = result['address']['Postal'];
            document.getElementById('id_address').value = result['address']['Address'];

            document.getElementById('id_longitude').value = e.latlng["lng"];
            document.getElementById('id_latitude').value = e.latlng["lat"];
        });

    });