#!/usr/bin/node
const args = process.argv[2];

if (args === undefined || isNaN(parseInt(args))) {
  console.log('Missing size');
}
const size = parseInt(args);

for (let i = 0; i < size; i++) {
  let row = '';
  for (let j = 0; j < size; j++) {
    row += 'x';
  }
  console.log(row);
}
