class Solution {
    /**
     * @param {string} ransomNote
     * @param {string} magazine
     * @return {boolean}
     */
    canConstruct(ransomNote: string, magazine: string): boolean {
        const ransome: Record<string, number>= {};
        const mag: Record<string, number>={};

        for (const letter of ransomNote){
            ransome[letter] = (ransome[letter] ?? 0) + 1;
        }
        for (const letter of magazine){
            mag[letter] = (mag[letter] ?? 0) + 1;
        }
        for (const letter in ransome) {
            if ((mag[letter]) < ransome[letter]) {
                return false;
            }
            if (!(letter in mag) || mag[letter] < ransome[letter]) {
                return false;
            }
        }
        


         
    return true
    }
}
