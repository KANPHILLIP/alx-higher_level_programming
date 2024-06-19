#!/usr/bin/node
const args = process.argv[2];

if (args === undefined || isNaN(parseInt(args))) {
  console.log('Missing size');
} else {
  for (let i = 0; i < parseInt(args); i++) {
    let row = '';
    for (let b = 0; b < parseInt(args); b++) {
      row += 'X';
    }
    console.log(row);
  }
}
