var isPalindrome = function(x) {
    let y = [];   
    while(x>0){
        y.unshift(x%10);  
        x=x/10|0; 
    }
    // const z = String(x).split("").map(ele=>parseInt(ele));
    // console.log(11111111, z)

    console.log(y)
    let ans = true;
    if (Math.sign(x) == -1) return false

      for(let i=0; i < y.length; i++)
    {
        if (y[y.length-1-i] !== y[i]) { ans = false; break}
    }
    return ans;
};

console.log(isPalindrome(223));

