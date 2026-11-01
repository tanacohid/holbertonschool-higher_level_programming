#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length <= 1) {
  console.log(0);
} else {
  const sortedNumbers = args.map(Number).sort((a, b) => b - a);
  console.log(sortedNumbers[1]);
}
