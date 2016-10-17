int numberOfArithmeticSlices(int* array, int size) {
    if (size <= 2)
    {
        return 0;
    }
    int answer = 0;
    int adder = 0;
    for (int i = 2;i < size; ++i)
    {
        if (array[i] - array[i - 1] == array[i - 1] - array[i - 2])
        {
            adder += 1;
            answer += adder;
        }
        else
        {
            adder = 0;
        }
    }
    return answer;
}
