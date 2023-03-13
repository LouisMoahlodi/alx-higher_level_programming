#!/usr/bin/node
const args = process.argv.slice(2);
let numArgs = 0;
for (let i = 0; i < args.length; i++) {
  numArgs++;
}

if (numArgs >= 1) {
  console.log(`${args[0]}`);
} else {
  console.log('No Argument');
}
