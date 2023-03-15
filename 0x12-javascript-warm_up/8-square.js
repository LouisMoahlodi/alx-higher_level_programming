#!/usr/bin/node
const args = process.argv.slice(2);
const x = parseInt(args[0]);

if (isNaN(x)) {
  console.log('Missing size');
} else {
  let str = '';
  for (let i = 0; i < x; i++) {
    str += 'x';
  }
  for (let i = 0; i < x; i++) {
    console.log(str);
  }
}
