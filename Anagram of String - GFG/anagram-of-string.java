// { Driver Code Starts
//saksham raj seth
import java.util.*;
class Anagrams{
	public static void main(String[] args){
		Scanner sc=new Scanner(System.in);
		int t=sc.nextInt();
		while(t-->0){
			String s=sc.next();
			String s1=sc.next();
			GfG g=new GfG();
			System.out.println(g.remAnagrams(s,s1));
		}
	}
}// } Driver Code Ends


/*Complete the function below*/
class GfG
{
	public int remAnagrams(String s,String s1)
        {
                    String lowerImp="";
        String bigImp="";
        if(s.length()<s1.length())
        {
            lowerImp=s;
            bigImp=s1;
        }
        else
        {
            lowerImp=s1;
            bigImp=s;
        }
        HashMap<Character,Integer>map=new HashMap<>();
        for(int i=0;i<lowerImp.length();i++)
        {
            if(map.containsKey(lowerImp.charAt(i)))
            {
                map.put(lowerImp.charAt(i),map.get(lowerImp.charAt(i))+1);
            }
            else
            {
                map.put(lowerImp.charAt(i),1);
            }
        }
        
       int count=0;
       for(int i=0;i<bigImp.length();i++)
       {
           if(map.containsKey(bigImp.charAt(i)) && map.get(bigImp.charAt(i))>0)
           {
               map.put(bigImp.charAt(i),map.get(bigImp.charAt(i))-1);
           }
           else
           {
           count++;
           }
       }
       for (Map.Entry<Character,Integer> entry : map.entrySet())
       count+=entry.getValue();
            
       return count;
        }
}