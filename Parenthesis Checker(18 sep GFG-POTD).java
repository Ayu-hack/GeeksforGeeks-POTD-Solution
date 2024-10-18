
class Solution
{
    public:
    bool ispar(string x) {
    stack<char> s;
    for (char c : x) {
        if (c == '(' || c == '{' || c == '[') {
            s.push(c);
        } 
        else {
            if (s.empty()) return false;
            char top = s.top();
            if ((c == ')' && top == '(') || 
                (c == '}' && top == '{') || 
                (c == ']' && top == '[')) {
                s.pop();  
            } else {
                return false;  
            }
        }
    }
    return s.empty();
}
};
