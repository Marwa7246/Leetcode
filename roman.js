
var romanToInt = function(s) {

    const conv = {
        "I":             1,
        "V":             5,
        "X":             10,
        "L":             50,
        "C":             100,
        "D":             500,
        "M":             1000,
    };
    let result=0;
    // let s = s.split("").map(ele=>conv[ele]);
    for (let i=1; i <= s.length; i++) {
        if ( i === s.length) 
        {
            result += conv[s[i-1]];
            break;
        }
        else if (conv[s[i]] > conv[s[i-1]])
        {
            result += conv[s[i]] - conv[s[i-1]];
            i++;
        }
        else 
        {
            result += conv[s[i-1]]
        }
    }
    return result;
}
console.log(romanToInt("LVIII"))
