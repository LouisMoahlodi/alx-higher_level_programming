#!/usr/bin/node
const args = process.argv.slice(2);
const x = parseInt(args[0]);

if (isNaN(x)) {
  console.log('Missing size');
} else {
  let i = 0;
  const str = 'x'.repeat(x);
  while (i < x) {
    console.log(str);
    i++;
  }
}
