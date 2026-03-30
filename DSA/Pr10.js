function second_largest(nums) {
    if (!nums || nums.length < 2) {
        return null;
    }
    
    let largest = -Infinity;
    let second_largest = -Infinity;
    
    for (let num of nums) {
        if (num > largest) {
            second_largest = largest;
            largest = num;
        } else if (num > second_largest && num !== largest) {
            second_largest = num;
        }
    }
    
    return second_largest !== -Infinity ? second_largest : null;
}