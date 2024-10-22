// User function template for C++

class Solution {
  public:

    string longestCommonPrefix(vector<string> arr) {
        // your code here
        int min_length = arr[0].length();
        string min = arr[0];
        if(arr.size()==1){
            return min;
        }
        for(int i{1};i<arr.size();++i){
            if(arr[i].length() < min_length){
                min_length = arr[i].length();
                min = arr[i];
            }
        }
        
        vector<char> min_char(min_length);
        for(int i{};i<min_length;++i){
            min_char[i]=min[i];
        }
        min="";
        
        for(int i=min_length-1;i>=0;--i){
            for(int j = 0; j<arr.size();++j){
                if(arr[j].at(i)!=min_char[i]){
                    min_char[i]='\0';
                    if(i!=min_length-1)
                        min_char[i+1]='\0';
                    break;
                }
            }
        }
        for(int i {};i<min_length;++i){
            if(min_char[i]=='\0')
                continue;
            min+=min_char[i];
        }
        
        if(min=="")
            return "-1";
        return min;
    }
};