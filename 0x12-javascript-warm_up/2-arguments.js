#!/usr/bin/node
const args = process.argv;

if (args[2] !== undefined) {
  console.log('Argument found');
} else {
  console.log('No argument');
}
