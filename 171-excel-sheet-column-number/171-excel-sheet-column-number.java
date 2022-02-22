class Solution {
    public int titleToNumber(String columnTitle) {
        int i = 0, r = 0;
        for(int j = columnTitle.length()-1; j>=0; --j)
            r += Math.pow(26, i++) * (columnTitle.charAt(j) - 'A' + 1);
        return r;
    }
}