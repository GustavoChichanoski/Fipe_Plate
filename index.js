'use strict';

const fs = require('fs');
const sinespApi = require('sinesp-api');

let vehicle = search_plate('AUA7318')

async function search_plate(plate){
    const vehicle = await sinespApi.search(plate);
    let json = JSON.stringify(vehicle);

    fs.writeFileSync('AUA7318.json', json);
}