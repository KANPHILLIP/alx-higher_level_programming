#!/usr/bin/node
const args = process.argv.slice(2).map(arg => parseInt(arg, 10));
if (args.length === 0 || args.length === 1) {
  console.log(0);
} else {
  const max = Math.max(...args);
  console.log(max);
}
