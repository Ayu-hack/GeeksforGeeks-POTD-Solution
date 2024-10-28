import java.util.*;
class TripletFamily27Oct {
    public boolean findTriplet(int[] arr)
    {
        Arrays.sort(arr); 
        for(int i=0;i<arr.length;i++)
        {
            int left=0;
            int right=arr.length-1;
            while(left<right)
            {
                int sum=arr[left]+arr[right];
                if(sum==arr[i])
                {
                    return true;
                }
                else if(sum<arr[i])
                {
                    left++;
                }
                else{
                   right--;
                }
            }
        }
        return false;
        
    }
}


