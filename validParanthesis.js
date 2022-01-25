var isValid3 = function(s) {
    let openedParenthesisArray = [];
    console.log(openedParenthesisArray[0])
    const openParenthesis = { 
        "(": ")", 
        "{": "}", 
        "[": "]" 
        };

 for (let i = 0; i < s.length; i++) {
   const currentParenthesis = s[i];

   if (openParenthesis[currentParenthesis]) {
     openedParenthesisArray.unshift(currentParenthesis);
    } else {
     if (currentParenthesis === openParenthesis[openedParenthesisArray[0]]) {
       openedParenthesisArray.shift();
 
     } else {
       return false;
     }
   }
 }

 return openedParenthesisArray.length === 0;
   
};

console.log(isValid3(")([])()"))