bool isPalindrome(int x) {
    if (x < 0)
        return false;
    if (x >=0 && x < 10)
        return true;
    int leftdiv = 1,rightdiv = 10;
    while (x / leftdiv >= 10) {
        leftdiv *= 10;
    }
    int l,r;
    int tmplx,tmprx;
    tmplx = tmprx = x;
    while (tmplx && tmprx) {
        l = tmplx / leftdiv;
        r = tmprx % 10;
        //printf("%d,%d\n",l,r );
        if (l != r)
            return false;
        tmplx %= leftdiv;
        leftdiv /= 10;
        tmprx /= 10;
    }
    return true;
}