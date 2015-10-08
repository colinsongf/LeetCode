#define MAX(x,y) (x)>(y)?(x):(y)

int maximalSquare(char** matrix, int matrixRowSize, int matrixColSize) {
	int **m=malloc(sizeof(int *)*matrixRowSize);
	int i,j;
	for(i=0;i<matrixRowSize;++i)
		m[i]=malloc(sizeof(int)*matrixColSize);
	int answer=0;
	//init
	for(i=0;i<matrixRowSize;++i){
		m[i][0]=matrix[i][0]=='1'?1:0;
		answer=MAX(answer,m[i][0]);
	}
	for(j=0;j<matrixColSize;++j){
		m[0][j]=matrix[0][j]=='1'?1:0;
		answer=MAX(answer,m[0][j]);
	}
	//dynamic
	for(i=1;i<matrixRowSize;++i)
		for(j=1;j<matrixColSize;++j)
			if(matrix[i][j]=='0')
				m[i][j]=0;
			else{
				m[i][j]=m[i-1][j-1];
				if(m[i-1][j] < m[i][j])
					m[i][j]=m[i-1][j];
				if(m[i][j-1] < m[i][j])
					m[i][j]=m[i][j-1];
				++m[i][j];
				answer=MAX(m[i][j],answer);
			}
	return answer*answer;
}