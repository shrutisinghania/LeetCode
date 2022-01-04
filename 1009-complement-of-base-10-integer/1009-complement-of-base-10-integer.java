class Solution {
    public int bitwiseComplement(int n) {
        String no = Integer.toBinaryString(n);
        char[] c = no.toCharArray();
        for (int i = 0; i < no.length(); ++i)
            c[i] = (c[i] == '0') ? '1' : '0';
        no = String.valueOf(c);
        return Integer.parseInt(no,2);
    }
}