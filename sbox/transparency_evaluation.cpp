#include <stdio.h>
#include <stdlib.h>
#include <string.h>
//#include <iostream>
//using namespace std;

typedef unsigned char u8;

int wt_nl (u8 *);							//returns nonlinearity of Boolean function
int balance (u8 *);						//returns whether a Boolean function o+is balanced
int nonlinearity (int);					//returns nonlinearity of Boolean function
int evaluate_box(u8 *, int, int);				// evaluate S-box for the derivative of F in direction of a
int inner_product(int, int);					//calculate inner product of two vectors
float transparency (u8 *);					//calculate transparency order of S-box
//float transparency2 (u8 *);					//calculate transparency order of S-box, another formula
void xor_elements (u8 *, u8 *, u8 *);			//xor elements of two arrays and put in third array
float find_min_nl(int *);						//find the minimum value in the array
float find_bal(int *);						//find the total balancedness
void set_to_zero (u8 *);					//set array elements to zero value

const int M = 8;
const int N = 8;


//
// ako je nelinearnost == true, vrati samo min_nl
//
float eval(u8 tt[N][256], bool& stop)
{

	/*Properties of (m,n) S-box

	At the moment, we are interested in following properties of S-Boxes
	1. balancedness - equal numbe of zeros and ones for each of Boolean functions and for linear combinations of them
	2. nonlinearity - smallest Hamming distance between Boolean function and its best affine aproximation and for linear combinations of all Boolean functions

	*/

/*	u8 tt[8][256] =	   {{0,1,1,0,1,0,1,0,0,0,1,0,1,1,0,0,0,0,0,1,1,1,0,1,0,1,0,0,0,1,0,0,1,0,0,1,0,1,0,0,0,0,0,1,1,0,0,1,1,1,0,1,1,1,0,1,0,1,0,0,1,0,1,1,0,0,0,1,0,0,1,0,0,1,0,0,1,0,1,1,0,0,0,1,1,0,1,1,0,1,0,1,1,1,1,1,1,1,0,1,1,0,1,1,1,0,1,0,0,1,1,1,0,0,1,1,0,1,0,1,1,1,1,0,0,0,1,0,0,1,1,0,1,0,1,1,1,1,1,1,1,0,0,0,1,0,0,0,0,1,0,1,1,0,1,1,1,1,0,0,1,0,1,1,0,1,0,0,0,0,0,1,0,0,0,1,0,1,0,0,1,1,1,0,0,1,0,1,1,1,1,1,1,1,0,0,0,1,1,1,0,1,1,1,1,1,0,0,0,0,0,0,1,1,1,0,1,0,0,1,1,0,1,1,0,0,0,1,0,1,0,0,1,0,0,0,0,0,0,1,0,1,1,1,0,0,0,0,0,0,0,1,1,1,1,1},
						{1,1,1,0,1,1,0,1,1,1,1,0,1,0,0,0,1,0,1,0,1,1,0,1,1,1,1,1,1,1,0,0,1,0,1,0,0,1,0,0,1,0,1,0,0,1,1,1,1,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,1,1,1,0,0,1,1,1,1,0,1,1,0,1,1,0,1,0,0,1,1,1,0,0,0,1,1,1,1,1,1,1,1,0,0,0,1,1,1,0,1,1,0,1,0,1,0,0,0,1,1,1,1,0,1,0,1,1,0,1,0,0,0,1,0,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,1,1,0,1,0,0,1,0,1,0,1,0,1,0,0,0,1,0,1,1,1,1,0,0,0,1,1,1,1,0,0,0,1,1,0,0,0,0,0,0,1,0,0,0,0,0,1,0,1,1,1,1,0,1,1,0,1,0,0,0,1,0,0,1,0,0,1,1,0,1,1,0,0,0,0,0,1,0,0,1,1,0,1,1,0,1,0,1,1,1,1,1,1,1,1,1,0,1,1,0,1,0,0,1,0,0,0,0,0,0,1,1},
						{1,1,1,0,1,0,1,0,1,1,1,1,1,1,1,0,0,1,0,1,1,1,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,0,0,1,0,1,0,0,0,1,1,1,0,0,1,0,1,0,1,0,0,1,0,0,0,0,0,1,1,0,0,1,1,0,1,1,1,0,1,1,0,1,1,0,0,1,0,1,1,0,1,1,0,0,0,0,1,0,0,1,1,1,0,0,1,1,1,0,0,0,0,0,0,0,1,1,1,1,1,1,0,1,0,1,1,1,1,1,1,0,0,1,0,1,0,0,1,0,1,1,0,1,0,1,1,1,1,0,0,1,0,0,1,1,1,1,0,0,0,1,1,0,0,0,1,0,0,0,0,1,0,1,1,1,0,0,1,1,0,1,1,1,1,0,1,0,0,1,0,0,1,1,1,1,0,0,1,1,1,1,0,0,0,1,1,1,0,0,1,0,1,0,0,0,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,0,0,0,1,0,0,1,1,0,1,0,0,0,1,0,1,0,1,0,0,0,0,0,0,0},
						{1,0,0,0,0,0,1,1,1,1,0,1,1,1,1,1,1,0,1,0,0,0,1,0,0,0,1,1,0,1,0,0,1,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,0,1,1,0,0,0,0,0,1,1,1,0,1,0,0,0,1,0,0,0,0,0,1,1,0,0,1,1,0,1,1,1,0,1,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,1,0,1,0,0,0,1,0,0,1,0,1,1,0,0,1,1,1,1,0,0,0,1,1,0,0,1,1,1,0,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,0,0,0,0,1,0,0,0,0,0,0,1,1,0,1,1,1,1,0,0,1,0,1,1,1,0,1,0,1,1,0,0,0,1,1,0,0,1,0,1,1,0,0,1,0,1,0,0,1,0,1,1,0,1,0,1,1,0,0,0,0,1,0,1,1,0,1,0,1,1,0,1,1,1,1,1,1,1,0,1,1,0,1,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,1,0,0,1,1,0,0,0,0,1,0},
						{0,1,1,1,0,1,0,1,0,0,0,1,1,1,0,0,0,0,0,1,0,0,1,1,1,0,1,0,1,1,0,0,0,1,0,0,0,0,1,0,1,0,1,0,0,1,0,1,0,1,0,1,1,0,0,0,1,1,0,0,1,0,0,0,0,1,0,1,0,1,1,1,1,1,1,1,0,0,1,0,1,0,1,1,0,0,1,0,0,0,1,1,0,1,1,0,1,1,0,0,0,0,1,0,1,1,0,0,0,1,1,0,1,0,1,0,1,1,0,0,1,1,1,1,1,0,0,0,1,1,0,0,0,0,0,0,0,0,1,1,1,0,0,1,1,1,0,1,1,1,1,0,0,1,1,1,0,1,1,1,0,1,0,0,1,0,1,0,1,1,1,0,1,0,1,0,0,0,0,0,1,1,1,0,0,1,1,1,1,0,1,0,1,0,1,1,1,1,1,0,0,0,1,1,1,0,1,0,1,0,0,1,1,0,1,0,1,1,1,0,0,1,0,1,0,1,0,1,1,0,1,0,0,1,1,1,0,0,0,0,1,1,1,1,0,1,0,0,0,0,1,0,0,0,1,0},
						{1,0,1,0,0,0,0,0,0,1,0,1,0,0,0,1,0,1,1,1,1,1,0,1,0,0,0,1,1,1,0,0,1,0,0,0,1,0,0,1,1,0,1,0,1,1,0,0,1,1,0,1,0,1,1,0,0,0,0,1,1,0,0,1,1,0,1,1,0,0,1,0,0,0,0,1,0,1,0,1,1,1,1,1,0,1,0,0,1,1,0,1,1,1,0,0,1,1,1,1,0,1,1,0,0,1,0,0,1,1,0,0,1,0,0,1,1,1,0,0,1,0,0,0,1,1,1,0,0,1,0,1,1,0,1,1,1,0,0,1,0,1,0,0,0,1,0,1,0,0,1,1,0,1,1,1,1,1,0,1,1,0,1,1,0,1,0,0,1,1,1,0,1,1,1,1,0,1,0,0,1,1,0,1,0,1,1,0,1,0,1,1,0,0,0,1,1,1,0,1,1,1,0,0,1,0,1,0,0,1,1,1,0,0,0,1,0,1,1,1,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,1,1,0,0,1,0,0,1,1,0,0,0,0,0,0,1,0,0,0,0},
						{0,0,1,0,1,0,1,0,1,0,0,1,1,1,0,1,0,0,0,1,1,0,0,1,0,1,1,1,0,1,1,0,0,0,1,0,0,1,0,1,1,1,1,0,1,0,0,0,0,1,1,1,0,1,0,1,1,0,0,1,0,1,1,1,1,1,0,0,0,0,0,1,0,0,0,0,0,1,1,0,0,0,1,1,0,0,1,1,0,1,1,1,0,1,0,0,0,0,0,0,0,0,1,0,1,0,0,0,1,0,0,0,0,1,0,0,1,1,0,0,0,1,1,1,0,1,0,0,1,0,1,0,1,1,1,1,1,0,0,1,1,1,1,1,1,1,0,0,0,1,1,0,0,0,0,1,0,0,1,0,1,0,1,1,0,0,0,0,1,1,1,1,1,0,1,1,0,1,0,1,0,0,1,1,0,1,0,1,0,1,0,0,1,0,1,0,1,0,0,1,1,0,0,0,1,1,0,1,0,1,1,0,0,1,1,0,1,1,1,0,0,1,0,0,1,1,1,0,0,0,1,0,1,1,0,1,1,1,1,0,0,0,1,1,0,1,1,1,1,0,1,1,1,1,0,1},
						{1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,1,1,1,1,1,0,1,1,1,1,1,1,0,0,0,1,1,1,0,0,1,1,1,1,0,0,1,1,0,1,1,0,1,1,1,0,0,0,1,1,0,0,1,1,1,0,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,1,0,1,0,0,0,1,0,1,1,1,0,0,1,1,0,0,1,0,0,0,1,0,1,1,1,0,0,0,1,1,1,0,0,0,1,1,0,1,0,0,1,1,1,1,0,1,0,0,1,1,1,1,1,0,1,0,1,0,1,0,1,1,0,1,1,0,1,1,1,0,0,0,0,1,1,0,0,0,1,0,1,1,1,1,0,1,0,0,0,1,0,0,1,0,1,0,0,1,1,1,0,1,1,0,0,0,0,1,0,0,0,1,0,1,1,0,0,1,0,1,0,1,1,0,0,1,1,0,1,1,1,1,1,1,0,1,1,0,1,0,0,1,1,1,1,0,1,1,1,1,1,1,0,0,1,0,0,0,1,1,1,0,1,0,0,0,1,0,0,0}};
*/

	int i;
	float fitness = 0.0, min_nl = 0.0, min_bal = 0.0, tr = 0.0;

//	u8 tt[2][4] = {{1,1,1,1},{0,1,1,1}}; //truth table dimension: 2^M for each of N Boolean functions

	u8 *ptr;

	int res_balance[255], res_nonlinearity[255]; // dimension 2^M-1

	u8 result[256] = {0};

	ptr = &tt[0][0];


	for (i = 1; i < (1 << N); i++) // start from 1, 0 does not have any interesting case
	{
		set_to_zero(result);

		if (i & 0x01) {
			xor_elements(result, tt[0], result);
		}
		if (i >> 1 & 0x01) {
			xor_elements(result, tt[1], result);
		}
		if (i >> 2 & 0x01) {
			xor_elements(result, tt[2], result);
		}
		if (i >> 3 & 0x01) {
			xor_elements(result, tt[3], result);
		}
		if (i >> 4 & 0x01) {
			xor_elements(result, tt[4], result);
		}
		if (i >> 5 & 0x01) {
			xor_elements(result, tt[5], result);
		}
		if (i >> 6 & 0x01) {
			xor_elements(result, tt[6], result);
		}
		if (i >> 7 & 0x01) {
			xor_elements(result, tt[7], result);
		}
		//res_balance[i-1] = balance (result);
		res_nonlinearity[i-1] = wt_nl (result);
	}

	//min_bal = find_bal(res_balance); //for balance check how many linear combinations are nonbalanced
	min_nl = find_min_nl(res_nonlinearity); //for nonlinearity look for the smallest

	//fitness = transparency(ptr);

	//printf("Min balance je %f\n", min_bal);

	// ovo je samo za nelinearnost:
	//printf("nl: %f, bal: %f\n", min_nl, min_bal);	
/*
	if (min_bal == 0)
	{
		float t = transparency2((u8 *)tt);
		tr = (M - t);
		//cout << "tr: " << t << endl;

/*		if (tr <= 0.5)
			tr = tr*20;
		else
			tr = tr*10;
*/
	/*	tr *= 1;
	}
	else
	{
		tr = 0;
	}

	// ovo nije realno ocekivati...
	if (tr > 0.2 && min_nl >= 110) 
		stop = true;
		*/
	//fitness = (float) (min_bal + min_nl) + tr;
	fitness = min_nl;

	return fitness;

}


//
// izracunaj samo nelinearnost
//
float nl(u8 tt[N][256])
{
	int i;
	float fitness = 0.0, min_nl = 0.0, min_bal = 0.0, tr = 0.0;

	u8 *ptr;

	int res_balance[255], res_nonlinearity[255]; // dimension 2^M-1

	u8 result[256] = {0};

	ptr = &tt[0][0];


	for (i = 1; i < (1 << N); i++) // start from 1, 0 does not have any interesting case
	{
		set_to_zero(result);

		if (i & 0x01) {
			xor_elements(result, tt[0], result);
		}
		if (i >> 1 & 0x01) {
			xor_elements(result, tt[1], result);
		}
		if (i >> 2 & 0x01) {
			xor_elements(result, tt[2], result);
		}
		if (i >> 3 & 0x01) {
			xor_elements(result, tt[3], result);
		}
		if (i >> 4 & 0x01) {
			xor_elements(result, tt[4], result);
		}
		if (i >> 5 & 0x01) {
			xor_elements(result, tt[5], result);
		}
		if (i >> 6 & 0x01) {
			xor_elements(result, tt[6], result);
		}
		if (i >> 7 & 0x01) {
			xor_elements(result, tt[7], result);
		}
		res_balance[i-1] = balance (result);
		res_nonlinearity[i-1] = wt_nl (result);
	}

	//min_bal = find_bal(res_balance); //for balance check how many linear combinations are nonbalanced
	min_nl = find_min_nl(res_nonlinearity); //for nonlinearity look for the smallest

	return min_nl;
}



void set_to_zero (u8 *res)		//set array elements to zero value
{
	int i;
	for (i=0; i < (1 << M); i++)
		res[i] = 0;
}

void xor_elements (u8 *a1, u8 *a2, u8 *res)
{
	int z;
	for (z = 0; z < (1 << M); z++)
	{
		res[z] = a1[z] ^ a2[z];
	}
}

int balance (u8 *tt) //this is maybe better with walsh transform coefficients
{
	int i, rez=0;

   for(i=0; i < (1 << M); i++)
   {
	   if (tt[i] == 0) //count zeros
		   rez=rez+1;
   }
   if (rez == ((1 << (M-1))))
	   return 0; //if the Boolean functions is balanced, we give nothing since it is constraint
   else
	   return 1;
}


int wt_nl (u8 *tt) //nonlinearity of the Boolean function
{
    int i, j, m, halfm, t1, t2, r, a, b, max = 0;

	int *rez=0;

	rez=(int *) malloc((1 << M)*sizeof(int));

    for(i=0; i < (1 << M); ++i )
        rez[i] = (tt[i] == 0)? 1 : -1;

    for( i = 1; i <= M; ++i ) {
        m  = (1 << i);
        halfm = m/2;
        for( r=0; r < (1 << M); r += m ) {
            t1 = r;
            t2 = r + halfm;
            for( j=0; j < halfm; ++j, ++t1, ++t2 ) {
                a = rez[t1];
                b = rez[t2];
                rez[t1] = a + b;
                rez[t2] = a - b;
				//help so I don't need to search for maximum later
				if (abs(rez[t1]) > max)
					max = abs(rez[t1]);
			    if (abs(rez[t2]) > max)
					max = abs(rez[t2]);
            }
        }
    }

	free(rez);

	return nonlinearity (max);
}

int nonlinearity (int max)
{
	return (((1 << M) - max)/2);
}


int hammingWeight(int x)
{
    int res;
    for( res = 0; x > 0; x = x >> 1 )
        res = res + (x & 0x01);
    return res;
}


float find_min_nl(int *tt)
{
	int i, res = 0;
	res = tt[0];
	for (i = 1; i < ((1 << M)-1); i++)
	{
		if (tt[i] < res)
			res = tt[i];
	}
	return (float)res;
}


float find_bal(int *tt)
{
	int i, res = 0;
	for (i = 0; i < ((1 << M)-1); i++)
	{
			res = res + tt[i];
	}
	if (res <= 5)
		res = res * (-2);
	else if (res > 5 && res <=50)
		res = res *(-1);
	else if (res > 50 && res <=100)
		res = res *(-0.5);
	else
		res = res *(-0.25);
	return (float) res;
}

float transparency (u8 *tt)
{
	float res = 0.0;
	float C = (float) ((1 << (2*N)) - (1 << N));
	int b, a, v, x, tmp1, tmp2;
	float sigma1, sigma2, sigma3 = 0;
	int tmp = 0;

	tmp1 = (1 << M);
	tmp2 = (1 << N);

	for (b = 0; b < tmp1; b++)
	{
		sigma1 = 0;
		for (a = 1; a < tmp2; a++)
		{
			sigma2 = 0;
			for (v = 1; v < tmp1; v = v << 1) //can go from 1 since we need that Hamming weight be 1
			{
				//if (hammingWeight(v) == 1)
				//{
					sigma3 = 0;
					for (x = 0; x < tmp2; x++)
					{
						sigma3 = sigma3 + (float) (1 - 2*inner_product(v, (evaluate_box(tt, x, a))));
					}
					sigma2 = sigma2 + (float) (1 - 2*inner_product(v, b)) * sigma3;
				//}
			}

			if (sigma2 < 0)
				sigma2 = sigma2 *(-1);

			sigma1 = sigma2 + sigma1;
		}
		tmp = 2 * hammingWeight(b);
		if (res < abs(M - tmp)-sigma1/C)
			res = abs(M - tmp)-sigma1/C;
	}
	return res;
}


int inner_product(int a, int b)
{
	int i, res = 0;
	for (i = 0; i < M; i++)
	{
		res = res ^ (((a >> i) & 0x01) & ((b >> i ) & 0x01));
	}
	return res;
}


int evaluate_box(u8 *tt, int x, int a)
{
 	int i, res1 = 0, res2 = 0, tmp, help;

	tmp = 1 << M;

	for (i = 0; i < M; i++)
	{
		help = *(tt + tmp*i + x);
		res1 |= ((*(tt + tmp*i + x)) << i);
	}

	x = x^a;
	for (i = 0; i < M; i++)
		res2 |= ((*(tt + tmp*i + x)) << i);

	return res1 ^ res2;
}

float transparency2 (u8 *tt)
{
	float res = 0.0;
	float C = (float) ((1 << (2*N)) - (1 << N));
	float K = (float) (N * (1<<N));
	float z = 0;
	int b, a, x, tmp1, tmp2;
	float sigma1 = 0, sigma2 = 0;
	int tmp = 0;

	tmp1 = (1 << M);
	tmp2 = (1 << N);


	for (b = 0; b < tmp2; b++)
	{
		sigma2 = 0;
		for (a = 1; a < tmp2; a++)
		{
			sigma1 = 0;
			for (x = 0; x < tmp2; x++)
			{
				sigma1 = sigma1 + hammingWeight(b^(evaluate_box(tt,x,a)));
			}
			z = K - 2*sigma1;
			if (z < 0)
				z = z*(-1);
			sigma2 = sigma2 + z;
		}
		tmp = 2 * hammingWeight(b);
		if (res < abs(M - tmp)-sigma2/C)
			res = abs(M - tmp)-sigma2/C;
	}
	
	return res;
}
