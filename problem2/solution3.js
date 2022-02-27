let fibSum = 0;
let [first, second] = [0, 1];

while (second < 4000000) {
    if (second % 2 === 0) {
        fibSum += second;
    }
    [first, second] = [second, first + second];
}

console.log(fibSum);
