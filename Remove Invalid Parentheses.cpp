class SearchNode {
public:
    SearchNode(int _cut, string _str): cut(_cut), str(_str) {}
    int cut;
    string str;
};

class Solution {
public:
    vector<string> removeInvalidParentheses(string str) {
        vector<string> answer;
        if (checkValid(str)) {
            answer.push_back(str);
            return answer;
        }
        set<string> visited = {str};
        queue<SearchNode> iqueue;
        iqueue.push(SearchNode(0, str));
        int searchCounter = INT_MAX;
        while (!iqueue.empty()) {
            SearchNode current = iqueue.front();
            iqueue.pop();
            if (current.cut > searchCounter) {
                break;
            }
            if (checkValid(current.str)) {
                answer.push_back(current.str);
                searchCounter = current.cut;
                continue;
            }
            for (int i = 0;i < current.str.size(); ++i) {
                if (current.str[i] == '(' || current.str[i] == ')') {
                    string nextstr = current.str.substr(0, i) + current.str.substr(i + 1, current.str.size() - i - 1);
                    auto it = visited.find(nextstr);
                    if (it == visited.end()) {
                        visited.insert(nextstr);
                        iqueue.push(SearchNode(current.cut + 1, nextstr));                        
                    }
                }
            }
        }
        return answer;
    }

    bool checkValid(string str) {
        int left = 0, right = 0;
        for (auto ch: str) {
            if (ch == '(') {
                ++left;
            } else if (ch == ')') {
                ++right;
            }
            if (left < right) {
                return false;
            }
        }
        return left == right;
    }
};