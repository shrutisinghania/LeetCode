class Solution {
    public String removeKdigits(String num, int k) {
        if (k == 0)
            return num;
        int l = num.length();
        if (l == k)
            return "0";
        Stack<Character> s = new Stack<>();
        int i = 0;
        while(i < l)
        {
            while(k > 0 && !s.isEmpty() && s.peek() > num.charAt(i))
            {
                s.pop();
                --k;
            }
            s.push(num.charAt(i++));
        }
        while(k-- > 0)
            s.pop();
        
        String no = "";
        while(!s.isEmpty())
            no = s.pop() + no;
        
        while(no.length() > 1 && no.charAt(0) == '0')
            no = no.substring(1);
        return no;
    }
}