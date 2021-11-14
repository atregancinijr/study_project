#include "Leilao.hpp"
#include <iostream>
Leilao::Leilao(std::string descricao) : descricao(descricao)
{

}

const std::vector<Lance>& Leilao::recuperaLances() const
{
    return lances;
}

void Leilao::recebeLance(const Lance& lance)
{
    std::cout << "[l-value]" << std::endl;
    if (lances.size() == 0 ||
        lances.back().recuperaUsuario().recuperaNome() != lance.recuperaUsuario().recuperaNome()) {
        lances.push_back(lance);
    }

}

void Leilao::recebeLance(Lance&& lance) {
    std::cout << "[r-value]" << std::endl;
    if (lances.size() == 0 ||
        lances.back().recuperaUsuario().recuperaNome() != lance.recuperaUsuario().recuperaNome()) {
        lances.push_back(lance);
    }
}