#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <map>
#include <unordered_set>
#include <set>
#include <ctime>
#include <regex>

typedef std::map<std::string, std::string> map_ss;

bool regex_match(const std::string &text, const std::string &filter) {
    return std::regex_match(text, std::regex(filter, std::regex_constants::basic));
}

map_ss readInputArguments(int argc, char *argv[]) {

    map_ss keyValue;
    std::string keyRegex("-[a-z]");

    for (int i = 1; i < argc; ++i) {
        std::string key(argv[i]);
        if (regex_match(key, keyRegex)) {
            if (i != argc - 1) {
                std::string value(argv[i + 1]);
                if (regex_match(value, keyRegex)) {
                    std::cerr << "Input arguments error" << std::endl;
                    exit(-1);
                }
                keyValue[key] = value;
            } else {
                std::cerr << "Input arguments error" << std::endl;
                exit(-1);
            }
        }
    }

    return keyValue;
}

