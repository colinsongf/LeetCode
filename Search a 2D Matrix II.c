bool searchMatrix(int** matrix, int matrixRowSize, int matrixColSize, int target) {
    if (matrixRowSize == 0 || matrixColSize == 0)
        return false;
    int current_row = 0,current_col = matrixColSize - 1;
    while (current_col >= 0 && current_row < matrixRowSize) {
        int top = matrix[current_row][current_col];
        if (top == target)
            return true;
        else if (top < target)
            current_row += 1;
        else
            current_col -= 1;
    }
    return false;
}