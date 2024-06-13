#!/usr/bin/node
/***
 * @fileoverview Star Wars API
 */

const request = require('request');
const url = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}/`;

request(url, async (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const characters = JSON.parse(body).characters;
    for (const character of characters) {
      await new Promise((resolve, reject) => {
        request(character, (error, response, body) => {
          if (error) {
            reject(error);
          } else {
            console.log(JSON.parse(body).name);
            resolve();
          }
        });
      });
    }
  }
});
