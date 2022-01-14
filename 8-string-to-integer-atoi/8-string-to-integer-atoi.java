class Solution {
    public int myAtoi(String s) {
        int i = 0, no = 0, neg = 1;
        while(i < s.length() && s.charAt(i)==' ')
            ++i;
        if(i < s.length() && (s.charAt(i)=='-' || s.charAt(i)=='+'))
        {
            if(s.charAt(i++)=='-')
                neg = -1;
        }
        while(i < s.length() && Character.isDigit(s.charAt(i))==true)
        {
            if (no > Integer.MAX_VALUE / 10 || (no == Integer.MAX_VALUE / 10 && s.charAt(i) - '0' > 7)) {
				if (neg == -1) 
					return Integer.MIN_VALUE;
				return Integer.MAX_VALUE;
			}
            no = no*10 + (s.charAt(i++) - '0');
        }

        return no*neg;
    }
}