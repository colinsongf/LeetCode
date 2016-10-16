#include <sstream>

template<class T>
std::string convert2String(const T& val)
{
    ostringstream convert;
    convert << val;
    std::string result = convert.str();
    return result;
}

class Solution {
public:
    vector<string> fizzBuzz(int n) {
        vector<string> answer;
        for (int i = 1;i < n + 1; ++i)
        {
            if (i % 3 == 0 && i % 5 == 0)
            {
                answer.push_back("FizzBuzz");
            }
            else if (i % 3 == 0)
            {
                answer.push_back("Fizz");
            }
            else if (i % 5 == 0)
            {
                answer.push_back("Buzz");
            }
            else
            {
                answer.push_back(convert2String(i));   
            }
        }
        return answer;
    }
};
