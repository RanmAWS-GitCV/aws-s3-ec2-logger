const prompt = require("prompt-sync")();


console.log('hello wonderland');

let BTLs = ['eatme_cake', 'drinkme_potion', 'blue_pipe']

class Alice { 
  constructor(name, size, mood) {
  this.name = name;
  this.size = size;
  this.mood = mood;
  }
};
console.log('alice wants to go to wonderland.')
console.log('Her wonderland chips are:', BTLs)
console.log("What should alice do in wonderland?")


function alice_grow() {
  const alice = new Alice("giant alice", 200, "unstopable")
  console.log('alice got big')
  console.log('she is now', alice.name)
  console.log('her new size is', alice.size,'%!')
  console.log("she's feeling", alice.mood)
}

function alice_shrink() {
  const alice = new Alice("mini alice", 50, "stealthy")
  console.log('alice got small')
  console.log('she is now', alice.name)
  console.log('her new size is', alice.size,'%!')
  console.log("she's feeling", alice.mood)
}

function alice_trip() {
  "like she's about to puke rainbows, meet an angel and never leave wonderland. all in all, great!"
  const alice = new Alice("tripping alice", 100, "like she's about to puke rainbows, meet an angel and never leave wonderland. all in all, pretty wonderful!")
  console.log("alice tried the blue caterpillar's pipe")
  console.log('she is now', alice.name)
  console.log("she's feeling", alice.mood)
}

let user_choice = prompt("Choose from chip 1, 2, or 3- ")

if (user_choice == 1) {
  alice_grow()
}

if (user_choice == 2) {
  alice_shrink()
}

if (user_choice == 3) {
  alice_trip()
}