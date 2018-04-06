/**
 * @param {number[]} nums
 */

var NumArray = function(nums) {
    this.sumArray = []
    var sumlocal = 0
    for (var i=0; i < nums.length; i++) {
        sumlocal += nums[i]
        this.sumArray.push(sumlocal)
    }
};

/** 
 * @param {number} i 
 * @param {number} j
 * @return {number}
 */
NumArray.prototype.sumRange = function(i, j) {
    if (i==0) {
        return this.sumArray[j]
    } else {
        return this.sumArray[j] - this.sumArray[i-1]
    }
};

/** 
 * Your NumArray object will be instantiated and called as such:
 * var obj = Object.create(NumArray).createNew(nums)
 * var param_1 = obj.sumRange(i,j)
 */

var nums = [-2, 0, 3, -5, 2, -1];

var newarray1 = new NumArray(nums);
console.log(newarray1.sumRange(0,2))
console.log(newarray1.sumRange(2,5))
console.log(newarray1.sumRange(0,5))

