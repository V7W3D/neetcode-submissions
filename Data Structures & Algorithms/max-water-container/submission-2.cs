public class Solution {
    public int MaxArea(int[] heights) {
        if (heights.Length <= 1) {
            return 0;
        }

        int maxAmount = 0;
        int actualAmount = 0;
        int start = 0;
        int end = heights.Length - 1;
        while (start < end) {
            actualAmount = (end - start) * Math.Min(heights[end], heights[start]);
            if (actualAmount > maxAmount) {
                maxAmount = actualAmount;
            }
            if (heights[start] > heights[end]) {
                end--;
            }
            else {
                start++;
            }
        }

        return maxAmount;
    }
}
