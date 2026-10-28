#!/usr/bin/node

const num = parseInt(process.argv[2]);

if (isNaN(num)) {
  console.log('Missing number of occurrences');
} else {
  for (let count = 0; count < num; count++) {
    console.log('C is fun');
  }
}
