int calc_diff(int* array, int size, int sp, int sum)
{
    return sum - array[sp] - (size - 1) * array[sp];
}

int maxRotateFunction(int* array, int size)
{
    int sum = 0, i;
    for (i = 0;i < size; ++i)
    {
        sum += *(array + i);
    }
    int max_r = 0;
    for (i = 0;i < size; ++i)
    {
        max_r += i * (*(array + i));
    }
    int sp = size - 1;
    int prev_value = max_r;
    while (sp > 0)
    {
        int diff = calc_diff(array, size, sp, sum);
        prev_value += diff;
        if (prev_value > max_r)
        {
            max_r = prev_value;
        }
        --sp;
    }
    return max_r;
}
