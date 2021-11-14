#include "ContaPoupanca.hpp"
#include "Titular.hpp"
#include <iostream>

ContaPoupanca::ContaPoupanca(std::string numero_conta, Titular titular):
Conta(numero_conta, titular)
{

}

float ContaPoupanca::retorna_taxa_de_saque() const
{
    return 0.0;
}