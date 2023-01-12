"use strict"
let userWeather = prompt('What is the weather outside?');
let fahrenheit = (9 / 5) * parseInt(userWeather) + 32;
alert(`Degree celsius is ${userWeather}C. Fahrenheit is ${fahrenheit.toFixed(1)}F.`);