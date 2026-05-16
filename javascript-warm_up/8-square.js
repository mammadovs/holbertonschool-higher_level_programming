#!/usr/bin/node
const x = Number(process.argv[2]);

if (Number.isInteger(x)) {
  for (let i = 0; i < x; i++) {
    console.log('X'.repeat(x));
  }
} else {
  console.log('Missing size');
}
