class Solution {
    public int romanToInt(String s) {
        int sum = 0;
        for(int i=0; i<s.length();i++){  
            char c = s.charAt(i);  
            switch(c){
                case 'I':
                    try{
                        int n = s.charAt(i+1);
                        if(n == 'V'){
                            sum = sum+4;
                            i = i+1;
                            break;
                        }
                        if(n == 'X'){
                            sum = sum+9;
                            i = i+1;
                            break;
                        }
                    }
                    catch(StringIndexOutOfBoundsException e){                
                    }
                    sum = sum+1;
                    break;
                case 'V':
                    sum = sum+5;
                    break;
                case 'X':
                    try{
                        int o = s.charAt(i+1);
                        if(o == 'L'){
                            sum = sum+40;
                            i = i+1;
                            break;
                        }
                        if(o == 'C'){
                            sum = sum+90;
                            i = i+1;
                            break;
                        }
                    }
                    catch(StringIndexOutOfBoundsException e){                
                    }
                    sum = sum+10;
                    break;
                case 'L':
                    sum = sum+50;
                    break;
                case 'C':
                    try{
                        int h = s.charAt(i+1);
                        if(h == 'D'){
                            sum = sum+400;
                            i = i+1;
                            break;
                        }
                        if(h == 'M'){
                            sum = sum+900;
                            i = i+1;
                            break;
                        }
                    }
                    catch(StringIndexOutOfBoundsException e){                
                    }
                    sum = sum+100;
                    break;
                case 'D':
                    sum = sum+500;
                    break;
                case 'M':
                    sum = sum+1000;
                    break;
                
            }
        }  
        return sum;
    }
}