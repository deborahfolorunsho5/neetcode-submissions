class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums: number[], k: number): number[] {
        const count: Record<number, number> = {};
        for (const num of nums) {
            count[num] = (count[num] ?? 0) + 1;
        }

        const keys: number[] = [];
        for (const key in count) {
            keys.push(Number(key));
        }

        keys.sort((a, b) => count[b] - count[a]);

        return keys.slice(0, k);
        // add every number to the dict
        //somehow get to take out the k most one from the dict key??
    }
}
//    
