#!/usr/bin/node

const request = require('request');

// Function to get character names in order for a specified movie ID
async function getStarWarsCharacters(movieId) {
  const filmUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

  // Fetch movie data to get character URLs
  request(filmUrl, async (error, response, body) => {
    if (error) {
      console.error(error);
      return;
    }

    // Parse JSON data
    const filmData = JSON.parse(body);

    if (!filmData.characters) {
      console.error('No characters found for the specified movie.');
      return;
    }

    // Function to fetch each character's name
    const fetchCharacterName = (url) =>
      new Promise((resolve, reject) => {
        request(url, (error, response, body) => {
          if (error) reject(error);
          resolve(JSON.parse(body).name);
        });
      });

    // Fetch and print character names in order
    for (const characterUrl of filmData.characters) {
      try {
        const name = await fetchCharacterName(characterUrl);
        console.log(name);
      } catch (error) {
        console.error(error);
      }
    }
  });
}

// Get the movie ID from command-line arguments
const movieId = process.argv[2];

if (!movieId) {
  console.error('Please provide a Movie ID');
  process.exit(1);
}

// Call the function with the provided Movie ID
getStarWarsCharacters(movieId);
