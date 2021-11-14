#include<vector>
#include "nao_enforcou.hpp"

extern std::vector<char> chutes_errados;
extern const int NUMERO_DE_TENTATIVAS = 5;

bool nao_enforcou(){
    return chutes_errados.size() < NUMERO_DE_TENTATIVAS;
}