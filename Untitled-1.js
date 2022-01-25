/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */


// Output: [0,1]
 var twoSum = function(nums, target) {
     let sol;
     let i;
     let j;
    
    for( i=0; i < nums.length; i++){
        sol = nums.find(function(ele, k) {
            j=k;
            return ele+nums[i]==target
        })
        if (sol!=undefined && i !== j) break
    }
    if (sol!=undefined) return [ i,j];
    else return null
    
};
let nums  = [2,7,6,77] 
let target = 9
console.log(twoSum(nums, target));