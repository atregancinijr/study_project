#pragma once
#include "Leilao.hpp"
#include "Lance.hpp"
#include<vector>

class Avaliador
{
private:
    float maiorValor = FLT_MIN;
    float menorValor = FLT_MAX;
    std::vector<Lance> maiores3Lances;
    static bool ordenaLances(const Lance&, const Lance&);
public:
    void avalia(Leilao);
    float recuperaMaiorValor() const;
    float recuperaMenorValor() const;
    std::vector<Lance> recupera3MaioresLances() const;
};
