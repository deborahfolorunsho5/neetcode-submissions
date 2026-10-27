class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs: string[]): string[][] {
        const seen: Record <string, string[]> = {};
        for (const word of strs){
            const label = word.split("").sort().join("")

            if (!(label in seen)){
                seen[label] = []
            }
            seen[label].push(word)
        }
        return Object.values(seen);


        // const seen = new Map <string, string[]>();

        // for (const word of strs){
        //     const label = word.split("").sort().join("")
             
        //     if (!seen.has(label)){
        //         seen.set(label,[]);
        //     }
        //     seen.get(label)!.push(word);
        //     //convert each word in alphabetical order and add to map
        //     //if the word alr exists then i would add it to the value 
        //     // label, value is mini actual list 
        //     // 
        // }
        // return Array.from(seen.values());

    }
}
