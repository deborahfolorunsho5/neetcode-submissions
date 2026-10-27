class Solution {
    lengthOfLongestSubstring(s: string): number {
        let best = 0;
        let start = 0;
        const seen = new Set<string>();

        for (let end = 0; end < s.length; end++) {
            while (seen.has(s[end])) {
                seen.delete(s[start]);
                start++;
            }
            seen.add(s[end]);
            best = Math.max(best, end - start + 1);
        }

        return best;
    }
}