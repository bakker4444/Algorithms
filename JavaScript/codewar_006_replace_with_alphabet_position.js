// Replace With Alphabet Position
//
// In this kata you are required to, given a string, replace every letter with its position in the alphabet.
// If anything in the text isn 't a letter, ignore it and don't return it.
//
// a being 1, b being 2, etc.
//
// As an example:
// alphabet_position("The sunset sets at twelve o' clock.")
// Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" as a string.


function alphabetPosition(text) {

  var newText = "";
  var dict1 = {
    "a": "1", "b": "2", "c": "3", "d": "4", "e": "5",
    "f": "6", "g": "7", "h": "8", "i": "9", "j": "10",
    "k": "11", "l": "12", "m": "13", "n": "14", "o": "15",
    "p": "16", "q": "17", "r": "18", "s": "19", "t": "20",
    "u": "21", "v": "22", "w": "23", "x": "24", "y": "25",
    "z": "26"
  };

  // replace text code to newText variable
  for (var i = 0; i < text.length; i++) {
    let char1 = text[i].toLowerCase();
    if (char1 in dict1) {
      newText += dict1[char1] + " ";
    }
  }

  // remove last character which is empty space
  newText = newText.substring(0, newText.length-1);
  return newText;
}

// Result
console.log(alphabetPosition("The sunset sets at twelve o' clock."));

// Expected result
console.log("20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11")