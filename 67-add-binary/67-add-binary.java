class Solution {
    public String addBinary(String a, String b) {
        int al = a.length();
        int bl = b.length();
        int c = 0;
        String res = "";
        for(int i=0; i < Math.max(al, bl); ++i)
        {
            int x = (al > i) ? a.charAt(al - 1 - i) - '0' : 0;
            int y = (bl > i) ? b.charAt(bl - 1 - i) - '0' : 0;
            int tmp = x + y + c;
            c = tmp / 2;
            res = tmp %2 +res;
        }
        return (c==0) ? res : "1" + res;
    }
}