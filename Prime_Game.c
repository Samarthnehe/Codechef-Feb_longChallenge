#include <stdio.h>

// #define FAST  ios::sync_with_stdio(0),cin.tie(0),cout.tie(0);
typedef long long int lli;
int prime[1000009];
int number[1000009];
void sieve(int n)
{
    // bool prime[n + 1];
    // memset(prime, 1, sizeof(prime));
 
    for (int i=2;i*i<=n;i++)
    {
        if (prime[i] == 1) 
        {
            for (int j=i*i;j<=n;j+=i)
                prime[j] = 0;
        }
    }
    int count=0;number[0]=0;number[1]=0;
    for(int i=2;i<=n;i++){
        if(prime[i]==1)
            count++;
        number[i]=count;
    }
    
}

int main(void) {
	// your code goes here
// 	ios_base::sync_with_stdio(false);

	int n,t,k;
	scanf("%d",&t);
	for(int i=0;i<1000009;i++)
	    prime[i]=1;
	sieve(1000008);
	while(t--){
	    int x,y;
	    scanf("%d %d",&x,&y);
	   // printf("%d\n",prime[x]);
        if(number[x]<=y)
            printf("Chef\n");
        else
            printf("Divyam\n");
	}
	
	return 0;
}
