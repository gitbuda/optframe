#include <ecf/ECF.h>
//#include "EvalOp.h"
#include <iostream>
#include <fstream>
#include <string.h>
#include <stdlib.h>
#include <math.h>


// MOEA
#ifdef MOEA
#include "ECF/AlgNSGA.h"
#endif


int hamming_weight (int);
float computeKappa(int inputBits, int outputBits, int keyBits, int bit, unsigned char *Sbox);
float get_transparency_modified(unsigned char *sbox, int dim);
int get_delta_uniformity (unsigned char *Sbox);
/*
Program evoluira S-box uz pomoc permutacijskog genotipa
- za 8x8 s-box koristimo permutaciju 256 indeksa
- evaluacija se temelji na kodu iz transparency_evaluation.cpp
- 
*/


// za evaluaciju S-box, iz transparency_evaluation.cpp
// 8x8 s-box:
/*const int M = 8;
const int N = 8;
const int P = 256;
typedef unsigned char u8;
extern float eval(u8 tt[N][256], bool& stop);
extern float nl(u8 tt[N][256]);

*/
// za 4x4 s-box:

const int M = 4;
const int N = 4;
const int P = 16;
typedef unsigned char u8;
extern float eval(u8 tt[N][16], bool& stop);
float nl(u8 tt[N][16]);

extern float transparency2(u8 *);


// globalna varijabla za zadanu razinu nelinearnosti
uint targetNL = 0;
// kaznjavamo li rjesenja druge nelinearnosti
bool forceOnlyTargetNL = false;



//
// evaluator za Permutation reprezentaciju (tablica istinitosti)
// varijanta za S-box
//
class BitEvalOp : public EvaluateOp
{
protected:
	StateP state_;

public:
	u8 tt[N][P];
	uint nVariables;	// broj varijabli
	uint varijanta;		// varijanta fitness funkcije


	void registerParameters(StateP state)
	{
	}


	bool initialize(StateP state)
	{
		state_ = state;

		return true;
	}


#ifndef MOEA

	// redovna verzija fitnesa
	FitnessP evaluate(IndividualP individual)
	{
		FitnessP fitness (new FitnessMax);
		// za genetsko kaljenje je FitnessMin:
		//FitnessP fitness (new FitnessMin);

		Permutation::Permutation* perm = (Permutation::Permutation*) individual->getGenotype().get();

		// 8x8 s-box
		/*for(uint i = 0; i < P; i++)
		{
			tt[0][i] = perm->variables[i] >> 7 & 0x01;
			tt[1][i] = perm->variables[i] >> 6 & 0x01;
			tt[2][i] = perm->variables[i] >> 5 & 0x01;
			tt[3][i] = perm->variables[i] >> 4 & 0x01;
			tt[4][i] = perm->variables[i] >> 3 & 0x01;
			tt[5][i] = perm->variables[i] >> 2 & 0x01;
			tt[6][i] = perm->variables[i] >> 1 & 0x01;
			tt[7][i] = perm->variables[i] >> 0 & 0x01;
		}*/
		
		// 4x4 s-box
		
		for(uint i = 0; i < 16; i++)
		{
			tt[0][i] = perm->variables[i] >> 3 & 0x01;
			tt[1][i] = perm->variables[i] >> 2 & 0x01;
			tt[2][i] = perm->variables[i] >> 1 & 0x01;
			tt[3][i] = perm->variables[i] >> 0 & 0x01;
		}
		

		bool stop = false;
		float score = eval(tt, stop); //ovdje dobijem nelinearnost i transparency

		unsigned char *permutacija = new unsigned char[P];

		for (uint i = 0; i < P; i++)
		{
			permutacija[i] = perm->variables[i];
		}

		//ovdje nadodam drugi dio

		float confusion = computeKappa (8, 8, 8, 1, permutacija);
		//float confusion = computeKappa (4, 4, 4, 1, permutacija);
		float mto = get_transparency_modified(permutacija, P);
		int delta = get_delta_uniformity(permutacija);
		if(stop == true)
			state_->setTerminateCond();

		// ako je zadana razina nelinearnosti, ostale kazni
		if(forceOnlyTargetNL && ((uint) score) != targetNL)
			score = 0;

		score = score + ((1 << M) - delta);
		score = score + confusion;
		score = score + (M - mto);
		fitness->setValue(score);

		delete(permutacija);
		return fitness;
	}
#endif



#ifdef MOEA

	// MOEA verzija fitnesa
	FitnessP evaluate(IndividualP individual)
	{
		MOFitnessP fitness = static_cast<MOFitnessP> (new MOFitness);
		// za genetsko kaljenje je FitnessMin:
		//FitnessP fitness (new FitnessMin);

		Permutation::Permutation* perm = (Permutation::Permutation*) individual->getGenotype().get();

		// 8x8 s-box
		/*
		for(uint i = 0; i < P; i++)
		{
			tt[0][i] = perm->variables[i] >> 7 & 0x01;
			tt[1][i] = perm->variables[i] >> 6 & 0x01;
			tt[2][i] = perm->variables[i] >> 5 & 0x01;
			tt[3][i] = perm->variables[i] >> 4 & 0x01;
			tt[4][i] = perm->variables[i] >> 3 & 0x01;
			tt[5][i] = perm->variables[i] >> 2 & 0x01;
			tt[6][i] = perm->variables[i] >> 1 & 0x01;
			tt[7][i] = perm->variables[i] >> 0 & 0x01;
		}*/
		
		// 4x4 s-box
		
		for(uint i = 0; i < 16; i++)
		{
			tt[0][i] = perm->variables[i] >> 3 & 0x01;
			tt[1][i] = perm->variables[i] >> 2 & 0x01;
			tt[2][i] = perm->variables[i] >> 1 & 0x01;
			tt[3][i] = perm->variables[i] >> 0 & 0x01;
		}
		

		bool stop = false;
		//float score = eval(tt, stop);

		float nonlinearity = nl(tt);

		unsigned char *permutacija = new unsigned char[P];

		for (uint i = 0; i < P; i++)
		{
			permutacija[i] = perm->variables[i];
		}

		//ovdje nadodam drugi dio

		float confusion = computeKappa (8, 8, 8, 1, permutacija);
		//float confusion = computeKappa (4, 4, 4, 1, permutacija);

		float to = transparency2((u8 *)tt);

		float mto = get_transparency_modified(permutacija, P);
		int delta = get_delta_uniformity(permutacija);
		if(stop == true)
			state_->setTerminateCond();

		// ako je zadana razina nelinearnosti, ostale kazni
		/*if(forceOnlyTargetNL && ((uint) score) != targetNL)
			score = 0;
*/
		// komponente MO fitnesa:
		fitness->push_back((FitnessP) new FitnessMax);
		fitness->back()->setValue(nonlinearity);

		fitness->push_back((FitnessP) new FitnessMin);
		fitness->back()->setValue(delta);

		fitness->push_back((FitnessP) new FitnessMin);
		fitness->back()->setValue(mto);

		//fitness->push_back((FitnessP) new FitnessMin);
		//fitness->back()->setValue(to);

		//fitness->push_back((FitnessP) new FitnessMax);
		//fitness->back()->setValue(confusion);

		delete(permutacija);
		return fitness;
	}
#endif


	uint nelinearnost(IndividualP individual)
	{
		Permutation::Permutation* perm = (Permutation::Permutation*) individual->getGenotype().get();

		for(uint i = 0; i < P; i++)
		{
			tt[0][i] = perm->variables[i] >> 7 & 0x01;
			tt[1][i] = perm->variables[i] >> 6 & 0x01;
			tt[2][i] = perm->variables[i] >> 5 & 0x01;
			tt[3][i] = perm->variables[i] >> 4 & 0x01;
			tt[4][i] = perm->variables[i] >> 3 & 0x01;
			tt[5][i] = perm->variables[i] >> 2 & 0x01;
			tt[6][i] = perm->variables[i] >> 1 & 0x01;
			tt[7][i] = perm->variables[i] >> 0 & 0x01;
		}

		return (uint) nl(tt);
	}


};




/*
Ova main funkcija radi ovisno o broju argumenata:
- samo uz datoteku s parametrima, evoluira s-box u obliku permutacije
	(primjer: <exe> parameters.txt)
- za 3 argumenta, cita s-box iz 3. argumenta, prepise preko svih jedinki i mutira 
	(primjer <exe> parameters.txt aes.txt)
- za 4 argumenta, mutira na zadanu razinu nelinearnosti
	(primjer <exe> parameters.txt aes.txt 100)
- za 5 argumenata, kaznjava jedinke koje nemaju zadanu razinu nelinearnosti
	(primjer <exe> parameters.txt aes.txt 100 1)
*/
int main(int argc, char **argv)
{
	StateP state (new State);

	// set the evaluation operator
	BitEvalOp *eval = new BitEvalOp;
	state->setEvalOp(eval);

#ifdef MOEA
	// ukljuci MOEA algoritam
	AlgNSGAP alg = (AlgNSGAP) (new AlgNSGA());
	state->setAlgorithm(alg);
#endif

	state->initialize(argc, argv);


	// seeding: procitaj iz fajla
	if(argc == 3) {
		XMLNode xInd = XMLNode::parseFile(argv[2], "Individual");
		IndividualP ind = (IndividualP) new Individual(state);
		ind->read(xInd); 
		//state->getAlgorithm()->evaluate(ind);
		//std::cout << ind->toString();

		// pa zamijeni sve u populaciji mutiranim AES rjesenjem
		for(uint i = 0; i < state->getPopulation()->getLocalDeme()->size(); i++) {
			// kopiraj i mutiraj dok nelinearnost ne bude manja od 112
			IndividualP novi = (IndividualP) ind->copy();
			do {
				state->getAlgorithm()->mutation_->mutate(novi);
			}while(eval->nelinearnost(novi) > 110);

			// stavi u populaciju
			state->getPopulation()->getLocalDeme()->replace(i, novi);
		}
	}


	// seeding: procitaj iz fajla, citaj zadanu nelinearnost
	if(argc > 3) {
		targetNL = atoi(argv[3]);
		// kaznjavamo li ostale?
		if(argc > 4)
			forceOnlyTargetNL = true;

		XMLNode xInd = XMLNode::parseFile(argv[2], "Individual");
		IndividualP ind = (IndividualP) new Individual(state);
		ind->read(xInd); 

		// pa zamijeni sve u populaciji mutiranim AES rjesenjem
		for(uint i = 0; i < state->getPopulation()->getLocalDeme()->size(); i++) {
			// kopiraj i mutiraj dok nelinearnost ne bude jednaka zadanoj
			IndividualP novi;
			do {
				novi = (IndividualP) ind->copy();
				state->getAlgorithm()->mutation_->mutate(novi);
			}while(eval->nelinearnost(novi) != targetNL);

			// stavi u populaciju
			state->getPopulation()->getLocalDeme()->replace(i, novi);
		}
	}

	state->run();

	// after the evolution: show best
	std::vector<IndividualP> hof = state->getHoF()->getBest();
	IndividualP ind = hof[0];
	std::cout << ind->toString();
#ifdef MOEA
	state->getAlgorithm()->evalOp_.get()->evaluate(ind);
#else
	state->getEvalOp().get()->evaluate(ind);
#endif


#ifdef MOEA
	//
	// ispis MOEA vrijednosti u posebnu datoteku:
	//
	std::ofstream myfile;
	myfile.open ("paretoFront.txt");
	DemeP deme = state->getPopulation()->getLocalDeme();
	for (uint i = 0; i<deme->size(); i++) {
		MOFitnessP fitness = boost::static_pointer_cast<MOFitness> (deme->at(i)->fitness);
		for (uint f = 0; f < fitness->size(); f++)
			myfile << fitness->at(f)->getValue() << "\t";
		myfile << "\n";
	}
	myfile.close();
#endif

	return 0;
}



/*
Ova main funkcija cita gotovo rjesenje (npr aes.txt) i mutira ga,
dobivena rjesenja svrstava u razine nelinearnosti (110, 108, ... 100)
i zapisuje u posebne datoteke
*/
/*
int main(int argc, char **argv)
{
	StateP state (new State);

	// set the evaluation operator
	BitEvalOp *eval = new BitEvalOp;
	state->setEvalOp(eval);

	state->initialize(argc, argv);

	// seeding: procitaj iz fajla
	if(argc > 2) {
		XMLNode xInd = XMLNode::parseFile(argv[2], "Individual");
		IndividualP ind = (IndividualP) new Individual(state);
		ind->read(xInd); 
		//state->getAlgorithm()->evaluate(ind);
		//std::cout << ind->toString();

		// brojaci za razlicite razine nelinearnosti
		uint levels = 6;
		std::vector<uint> number(levels,0);
		// koliko treba prikupiti (recimo 50)
		uint limit = 50;
		bool finished = false;

		while(!finished) {
			// kopiraj i mutiraj
			IndividualP novi = (IndividualP) ind->copy();
			state->getAlgorithm()->mutation_->mutate(novi);

			uint nl = eval->nelinearnost(novi);
			std::cout << "nl: " << nl << std::endl;

			ofstream out;
			bool skip = false;
			switch(nl) {
				case 110: out.open("110.txt", ios_base::app); number[0]++; 
					if(number[0] > limit)
						skip = true;
					break;
				case 108: out.open("108.txt", ios_base::app); number[1]++;  
					if(number[1] > limit)
						skip = true;
					break;
				case 106: out.open("106.txt", ios_base::app); number[2]++;  
					if(number[2] > limit)
						skip = true;
					break;
				case 104: out.open("104.txt", ios_base::app); number[3]++;  
					if(number[3] > limit)
						skip = true;
					break;
				case 102: out.open("102.txt", ios_base::app); number[4]++;  
					if(number[4] > limit)
						skip = true;
					break;
				case 100: out.open("100.txt", ios_base::app); number[5]++;  
					if(number[5] > limit)
						skip = true;
					break;
				default: skip = true;
			}

			if(skip)	// nije dovoljno dobar ili vec imamo dovoljno
				continue;

			// evaluiraj i zapisi
			state->getAlgorithm()->evaluate(novi);
			out << novi->toString() << std::endl;
			out.close();

			// jesmo gotovi?
			finished = true;
			for(uint l = 0; l < levels; l++)
				if(number[l] < limit)
					finished = false;
		}

		// pa stavi kao prvi u populaciji
		//IndividualP first = state->getPopulation()->getLocalDeme()->at(0);
		//state->getPopulation()->getLocalDeme()->replace(0, ind);
	}

	//state->run();

	return 0;
}
*/



/*
Ova main funkcija ucitava postojece rjesenje (npr. aes.txt), kopira ga na sve jedinke u populaciji
i pokrece evoluciju (namijenjeno za genetsko kaljenje)
- za genetsko kaljenje: fitness mora biti nariktan za minimizaciju!!!
*/
/*
int main(int argc, char **argv)
{
	StateP state (new State);

	// set the evaluation operator
	state->setEvalOp(new BitEvalOp);

	state->initialize(argc, argv);

	// seeding: procitaj iz fajla
	if(argc > 2) {
		XMLNode xInd = XMLNode::parseFile(argv[2], "Individual");
		IndividualP ind = (IndividualP) new Individual(state);
		ind->read(xInd); 
		state->getAlgorithm()->evaluate(ind);
		//std::cout << ind->toString();


		// pa zamijeni sve u populaciji
		for(uint i = 0; i < state->getPopulation()->getLocalDeme()->size(); i++) {
			IndividualP p = state->getPopulation()->getLocalDeme()->at(i);
			state->getPopulation()->getLocalDeme()->replace(i, (IndividualP) ind->copy());
		}
	}

	state->run();

	return 0;
}*/


float computeKappa(int inputBits, int outputBits, int keyBits, int bit, unsigned char *Sbox)
{ 
	int inputSize = 1 << inputBits;
	int outputSize = 1 << outputBits;
	int keySize = 1 << keyBits;
	int coefficientSize = (keySize * (keySize-1)) >> 1; // combinatorics on key picks i and j
	int confusionCounter = 0; //# of times we observe confusion
	int outi,outj; // Sbox output	
	int coefficientCounter = 0; //how many coefficients have we computed
	int keyi, keyj, input, i = 0, j = 0, k = 0,  fcounter = 0, in = 0;
	float mean = 0.0, var = 0.0, coefficientSum = 0.0;
	
	uint *temp_array = (uint *) malloc (sizeof(uint) * (1 << inputBits)) ;
	float *reducedCoefficients = (float *) malloc (coefficientSize * sizeof (float));
	float *frequency = (float *) malloc (coefficientSize * sizeof (float));
	float *confusionCharacteristic = (float *) malloc (coefficientSize * sizeof (float)); 
	
	if ((1 << M) == (1 << inputBits))
	{
		for (i = 0; i < (1 << M); i++)
				temp_array[i] =  Sbox[i];	
	}
	else if (((1 << M) * (1 << N)) == (1 << inputBits))
	{
		for (i = 0; i < (1 << M); i++)
			for (j = 0; j < (1 << N); j++)
				temp_array[i*16 + j] =  (Sbox[i] << M) ^ Sbox[j];
	}

	for (keyi = 0; keyi < keySize; keyi++)
	{
		for (keyj = keyi + 1; keyj < keySize; keyj++)
		{		
			for (input = 0; input < inputSize ; input++)
			{
				outi = temp_array[keyi ^ input];
				outj = temp_array[keyj ^ input];
				
				coefficientSum = (float) (coefficientSum + (float) (hamming_weight(outi) - hamming_weight(outj)) * (hamming_weight(outi) - hamming_weight(outj)));
				//if (input == 1 && keyi==0)
					//printf("%f\n", coefficientSum);		
			}	
			//input set is over, lets compute confusion coefficient for (keyi, keyj)
			confusionCharacteristic[coefficientCounter]=(float)coefficientSum / (float)inputSize;
		
			coefficientCounter ++;
			confusionCounter = 0; //dpa
			coefficientSum = 0; //cpa
		}
	}

	fcounter = 0;
	for (i = 0; i < coefficientSize; i++)
	{
		if(confusionCharacteristic[10] == confusionCharacteristic[i])
		{
			fcounter++;
		}
		mean = mean + confusionCharacteristic[i];
	}
	//printf("%f\n", mean);
	mean = mean / (float)coefficientSize;

	for (i = 0; i < coefficientSize; i++)
		var = (float) (var + (float) pow((confusionCharacteristic[i] - (float) mean), 2));

	var = var / (float)coefficientSize;

	free (temp_array);
	free (reducedCoefficients);
	free (confusionCharacteristic);
	free (frequency);

	return var;
}


float computeKappaa(int inputBits, int outputBits, int keyBits, int bit, unsigned char *aesSbox)
{
	int inputSize = 1 << inputBits;
	int outputSize = 1 << outputBits;
	int keySize = 1 << keyBits;
	int coefficientSize = (keySize * (keySize-1)) >> 1; // combinatorics on key picks i and j
	float *confusionCharacteristic = (float *) malloc (coefficientSize * sizeof (float)); // the confusion characteristic of the target Sbox or function
	int confusionCounter = 0; //# of times we observe confusion
	int outi,outj; // Sbox output	
	int start = 0;
	int coefficientCounter = 0; //how many coefficients have we computed
	int keyi, keyj, input, i = 0, j = 0, k = 0;	
	float coefficientSum = 0.0;
	int fcounter = 0, in = 0;
	float mean = 0.0, var = 0.0;
		
	for (keyi = 0; keyi < keySize; keyi++)
	{
		for (keyj = keyi + 1; (keyj < keySize); keyj++)
		{		
			for (input = 0; input < inputSize ; input++)
			{
				outi = aesSbox[keyi ^ input];
				outj = aesSbox[keyj ^ input];
				coefficientSum = (float) (coefficientSum + ((float) pow((float) (hamming_weight(outi) - hamming_weight(outj)), 2)));

			}	
			confusionCharacteristic[coefficientCounter]=(float)coefficientSum/(float)inputSize;
			coefficientCounter ++;
			confusionCounter = 0; //dpa
			coefficientSum = 0; //cpa
			start++;
		}
	}

	fcounter = 0;
	for (i = 0; i < coefficientSize; i++)
	{
		if(confusionCharacteristic[10] == confusionCharacteristic[i])
		{
			fcounter++;
		}
		mean = mean + confusionCharacteristic[i];
	}
	
	mean = mean / (float)coefficientSize;

	for (i = 0; i < coefficientSize; i++)
	{
		var = (float) (var + (float) pow((confusionCharacteristic[i] - (float) mean), 2));
	}
	var = var / (float)coefficientSize;
	
	free (confusionCharacteristic);	
	return var;
}


int hamming_weight (int x)
{
    int res;
    for (res = 0; x > 0; x = x >> 1)
        res = res + (x & 0x01);
    return res;
}


float get_transparency_modified(unsigned char *sbox, int dim)
{
	int i, j, a, sum1, sum_over_a, x;
	int beta, auto_corr, cross_corr, sum_cross_corr, help;
	float tau, tau_max, neg_part;
	unsigned char *fx1, *fx2;

	fx1 = (unsigned char *) malloc (sizeof (unsigned char) * dim);
	fx2 = (unsigned char *) malloc (sizeof (unsigned char) * dim);

	help = (1 << (2 * N)) - dim;
	tau_max = 0;

	for(beta = 0; beta < dim; beta++)
	{
		sum_over_a = 0;
		for(a = 1; a < dim; a++)
		{
			sum1 = 0;
			for(j = 0; j < N; j++)
			{
				for(x = 0; x < dim; x++) 
					fx1[x] = (sbox[x] & (1 << j)) >> j;
				auto_corr = 0; // compute autocorrelation of F_j
				for(x = 0; x < dim; x++)
				{
					if(((sbox[x] & (1 << j)) >> j) == (((sbox[x^a] & (1 << j)) >> j))) 
						auto_corr++;
					else auto_corr--;	
				}

				sum_cross_corr = 0;
				for(i = 0; i < N; i++)
				{
					for(x = 0; x < dim; x++) 
						fx2[x] = (sbox[x] & (1 << i)) >> i;
					if(i == j) continue;
					cross_corr = 0;	// compute cross correlation of F_i and F_j
					for(x = 0; x < dim; x++) 
					{
						if(fx1[x] == fx2[x^a]) 
							cross_corr++;
						else cross_corr--;
					}

					if(((beta & (1 << i)) >> i) == ((beta & (1 << j)) >> j)) 
						sum_cross_corr += cross_corr;
					else 
						sum_cross_corr -= cross_corr;
				}

				sum1 += abs(auto_corr + sum_cross_corr);
			}
			sum_over_a += sum1;
		}
		neg_part  = (float) sum_over_a/help;
		tau = N - neg_part;
		if(tau > tau_max) 
			tau_max = tau; // maximum tau over all beta
	}

	tau = tau_max;
	free (fx1);
	free (fx2);
	return tau;
}


int get_delta_uniformity (unsigned char *Sbox)
{
	uint i, j, delta = 0, R = 0;	
	uint **DDT;
	
	DDT = (uint **) malloc ((1<< M) * sizeof(uint *));
	
	for (i = 0; i < (1<< M); i++)
	{
		DDT[i] = (uint *) malloc ((1<< N) * sizeof(uint));
		memset (DDT[i], 0, (1<< N) * sizeof(uint));
	}

	for (i = 0; i < (1<< M); i++)
	{
		for (j = 0 ; j < (1<< N); j++)
		{
			DDT [i ^ j] [Sbox[i] ^ Sbox[j]]++;			
		}
	}

	for (i = 0; i < (1<< M); i++)
	{
		for (j = 0 ; j < (1<< N); j++)
		{
			if (DDT [i][j] > delta && (i != 0 && j != 0))
				delta = DDT [i][j];	
		}
	}

	for (i = 1; i < (1<< N); i++)
	{
		if (DDT [i][0] != 0)
			R++;
	}
	
	for (i = 0; i < (1<< M); i++)
    {
    	free(DDT[i]);
    }
    free(DDT);

	return delta;
}
