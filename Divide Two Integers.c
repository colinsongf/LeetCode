#define INT_MAX 2147483647
#define INT_MIN -2147483648
int divide(int intdividend,int intdivisor){
	if(!intdivisor)
		exit(1);
	long long dividend=intdividend,divisor=intdivisor,ret;
	int neg=0,how;
	if(dividend<0){
		dividend=~dividend+1;
		neg=1;
	}
	if(divisor<0){
		divisor=~divisor+1;
		neg=!neg;
	}
	if(divisor==1){
		ret=dividend;
	}
	else{
		while(dividend>=divisor){
			for(how=1;(divisor<<how)<=dividend;++how);
			how--;
			ret+=(1<<how);
			dividend-=(divisor<<how);
		}
	}
	ret=neg?(~ret+1):ret;
	if(ret>INT_MAX)
		return INT_MAX;
	else if(ret<INT_MIN)
		return INT_MIN;
	else
		return ret;
}