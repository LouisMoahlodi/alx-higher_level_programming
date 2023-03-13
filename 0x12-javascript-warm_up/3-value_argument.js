#!/usr/bin/node
const args = process.argv.slice(2);
args.forEach((arg, index) => {
  console.log(`${arg}`);
});
