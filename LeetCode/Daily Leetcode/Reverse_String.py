class Solution {
    public void reverseString(char[] s) {
        int n = s.length - 1;
        for (int i = 0; i < n; i++) {
            char l = s[i];
            s[i] = s[n];
            s[n] = l;
            n--;
        }
    }
}