class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        int n = static_cast<int>(nums.size()) - 1;
        int headchoice = 1, rearchoice = n;
        while (headchoice <= rearchoice) {
            if (headchoice == rearchoice) {
                return headchoice;
            }
            int midchoice = (headchoice + rearchoice) >> 1;
            int smallerthanme = 0, biggerthanme = 0;

            for (auto i: nums) {
                if (i < midchoice) {
                    smallerthanme++;
                } else if (i > midchoice) {
                    biggerthanme++;
                }
            }

            if (smallerthanme > midchoice - 1) {
                //duplicate is in [1, midchoice)
                rearchoice = midchoice - 1;
            } else if (biggerthanme > n - midchoice) {
                //duplicate is in (midchoice, rearchoice]
                headchoice = midchoice + 1;
            } else {
                return midchoice;
            }
        }
        return  -1;
    }
};