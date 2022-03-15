class Solution {
    public String minRemoveToMakeValid(String s) {
      StringBuilder sb = new StringBuilder(s), sb1 = new StringBuilder();
      Stack<Integer> st = new Stack();
      for (int i = 0; i < sb.length(); ++i) {
        if (sb.charAt(i) == '(') st.add(i + 1);
        if (sb.charAt(i) == ')') {
          if (!st.empty() && st.peek() >= 0) st.pop();
          else st.add(-(i + 1));
        }
      }
      for(int i = 0, j = 0; i < sb.length(); ++i) {
          if (j >= st.size() || i != Math.abs(st.elementAt(j)) - 1) {
            sb1.append(sb.charAt(i));
          } else ++j;
      }
      return sb1.toString(); 
    }
}