/**
 * The MarkerClusterGroup
 * @type {L.MarkerClusterGroup}
 */
var markers = new L.MarkerClusterGroup();

/**
 * The Map object.
 * @type {L.map}
 */
var map = null;

/**
 * Location Geocoding cache object.
 * @type {Object}
**/
var location_cache = {};

/**
 * Keeps map focused
 * @type {Array}
**/
var bounds = [];

/**
 * Icon theme list
 * @type {Array}
**/
var icons = [];

/**
 * Icons count
 * @type {Integer}
 */
var icon_length = 0;

/**
 * Default Marker Icon
 * @type {L.Icon.Default}
 */
var default_icon = new L.Icon.Default();

/**
 * Countries to be skipped
 * @type {Object}
 */
var skip_city_country_keywords = {}

// Provider of templating
String.prototype.format = function() {
    var args = arguments;
    return this.replace(/{(\d+)}/g, function(match, number) { 
	return typeof args[number] != 'undefined'
	    ? args[number]
	    : match;
    });
};

// This function add 1km of random offset to city points to avoid overlapping
function markerOffset(location) {
    var lat = location[0] + (Math.random() - 0.5) / 1500;
    var lng = location[1] + (Math.random() - 0.5) / 1500;
    return [lat, lng];
}

// Query geocoding service for lat, long
function geocode_location(city, country) {
    var location_query = '';
    if (city != '') {
	location_query = city;
    }

    if (country != '') {
	if (location_query != '') {
	    location_query += ',' + country;
	} else {
	    location_query = country;
	}
    }

    var data = {q: location_query,
		format: 'json'}
    
    var url = ' http://nominatim.openstreetmap.org/search';
    $.ajax({
	url: url,
	dataType: 'json',
	data: data,
	type: 'GET',
	async: false,
	success: function (data) {
	    if (data.length > 0) {
		var location = data[0];
    		location_cache[location_query] = [location.lat, location.lon];
	    }
	}
    });
}

// Add marker
function add_marker(mission, k) {
    var location_name = mission.city;
    if (location_name != '') {
	location_name += ',' + mission.country;
    } else {
	location_name = mission.country;
    }
    
    if (!location_cache[location_name]) {
    	if (!mission.latlng) {
	    // End it if the country is marked as skipped
	    if (!(mission.country in skip_city_country_keywords) &&
	        !(mission.city in skip_city_country_keywords)) {
    		// If cached location is not found, geocode location
    		geocode_location(mission.city, mission.country);
	    }
    	} else {
    	    location_cache[location_name] = mission.latlng.split(',');
	    
    	}
    }

    var coord = location_cache[location_name]
    if (coord) {
	// Add offset to city location
	var latlng = markerOffset(coord);

	// Rotate icons if icons are found
	if (icons) {
    	    var icon = icons[k % icon_length];
	} else {
	    var icon = default_icon;
	}

	var marker = L.marker(latlng, {icon: icon});

	// Compose info window
	var info_template = $("#info-template").html();
	var info_content = info_template.format(mission.title,
    						mission.description,
    						mission.members,
                            mission.startDate,
                            mission.endDate,
                            mission.office,
                            mission.theme,
    						mission.url);
    
	marker.bindPopup(info_content);
	
	markers.addLayer(marker);    
	bounds.push(latlng);
    }
}

function initializeMap(node, endpoint, config) {
    // Populate icons
    if (config) {
	if (config.icons){
	    for (var i in config.icons) {
		var icon = new L.Icon({iconUrl: config.icons[i]});
		icons.push(icon);
	    }
	    icon_length = icons.length;
	}
	
	if (config.skip_keywords) {
	    for (var keyword in config.skip_keywords) {
		skip_city_country_keywords[config.skip_keywords[keyword]] = 0;
	    }
	}
    }

    // Default zoom to Kuala Lumpur
    map = new L.map(node, {markerZoomAnimation: false});
    map.setView([3.139003, 101.686855], 1);

    // create the tile layer with correct attribution
    var osmUrl = 'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';
    var osmAttrib = 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors';
    var osm = new L.TileLayer(osmUrl, {minZoom: 1, maxZoom: 20, attribution: osmAttrib});

    map.addLayer(osm);

    $.getJSON(endpoint, function(data) {
    	if (data) {
    	    var data_count = data.length;
    	    $.each(data, function (k, v) {
    		// Process map markers
    	    	add_marker(v, k);
		if (k + 1 == data_count) {
		    // Add Clusterer
		    map.addLayer(markers);
		    
		    // Map center between markers
		    var mapbound = new L.LatLngBounds(bounds);
		    map.fitBounds(mapbound);
		}
    	    })
    	}
    });

}
