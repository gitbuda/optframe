#include <iostream>

#include "utils.hpp"

using namespace std;

typedef unsigned int uint;
typedef vector<string> vectors;
typedef set<string> unique_container;
typedef map<string, vectors> key_list;
typedef vector<double> vectord;
typedef vector<bool> vectorb;
typedef pair<string, string> string_pair;
typedef map<string_pair, int> pair_int;
typedef vector<int> vectori;

class Pipeline {

private:
    float layerCost_;
    float latencyCost_;

    float layerPenalty_; // parameter e.g. 1000
    int validLayerSum_; // parameter e.g. 1

    key_list parentChild_;
    vectord elementCost_;
    pair_int linkIndex_;
    vectors parent_element_container_;
    vectorb bistabil_;

    vectori path_;
    vectorb isLeaf_;

    void evaluateRecursive_(string element, int layerSum, float latencySum) {
        if (this->parentChild_.find(element) == parentChild_.end()) {
            if (layerSum != this->validLayerSum_) {
                this->layerCost_ += this->layerPenalty_;
            }
            if (latencySum > this->latencyCost_) {
                this->latencyCost_ = latencySum;
            }
            return;
        }
        vectors childContainer = this->parentChild_[element];
        for(vectors::iterator it = childContainer.begin(); it != childContainer.end(); it++) {
            string child = *it;
            int index = this->linkIndex_[make_pair(element, child)];
            bool isBistabil = this->bistabil_[index];
            float newLatencySum = latencySum + this->elementCost_[index];
            int  newLayerSum = layerSum + (int)isBistabil;
            if (isBistabil) {
                if (newLatencySum > this->latencyCost_) {
                    this->latencyCost_ = newLatencySum;
                }
                newLatencySum = 0;
            }
            this->evaluateRecursive_(child, newLayerSum, newLatencySum);
        }
    }

    void createFlatPath_(string element, vectori current) {
        if (this->parentChild_.find(element) == this->parentChild_.end()) {
            for (uint i = 0; i < current.size(); ++i) {
                int pathElement = current[i];
                this->path_.push_back(pathElement);
            }
            return;
        }
        vectors childContainer = this->parentChild_[element];
        for(vectors::iterator it = childContainer.begin(); it != childContainer.end(); ++it) {
            string child = *it;
            int index = this->linkIndex_[make_pair(element, child)];
            vectori new_current(current.begin(), current.end());
            new_current.push_back(index);
            this->createFlatPath_(child, new_current);
        }
    }

    void calculateIsLeaf_() {
        this->isLeaf_ = vectorb(this->elementCost_.size(), false);
        for(key_list::iterator it = this->parentChild_.begin(); it != this->parentChild_.end(); it++) {
            string parent = it->first;
            vectors childs = it->second;
            for (vectors::iterator itc = childs.begin(); itc != childs.end(); itc++) {
                string child = *itc;
                string_pair parent_child = make_pair(parent, child);
                if (this->parentChild_.find(child) == this->parentChild_.end()) {
                    int branchIndex = this->linkIndex_[parent_child];
                    this->isLeaf_[branchIndex] = true;
                }
            }
        }
    }

public:
    Pipeline() {
        // TODO: load from config
        this->layerCost_ = 0;
        this->latencyCost_ = 0;

        this->layerPenalty_ = 1000;
        this->validLayerSum_ = 1;
    }

    void resetCost() {
        this->layerCost_ = 0;
        this->latencyCost_ = 0;
    }

    void loadPipeline(string path) {

        // read file
        string line;
        ifstream pipelineDescription(path);
        if (pipelineDescription.is_open()) {

            cout << "Opened file: " << path << endl;
            unique_container all_childs;
            while (getline(pipelineDescription, line)) {
                istringstream iss(line);
                string parent; iss >> parent;
                // cout << "Parent: " << parent << endl;
                this->parentChild_[parent] = vectors();
                int childs_no; iss >> childs_no;
                // cout << "Childs no: " << childs_no << endl;
                vectors childs;
                for (int i = 0; i < childs_no; ++i) {
                    string child; iss >> child;
                    childs.push_back(child);
                    all_childs.insert(child);
                }
                float elementCost; iss >> elementCost;
                for (int i = 0; i < childs_no; ++i) {
                    string child = childs[i];
                    this->parentChild_[parent].push_back(child);
                    this->linkIndex_[make_pair(parent, child)] = elementCost_.size();
                    this->linkIndex_[make_pair(child, parent)] = elementCost_.size();
                    this->elementCost_.push_back(elementCost);
                }
            }
            pipelineDescription.close();

            cout << "Preprocessing..." << endl;

            for(key_list::iterator it = this->parentChild_.begin(); it != this->parentChild_.end(); it++) {
                string parent = it->first;
                const bool is_in = all_childs.find(parent) != all_childs.end();
                if (!is_in) {
                    this->parent_element_container_.push_back(parent);
                }
            }

            for (uint i = 0; i < this->parent_element_container_.size(); ++i) {
                string parent = this->parent_element_container_[i];
                vectori path;
                this->createFlatPath_(parent, path);
            }

            this->calculateIsLeaf_();
        } else {
            cout << "Unable to open pipeline file";
        }
    }

    float evaluateRecursive(vector<bool> fitness) {
        this->bistabil_ = fitness;
        for (unsigned int i = 0; i < this->parent_element_container_.size(); ++i) {
            string parent = this->parent_element_container_[i];
            this->evaluateRecursive_(parent, 0, 0);
        }
        return this->layerCost_ + this->latencyCost_;
    }

    float evaluateIterative(vector<bool> genotype) {
        this->bistabil_ = genotype;
        int bitSum = 0;
        float latencySum = 0;
        float maxCurrentLatencySum = 0;
        for (uint i = 0; i < this->path_.size(); ++i) {
            int link_index = this->path_[i];
            bool isBistabil = this->bistabil_[link_index];
            float latency = this->elementCost_[link_index];
            bool isLeaf = this->isLeaf_[link_index];
            bitSum += isBistabil ? 1 : 0;
            latencySum += latency;
            if (isBistabil || isLeaf) {
                if (latencySum > maxCurrentLatencySum) {
                    maxCurrentLatencySum = latencySum;
                    if (maxCurrentLatencySum > this->latencyCost_) {
                        this->latencyCost_ = maxCurrentLatencySum;
                    }
                }
                latencySum = 0;
            }
            if (isLeaf) {
                if (bitSum != this->validLayerSum_) {
                    this->layerCost_ += this->layerPenalty_;
                }
                bitSum = 0;
            }
        }
        return this->layerCost_ + this->latencyCost_;
    }

};

// c interface
extern "C" {
    static Pipeline *pipeline;

    void load(char *pipeline_path) {
        string pipelinePath(pipeline_path);
        pipeline = new Pipeline();
        pipeline->loadPipeline(pipelinePath);
    }

    float evaluate(int genotype[], int size) {
        pipeline->resetCost();
        vectorb bool_genotype;
        for (int i = 0; i < size; ++i) {
            int bit = genotype[i];
            if (bit == 0) bool_genotype.push_back(false);
            if (bit == 1) bool_genotype.push_back(true);
        }
        float cost = pipeline->evaluateIterative(bool_genotype);
        return -cost;
    }
}

void evaluateSolutionFile(string &pipelinePath, string &solutionPath) {

    Pipeline *pipeline = new Pipeline();
    pipeline->loadPipeline(pipelinePath);

    vector<bool> genotype;
    ifstream genotypeFile(solutionPath);
    if (genotypeFile.is_open()) {
        string line;
        while (getline(genotypeFile, line)) {
            istringstream iss(line);
            do {
                char bit; iss >> bit;
                if (bit == '0') genotype.push_back(false);
                if (bit == '1') genotype.push_back(true);
            } while (iss);
        }
        cout << "Genotype file loaded: " << solutionPath << endl;
    } else {
        cout << "Unable to open genotype file" << endl;
    }

    clock_t begin = clock();
    cout << "Evaluation..." << endl;
    cout << "Cost: " << pipeline->evaluateIterative(genotype) << endl;
    clock_t end = clock();
    double elapsed_secs = double(end - begin) / CLOCKS_PER_SEC;
    cout << "Evaluation time: " << elapsed_secs << endl;
}

int main(int argc, char *argv[]) {

    map_ss inputArguments = readInputArguments(argc, argv);

    string pipelinePath = inputArguments["-p"];
    string solutionPath = inputArguments["-s"];
    
    if (pipelinePath.empty()) {
        pipelinePath = "input/sbox_real.txt";
    }
    if (solutionPath.empty()) {
        solutionPath = "input/genotype1.txt";
    }
    
    evaluateSolutionFile(pipelinePath, solutionPath);

    return 0;
}
