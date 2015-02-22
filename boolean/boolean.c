#include <stdio.h>
#include <stdlib.h>

int wt_nl (int *, int);
int balans (int *, int);

int eval(int tt[], int nVariables)
{
	//example for input parameters
	//int tt[256] = {1,0,0,0,0,1,1,1,1,1,0,1,0,0,1,0,0,1,1,1,1,0,0,0,0,0,1,0,1,1,0,1,1,0,1,0,0,1,0,1,0,1,1,1,0,0,0,0,1,0,1,0,0,1,0,1,1,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,1,1,0,1,1,1,0,1,0,1,1,1,0,1,1,1,0,0,1,0,0,0,1,0,1,0,1,0,1,0,1,0,0,1,1,1,1,1,1,1,1,0,1,0,1,0,1,0,1,0,0,0,1,1,1,1,0,0,1,1,0,0,1,1,1,0,0,1,1,0,0,1,0,0,1,1,0,0,1,1,1,0,0,1,1,0,0,1,1,1,0,1,1,1,0,1,0,1,1,0,0,1,1,1,0,0,1,0,0,0,1,0,1,0,0,0,1,0,0,0,1,1,0,0,0,0,1,1,0,1,1,0,1,0,0,1,1,1,0,0,0,0,1,1,0,1,1,0,1,0,0,1,0,0,1,0,1,1,0,1,1,0,0,1,0,1,1,1,1,1,0,1,0,0,1,0,0,1,1,1,1,0,0,0};
	//nVariables = 8;

	int fitness;
    int i;

	fitness = balans(tt,nVariables) + wt_nl (tt, nVariables);

	return fitness;
}


int balans (int *tt, int n)
{
	int i, rez=0;

   for(i=0; i < (1 << n); i++)
   {
	   if (tt[i]==0) //count zeros
		   rez=rez+1;
   }
   if (rez == ((1 << n)/2))
	   return 0; //if balanced give small reward
   else if (rez < ((1 << n)/2)) // less than half zeros
	{
		if(rez == 0)
			rez = 1;
		return (((1 << n)-rez)/(1.*rez))*(-50);
	}
   else if (rez > ((1 << n)/2)) // more than half zeros
	{
		if(rez == (1 << n))
			rez = (1 << n) - 1;
	   return ((1.*rez)/((1 << n)-rez))*(-50);
    }
}

int wt_nl (int *tt, int n) //for nonlinearity
{
    int i, j, m, halfm, t1, t2, r, a, b, max = 0, rezultat = 0;

	int *rez=0;
	int *ac=0;

	rez=(int *) malloc((1 << n)*sizeof(int));

    for(i = 0; i < (1 << n); ++i)
        rez[i] = (tt[i]==0)? 1 : -1;

    for(i = 1; i <= n; ++i)
    {
        m  = (1 << i);
        halfm = m/2;
        for(r=0; r < (1 << n); r += m)
        {
            t1 = r;
            t2 = r + halfm;
            for(j=0; j < halfm; ++j, ++t1, ++t2)
            {
                a = rez[t1];
                b = rez[t2];
                rez[t1] = a + b;
                rez[t2] = a - b;
				if (abs(rez[t1]) > max)
					max = abs(rez[t1]);
			    if (abs(rez[t2]) > max)
					max = abs(rez[t2]);
            }
        }
    }

	free(rez);

	return (((1 << n) - max)/2);
}
