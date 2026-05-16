#!/usr/bin/node
const args = process.argv.slice(2);

if (args.length < 2) {
  console.log(0);
} else {
  let max1 = -Infinity;
  let max2 = -Infinity;

  for (let i = 0; i < args.length; i++) {
    const num = Number(args[i]);

    if (num > max1) {
      max2 = max1;
      max1 = num;
    } else if (num > max2) {
      max2 = num;
    }
  }

  console.log(max2);
}
