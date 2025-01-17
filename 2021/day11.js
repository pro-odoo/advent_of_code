const puzzle = [
  "5433566276",
  "6376253438",
  "8458636316",
  "6253254525",
  "7211137138",
  "1411526532",
  "5788761424",
  "8677841514",
  "1622331631",
  "5876712227",
].map((row) => row.split("").map((value) => parseInt(value, 10)));

let flashes = 0;
let countStep = 0;

function octopusPart1(puzzle, steps) {
  for (let i = 0; i < steps; i++) {
    puzzle = step(puzzle);
  }
  return flashes;
}

function octopusPart2(puzzle) {
  let count = 1;
  while (true) {
    countStep = 0;
    puzzle = step(puzzle);
    if (countStep === puzzle.length * puzzle[0].length) {
      return count;
    }
    count++;
  }
}

function step(array) {
  array = increaseByOne(array);
  let positions = getFullEnergyPositions(array);
  while (positions.length) {
    for (const position of positions) {
      increaseAdjacent(array, position);
    }
    positions = getFullEnergyPositions(array);
  }
  return resetEnergy(array);
}

function increaseAdjacent(array, position) {
  const [x, y] = position;
  array[x][y] = 20;
  increasePosition(array, [x - 1, y - 1]);
  increasePosition(array, [x - 1, y]);
  increasePosition(array, [x - 1, y + 1]);
  increasePosition(array, [x, y - 1]);
  increasePosition(array, [x, y + 1]);
  increasePosition(array, [x + 1, y - 1]);
  increasePosition(array, [x + 1, y]);
  increasePosition(array, [x + 1, y + 1]);
}

function increasePosition(array, position) {
  const [x, y] = position;
  if (x in array && y in array[x]) {
    array[x][y] = increase(array[x][y]);
  }
}

function increase(value) {
  return value === 10 ? value : value + 1;
}

function getFullEnergyPositions(array) {
  const positions = [];
  for (let x = 0; x < array.length; x++) {
    for (let y = 0; y < array[x].length; y++) {
      if (array[x][y] === 10) {
        flashes += 1;
        countStep += 1;
        positions.push([x, y]);
      }
    }
  }
  return positions;
}

function increaseByOne(array) {
  return array.map((row) => row.map((value) => increase(value)));
}

function resetEnergy(array) {
  return array.map((row) => row.map((value) => (value > 10 ? 0 : value)));
}

// Part 1
console.log(octopusPart1(puzzle, 100)); // 1665
// Part 2
console.log(octopusPart2(puzzle)); // 235
