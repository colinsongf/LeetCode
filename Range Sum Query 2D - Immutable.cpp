class NumMatrix {
public:
    NumMatrix(vector<vector<int> > &matrix) {
        if (matrix.size() != 0 && matrix[0].size() != 0) {
            int row = matrix.size();
            int col = matrix[0].size();
            for (int i = 0;i < row; ++i) {
                vector<int> v(col);
                rowSummary.push_back(v);
            }
            for (int j = 0;j < col; ++j) {
                rowSummary[0][j] = matrix[0][j];
            }
            for (int i = 1;i < row; ++i) {
                for (int j = 0;j < col; ++j) {
                    rowSummary[i][j] = rowSummary[i - 1][j] + matrix[i][j];
                }
            }
        }
    }

    int sumRegion(int row1, int col1, int row2, int col2) {
        if (rowSummary.size() == 0 || rowSummary[0].size() == 0) {
            return 0;
        }
        int row = rowSummary.size();
        int col = rowSummary[0].size();
        int summary = 0;
        for (int j = col1;j <= col2; ++j) {
            if (row1 == 0) {
                summary += rowSummary[row2][j];
            } else {
                summary += rowSummary[row2][j] - rowSummary[row1 - 1][j];
            }
        }
        return summary;
    }
private:
    vector<vector<int> > rowSummary;
};