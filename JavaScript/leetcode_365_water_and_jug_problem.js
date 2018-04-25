var canMeasureWater = function(x, y, z) {

    // edge condition handle
    if (x + y < z) {
        return false;
    }
    
    // fast find case handle
    if ((z % x == 0) || (z % y == 0) || (x + y == z)) {
        return true;
    }
    
    // general case
    return z % GCD(x, y) == 0
    
};


// find great common divisor
var GCD = (a, b) => {

    // Euclid Algorithm
    // 1. gcd(a, b) = gcd(b, a%b)
    // 2. gcd(n, 0) = n

    while (b != 0) {
        let temp = b;
        b = a % b;
        a = temp;
    }
    return a
}

console.log(canMeasureWater(3, 5, 4))
console.log(canMeasureWater(2, 6, 5))
