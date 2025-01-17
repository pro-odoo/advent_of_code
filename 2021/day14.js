const TEMPLATE = "SCVHKHVSHPVCNBKBPVHV";

const INSERTION_RULES = {
  SB: "B",
  HH: "P",
  VF: "N",
  BS: "S",
  NC: "C",
  BF: "H",
  BN: "H",
  SP: "H",
  BK: "H",
  FF: "N",
  VN: "B",
  FN: "C",
  FS: "S",
  PP: "F",
  ON: "H",
  FV: "F",
  KO: "F",
  PK: "H",
  VB: "S",
  HS: "B",
  NV: "O",
  PN: "S",
  VH: "B",
  OS: "P",
  BP: "H",
  OV: "B",
  HK: "S",
  NN: "K",
  SV: "C",
  PB: "F",
  SK: "F",
  FB: "S",
  NB: "K",
  HF: "P",
  FK: "K",
  KV: "P",
  PV: "F",
  BC: "S",
  FO: "N",
  HC: "F",
  CP: "B",
  KK: "F",
  PC: "S",
  HN: "O",
  SH: "H",
  CK: "P",
  CO: "F",
  HP: "K",
  PS: "C",
  KP: "F",
  OF: "K",
  KS: "F",
  NO: "V",
  CB: "K",
  NF: "N",
  SF: "F",
  SC: "P",
  FC: "V",
  BV: "B",
  SS: "O",
  KC: "K",
  FH: "C",
  OP: "C",
  CF: "K",
  VO: "V",
  VK: "H",
  KH: "O",
  NP: "V",
  NH: "O",
  NS: "V",
  BH: "C",
  CH: "S",
  CC: "F",
  CS: "P",
  SN: "F",
  BO: "S",
  NK: "S",
  OO: "P",
  VV: "F",
  FP: "V",
  OK: "C",
  SO: "H",
  KN: "P",
  HO: "O",
  PO: "H",
  VS: "N",
  PF: "N",
  CV: "F",
  BB: "H",
  VC: "H",
  HV: "B",
  CN: "S",
  OH: "K",
  KF: "K",
  HB: "S",
  OC: "H",
  KB: "P",
  OB: "C",
  VP: "C",
  PH: "K",
};

function extendedPoly(template, rules, steps) {
  let pairsInTemplates = initialPairs(template);
  const letters = initialCount(template);
  for (let i = 0; i < steps; i++) {
    pairsInTemplates = processPairs(pairsInTemplates, rules, letters);
  }
  return (
    Math.max(...Object.values(letters)) - Math.min(...Object.values(letters))
  );
}

function initialCount(template) {
  const letters = {};
  const chars = template.split("");
  for (let i = 0; i < chars.length; i++) {
    const char = chars.at(i);
    if (!(char in letters)) {
      letters[char] = 0;
    }
    letters[char]++;
  }
  return letters;
}

function initialPairs(template) {
  const pairsInTemplates = {};
  const chars = template.split("");
  for (let i = 0; i < chars.length - 1; i++) {
    const pair = `${chars.at(i)}${chars.at(i + 1)}`;
    if (!(pair in pairsInTemplates)) {
      pairsInTemplates[pair] = 0;
    }
    pairsInTemplates[pair]++;
  }
  return pairsInTemplates;
}

function processPairs(pairsInTemplates, insertion_rules, letters) {
  const newPairsInTemplates = {};
  for (const pair in pairsInTemplates) {
    const chars = pair.split("");
    if (pair in insertion_rules) {
      const char = insertion_rules[pair];
      if (!(char in letters)) {
        letters[char] = 0;
      }
      letters[char] += pairsInTemplates[pair];
      const pair1 = `${chars.at(0)}${char}`;
      const pair2 = `${char}${chars.at(1)}`;
      if (!(pair1 in newPairsInTemplates)) {
        newPairsInTemplates[pair1] = 0;
      }
      if (!(pair2 in newPairsInTemplates)) {
        newPairsInTemplates[pair2] = 0;
      }
      newPairsInTemplates[pair1] += pairsInTemplates[pair];
      newPairsInTemplates[pair2] += pairsInTemplates[pair];
    }
  }
  return newPairsInTemplates;
}

// Part 1
console.log(extendedPoly(TEMPLATE, INSERTION_RULES, 10)); //2712
// Part 2
console.log(extendedPoly(TEMPLATE, INSERTION_RULES, 40)); //8336623059567
