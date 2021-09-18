class Solution {
    private String findLC(String a, String b)
    {
        int j = (a.length() > b.length()) ? b.length() : a.length();
        for(int i = 0; i<j ; i++){
            if(a.charAt(i)!=b.charAt(i)){
                try{
                return a.substring(0,i);}
                catch(StringIndexOutOfBoundsException e){
                    return "";
                }
            }
        }
        return a.substring(0,j);
    }    
    public String longestCommonPrefix(String[] strs) {
        String a = strs[0];
        for(int i = 1; i<strs.length;i++){
            a = findLC(a,strs[i]);
            if (a.equals(""))
                return "";                
        }
        return a;
    }
}