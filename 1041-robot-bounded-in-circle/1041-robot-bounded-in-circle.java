class Solution {
    public boolean isRobotBounded(String instructions) {
        int dir = 90;
        int l = 0, r = 0;
        for(int i = 0; i < instructions.length(); ++i)
        {
            if(instructions.charAt(i) == 'L')
                dir = (dir + 90) % 360;
            else if(instructions.charAt(i) == 'R')
                dir = Math.abs((dir - 90 + 360) % 360);
            else if(instructions.charAt(i) == 'G')
            {
                if(dir == 90)
                    r++;
                else if(dir == 270)
                    r--;
                else if(dir == 180)
                    l--;
                else if(dir == 0)
                    l++;
            }
        }
        System.out.println(dir +" " + l + " " + r);
        if(dir != 90 || (l == 0 && r == 0))
            return true;
        return false;
    }
}