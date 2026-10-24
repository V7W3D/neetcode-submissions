public class Solution {
    public int MaxProfit(int[] prices) {
        if (prices.Length <= 1){
            return 0;
        }
        int output = 0;
        int start = 0;
        for (int i = 0; i < prices.Length; i++){
            if (prices[i] > prices[start]){
                if (prices[i]-prices[start] > output){
                    output = prices[i]-prices[start];
                }
            }
            else{
                start = i;
            }
        }
        return output;
    }
}
