#!/usr/bin/node
args1 = process.argv[2];
args2 = process.argv[3];
function add(a, b){
	return a + b;
}
const a = parseInt(args1);
const b =parseInt(args2);
console.log(add(a, b));
