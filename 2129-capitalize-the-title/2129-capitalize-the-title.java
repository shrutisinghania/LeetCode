class Solution {
    public String capitalizeTitle(String title) {
        String[] wrds = title.split("\\s");
        String s = "";
        for(String w:wrds)
        {
            if (w.length()>2)
                s = s + w.substring(0,1).toUpperCase() + w.substring(1).toLowerCase() + " ";
            else
                s = s + w.toLowerCase() + " ";
        }
        return s.substring(0, s.length() - 1);
    }
}