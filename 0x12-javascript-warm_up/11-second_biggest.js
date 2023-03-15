#!/usr/bin/node
function findSecondBiggest (args) {
  if (args.length < 2) {
    return 0;
  }

  const integers = args.map(arg => parseInt(arg));
  const sortedIntegers = integers.sort((a, b) => b - a);
  const secondBiggest = sortedIntegers[1];
  console.log(`${secondBiggest}`);
}

const args = process.argv.slice(2);

findSecondBiggest(args);
