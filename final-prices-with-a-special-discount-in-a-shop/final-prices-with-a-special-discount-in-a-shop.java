class Solution {
    public int[] finalPrices(int[] prices) {
      int j;
      for(int i =0; i< prices.length;i++){
          j = i+1;
          while(j<prices.length){
          if (prices[j] <= prices[i]){
              prices[i]=prices[i]-prices[j];
              break;
          }
          j++;
          }
      }  
      return prices;
    }
}