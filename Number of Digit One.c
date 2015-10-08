int countDigitOne(int n) {
	if (n <= 0)
		return 0;
	uint64_t biter = 1;
	uint64_t counter = 0;
	while (biter * 10 <= n)
		biter *= 10;
	int prev,current,leave;	
	while (biter) {
		prev= n/biter/10;
		current = n/biter%10;
		leave = n % biter;
		if (current == 0)
			counter += prev * biter;
		else if(current == 1)
			counter += leave + 1 + prev * biter;
		else
			counter += (prev + 1) * biter;
		biter /= 10;
	}
	return counter;
}