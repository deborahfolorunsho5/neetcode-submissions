class Solution {
    /**
     * @param {number} n
     * @return {number}
     */
    memo: Record <number,number> = {};
    climbStairs(n: number): number {
        
        if (n === 1){
            return 1;
        }
        if (n === 2){
            return 2;
        }
        if (n in this.memo){
            return this.memo[n]
        }

        const ways = this.climbStairs(n-1) + this.climbStairs(n-2);
        this.memo[n] = ways 
        return ways;
    }
}
