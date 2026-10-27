class Solution {
    /**
     * @param {number[]} nums1
     * @param {number[]} nums2
     * @return {number[]}
     */
    intersection(nums1: number[], nums2: number[]): number[] {
        new Set(nums1)
        new Set(nums2)
        const seen: Record <number,number> = {};
        const result: number[] = [];

        for (const num in new Set(nums1)){
            seen[num] = (seen[num]?? 0)+1;
            
        }
        for (const num in new Set(nums2)){
                seen[num] = (seen[num]?? 0) + 1;
            }
        for (const key in seen){
            if (seen[key] > 1){
                result.push(Number(key))
            }
        }
        
        return result
    }
    
}
