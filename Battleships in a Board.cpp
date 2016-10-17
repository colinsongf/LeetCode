class Solution {
public:
    void oneship(map<int, set<int> >& visited, int i, int j, vector<vector<char> >& board)
    {
        int v = i;
        while (v < board.size() && board[v][j] == 'X')
        {
            visited[v].insert(j);
            ++v;
        }
        int h = j;
        while (h < board[i].size() && board[i][h] == 'X')
        {
            visited[i].insert(h);
            ++h;
        }
    }

    bool isVisited(map<int, set<int> >& visited, int i, int j)
    {
        map<int, set<int> >::iterator it = visited.find(i);
        if (it == visited.end())
        {
            return false;
        }
        set<int>::iterator sit = it->second.find(j);
        return sit != it->second.end();
    }

    int countBattleships(vector<vector<char> >& board)
    {
        map<int, set<int> > visited;
        int answer = 0;
        if (!board.size() && !board[0].size())
        {
            return 0;
        }
        for (int i = 0;i < board.size(); ++i)
        {
            for (int j = 0;j < board[i].size(); ++j)
            {
                if (board[i][j] == 'X' && !isVisited(visited, i, j))
                {
                    oneship(visited, i, j, board);
                    answer += 1;
                }
            }
        }
        return answer;
    }
};
