class Solution {
    public int numSteps(String s) {
        int sum = 0;
        int carry = 0;
        for (int i = s.length() - 1; i >= 1; i--) {
            int n = s.charAt(i);
            if (n == 48) {
                if (carry == 0) {
                    sum += 1;
                }
                else {
                    sum += 2;
                    carry = 1;
                }
            }
            else {
                if (carry == 1) {
                    sum += 1;
                    carry = 1;
                }
                else {
                    sum += 2;
                    carry = 1;
                }
            }
        }
        if (carry > 0) {
            sum += 1;
        }
        return sum;
    }
}