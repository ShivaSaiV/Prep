class Solution {
    public int equalSubstring(String s, String t, int maxCost) {
        int sum_cost = 0;
        int count = 0;
        int l = 0;
        for (int i = 0; i < s.length(); i++) {
            int int_s = s.charAt(i);
            int int_t = t.charAt(i);
            int cost = int_s - int_t;
            if (cost < 0) {
                cost = cost * -1;
            }
            sum_cost += cost;
            while (sum_cost > maxCost) {
                sum_cost -= Math.abs(s.charAt(l) - t.charAt(l));
                l += 1;
            }
            count = Math.max(count, i - l + 1);
        }
        return count;
    }
}