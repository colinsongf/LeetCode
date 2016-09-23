bool isSubsequence(char* s, char* t) {
    unsigned s_size = strlen(s), t_size = strlen(t);
    int s_pos = 0, t_pos = 0;
    while (s_pos < s_size)
    {
        while (t_pos < t_size && *(t + t_pos) != *(s + s_pos))
        {
            ++t_pos;   
        }   
        if (t_pos == t_size)
        {
            return false;
        }   
        ++t_pos;
        ++s_pos;
    }   
    return true;
}
