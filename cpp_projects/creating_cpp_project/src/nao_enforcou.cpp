#include "nao_enforcou.hpp"

bool nao_enforcou(std::vector<char> &chutes_errados, const unsigned int &num_de_tentativas){
    return chutes_errados.size() < num_de_tentativas;
}