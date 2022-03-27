class Solution {
    public int[] kWeakestRows(int[][] mat, int k) {
       int[] arr = new int[mat.length];
        int[] ans = new int[k];
        ArrayList<Integer> list = new ArrayList<>();
        for(int i=0;i<mat.length;i++){
            int check = count(i,mat);
            arr[i]= check;
        }
        int flag =0;
        while (k!=0 && flag<ans.length){
            int index = findMin(arr);
            ans[flag] = index;
            k--;
            flag++;
            arr[index] =Integer.MAX_VALUE;
        }
        return ans;
        
    }
     public int findMin(int[] arr){
        int min = Integer.MAX_VALUE;
        int index =-1;
        for (int i =0;i<arr.length;i++){
            if (arr[i]<min){
                min = arr[i];
                index = i;
            }
        }
        return index;
    }
    public int count(int a, int[][] arr ){
        int b = arr[a].length;
        int count=0;
        for(int i=0;i<b;i++){
            if(arr[a][i]==0)
                break;
            if(arr[a][i]==1)
                count++;
        }
        return count;
    }
        
}