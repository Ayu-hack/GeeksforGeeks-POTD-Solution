class Solution {
  public:
    long long max_Books(int arr[], int n, int k) {
        // Your code here
        int front = -1;
        int back = -1;
        long long max_sum = 0;
        long long sum = 0;
        for(int i=0;i<n;i++)
        {
            if(arr[i]<=k)
            {
                if(front<0)
                {
                    front = i;
                    back = i;
                    sum = sum + arr[i];
                }
                else
                {
                    sum = sum + arr[i];
                    back++;
                }
            }
            else
            {
                sum = 0;
                front = -1;
                back = -1;
            }
            if(max_sum<sum)
            {
                max_sum = sum;
            }
        }
        return max_sum;
    }
};
