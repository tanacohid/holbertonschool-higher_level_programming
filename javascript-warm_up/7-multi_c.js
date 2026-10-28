#!/usr/bin/node

const num = parseInt(process.argv[2]);

if (isNaN(num)) {
  console.log('Missing number of occurrences');
} else {
  for (let count = 0; num.length < count; count++);
    console.log('C is fun');
}
