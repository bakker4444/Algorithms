// Is Unique

// Implement an algorithm to determine if a string has all unique characters.
// What is you cannot use additional data structure?

function isUniqueChars(str1) {
    if (str1.length > 128) {
        return false;
    } else {
        let boolArray = Array(128).fill(false);
        for (let i = 0; i < str1.length; i++) {
            if (boolArray[str1[i].charCodeAt(0)]) {
                return false;
            } else {
                boolArray[str1[i].charCodeAt(0)] = true;
            }
        }
        return true;
    }
}

console.log(isUniqueChars("asba"));
console.log(isUniqueChars("abcde"));
