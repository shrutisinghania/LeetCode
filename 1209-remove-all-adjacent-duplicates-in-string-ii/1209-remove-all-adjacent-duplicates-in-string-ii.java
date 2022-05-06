class Solution {
    public String removeDuplicates(String s, int k) {
        Stack<int []> st = new Stack<>();
        for (char c: s.toCharArray())
        {
            if(!st.isEmpty() && st.peek()[0] == c)
            {
                if (st.peek()[1] == k-1)
                    st.pop();
                else
                    st.peek()[1]++;
            }
            else
                st.push(new int[] {c, 1});
        }
        StringBuilder str = new StringBuilder();
        while(!st.isEmpty())
        {
            int[] top = st.pop();
            while(top[1]-- > 0)
                str.append((char)top[0]);
        }
        return str.reverse().toString();
    }
}