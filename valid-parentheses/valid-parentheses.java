class Solution {
    public boolean isValid(String s) {
        Deque<Character> stack = new ArrayDeque<Character>();
        for(int i=0; i<s.length(); i++){
            char c = s.charAt(i);
            if (c == '(' || c == '{' || c == '[')
                stack.push(c);
            else{
                if(stack.isEmpty())
                    return false;
                switch(c){
                case ')':
                        if (stack.pop()!='(')
                            return false;
                        break;
                case '}':
                        if (stack.pop()!='{')
                            return false;
                        break;
                case ']':
                        if (stack.pop()!='[')
                            return false;
                        break;
                }
            }
        }
        if(stack.isEmpty())
            return true;
        return false;
    }
}