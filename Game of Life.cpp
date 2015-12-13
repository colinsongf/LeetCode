class Solution {
private:
    int neiborLiveCounter(vector<vector<int> >& board, int i, int j, int row, int col) {
        pair<int, int> neibors[] = {pair<int, int>(i - 1, j - 1), pair<int, int>(i - 1, j), pair<int, int>(i - 1, j + 1), pair<int, int>(i, j - 1), pair<int, int>(i, j + 1), pair<int, int>(i + 1, j - 1), pair<int, int>(i + 1, j), pair<int, int>(i + 1, j + 1)};
        int counter = 0;
        for (int i = 0;i < 8; ++i) {
            int x = neibors[i].first, y = neibors[i].second;
            if (x >=0 && x < row && y >=0 && y < col && board[x][y]) {
                counter += 1;
            }
        }
        return counter;
    }
public:
    void gameOfLife(vector<vector<int> >& board) {
        int row = board.size();
        if (!row)
            return ;
        int col = board[0].size();
        set<pair<int, int> > liveRecord;
        for (int i = 0;i < row; ++i) {
            for (int j = 0;j < col; ++j) {
                int counter = neiborLiveCounter(board, i, j, row, col);
                if ((board[i][j] && (counter == 2 || counter == 3)) || (!board[i][j] && counter == 3)) {
                    pair<int, int> livePos(i, j);
                    liveRecord.insert(livePos);
                }
            }
        }
        set<pair<int, int> >::iterator it;
        for (int i = 0;i < row; ++i) {
            for (int j = 0;j < col; ++j) {
                pair<int, int> myPos(i, j);
                it = liveRecord.find(myPos);
                if (it != liveRecord.end()) {
                    board[i][j] = 1;
                } else {
                    board[i][j] = 0;
                }
            }
        }
    }
};