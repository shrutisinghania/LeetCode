class Solution {
    public int maxNumberOfBalloons(String text) {
        int a=0, no=0;
        char ch[]={'b','a','l','l','o','o','n'};
        do{
            for (int i = 0; i<7;i++){
            a = text.indexOf(ch[i]);
            if(a==-1)
               break;
            text = text.replaceFirst(Character.toString(ch[i]), "");
            if (i==6)
                no +=1;
        }}while(a!=-1);
        return(no);        
    }
}