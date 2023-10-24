#!/usr/bin/node

const process = require('process');
const path = require('path');
const file = process.argv[2];

path.readFile(file, 'utf8', function (error, data) {

  if (error) {
    console.log(error);
  } else {
    process.stdout.write(data);
  }
});
