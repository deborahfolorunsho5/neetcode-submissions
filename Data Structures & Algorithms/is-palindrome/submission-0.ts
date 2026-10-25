
class Solution {
    isPalindrome(s: string): boolean {
        // Clean it: lowercase, and keep only letters and numbers
        const clean = s.toLowerCase().replace(/[^a-z0-9]/g, "");

        // One pointer at the front, one at the back
        let left = 0;
        let right = clean.length - 1;

        // Keep going until they meet in the middle
        while (left < right) {
            // Letters don't match? Not a palindrome
            if (clean[left] !== clean[right]) {
                return false;
            }

            // They match, so move both toward the middle
            left++;
            right--;
        }

        // Made it to the middle with no mismatch
        return true;
    }
}
