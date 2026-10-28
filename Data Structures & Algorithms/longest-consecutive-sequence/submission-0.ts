class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    longestConsecutive(nums: number[]): number {
        const seen = new Set <number>();

        for(const num of nums){
            seen.add(num);
        }
        let best = 0

        for (const num of seen){
            // if has num- 1 therefore not a start
            if(seen.has(num-1)){
                continue
            }
            let length = 1
            while(seen.has(num+ length)){
                length++;

            }
            best = Math.max(best,length)
                
            
        }
        

        return best

    }
}
