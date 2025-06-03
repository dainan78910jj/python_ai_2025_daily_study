console.log("Problem 1: SLEEPING IN");

const sleepln = (weekday, vacation) => {
  if (weekday == false || vacation == true) {
    return true;
    // } else if (weekday == true || vacation == false) {
    //   return false;
  } else {
    return false;
  }
};

console.log(sleepln(true, false));
console.log(sleepln(true, true));
console.log(sleepln(false, false));
console.log(sleepln(false, true));


console.log("Problem 2: MONKEY TROUBLE");
const monkeyTrouble = (aSmile = false, bSmile = true) => {
  if (
    (aSmile == true && bSmile == true) ||
    (aSmile == false && bSmile == false)
  ) {
    return true;
  } else {
    return false;
  }
};

console.log(monkeyTrouble(true, false));
console.log(monkeyTrouble(true, true));
console.log(monkeyTrouble(false, false));
console.log(monkeyTrouble(false, true));

console.log("Problem 3: STRING TIMES");

const stringTimes = (string, nonNegativeInt) => {
  if (string.length >= 0 && nonNegativeInt >= 0) {
    console.log(string.repeat(nonNegativeInt));
  } else {
    console.log("Invalid input type!");
  }
};
stringTimes("abc", 0);
stringTimes("Hi", 7);
stringTimes("", 0);
stringTimes("hi", -9);
stringTimes("", 2);

console.log("Problem 4: LUCKY SUM");

const luckySum1 = (a, b, c) => {
  if (a == 13) {
    return 0;
  } else if (b == 13) {
    return a;
  } else if (c == 13) {
    return a + b;
  } else {
    return a + b + c;
  }
};

const luckySum2 = (...args) => {
  let sum = 0;
  for (let arg of args) {
    if (arg == 13) {
      break;
    } else {
      sum += arg
    }
  }
  return sum;
}

console.log(luckySum1(13, 5, 10));
console.log(luckySum1(1, 13, 10));
console.log(luckySum1(1, 3, 13));
console.log(luckySum1(1, 2, 3));

console.log(luckySum2(13, 5, 10));
console.log(luckySum2(1, 13, 10));
console.log(luckySum2(1, 3, 13));
console.log(luckySum2(1, 2, 3));
console.log(luckySum2(1, 2, 3, 4, 5, 6));

console.log("Problem 5");
/* solution 1
const caughtSpeeding = (speed, isBirthday) => {
  if ((speed <= 60 && isBirthday == false) || (speed <= 65 && isBirthday == true)) {
    return 0
  } else if ((speed <= 80 && isBirthday == false) || (speed <= 85 && isBirthday == true)) {
    return 1
  } else {
    return 2
  }
};
*/
/* solution 2 */
const caughtSpeeding = (speed, isBirthday) => {

  const offset = isBirthday ? 5 : 0;
  const limit_0 = 60 + offset;
  const limit_1 = 80 + offset;

  if (speed <= limit_0) {
    return 0
  } else if (speed <= limit_1) {
    return 1
  } else {
    return 2
  }
};

console.log(caughtSpeeding(60, false));
console.log(caughtSpeeding(65, true));
console.log(caughtSpeeding(70, false));
console.log(caughtSpeeding(85, true));
console.log(caughtSpeeding(90, false));
console.log(caughtSpeeding(89, true));

