let factor_num = 600851475143;
let i = 2;

while (i * i <= factor_num) {
    if (factor_num % i) {
        i += 1;
    } else {
        factor_num /= i;
    }
}

console.log(factor_num);