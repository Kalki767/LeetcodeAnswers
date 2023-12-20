class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        int n = strs.size();
        string pre = "";
        sort(strs.begin(),strs.end());
        string first=strs[0],last=strs[n-1];
        int length = first.length()>last.length()?last.length():first.length();
        for(int i=0;i<length;i++){
            if(first[i]!=last[i]){
                return pre;
            }
            pre+=first[i];
        }
        return pre;
    }
};