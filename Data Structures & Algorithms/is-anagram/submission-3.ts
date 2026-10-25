class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s: string, t: string): boolean {
        if (s.length !== t.length) {
            return false;
        }

        const countT: Record<string,number> = {};
        const countS: Record<string,number> = {};
        for (const letter of s){
            countS[letter] = (countS[letter] ?? 0)+1;
        }
        for (const letter of t){
            countT[letter] = (countT[letter] ?? 0)+1;
        }

        for (const letter in countS){
            if (countS[letter] != countT[letter]){
                return false
            }
            

        }
        return true
        //take the string s add it to the dict 
        // take the string t add it to another dict 
        // then compare that the dicts are identical


    }

}
