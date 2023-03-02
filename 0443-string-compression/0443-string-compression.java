class Solution {
    public int compress(char[] chars) {
        int j = 0;
        for(int i = 0; i < chars.length; ++i)
        {
            char c = chars[i];
            int n = 1;
            while (i + 1  < chars.length && chars[i+1] == c)
            {
                n++;
                i++;
            }
            chars[j++] = c;
            if (n > 1)
            {
                String a = String.valueOf(n);
                for (char p: a.toCharArray())
                    chars[j++] = p;
            }
        }
        return j;
    }
}