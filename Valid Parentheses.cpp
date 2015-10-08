class Solution {
public:
    bool isValid(string s) {
        string::iterator it; 
        map<char ,char> imap;
        imap[')'] = '(',imap[']'] = '[',imap['}'] = '{';
        stack<char> pstack;
        for (it = s.begin();it != s.end(); ++it) {
            if (*it == '(' || *it == '{' || *it == '[')
                pstack.push(*it);
            else {
                if (pstack.empty() || pstack.top() != imap[*it])
                    return false;
                pstack.pop(); 
            }
        }
        return pstack.empty();
    }
};