class Solution {
    public List<List<String>> partition(String s) {
        List<List<String>> l = new ArrayList<List<String>>();
        dfs(0, l, new ArrayList<String>(), s);
        return l;
    }
    
    private int isPalindrome(String s, int l, int r)
    {
        while(l < r)
        {
            if(s.charAt(l++)!=s.charAt(r--))
                return 0;
        }
        return 1;
    }
    
    private void dfs (int strt, List<List<String>> l, List<String> pal, String s)
    {
        if (strt >= s.length())
        {
            l.add(new ArrayList<String>(pal));
            return;
        }
        for(int end = strt; end < s.length(); ++end)
        {
            if (isPalindrome(s,strt,end)==1)
            {
                pal.add(s.substring(strt,end+1));
                dfs(end+1, l, pal, s);
                pal.remove(pal.size()-1);
            }
        }
    }
}