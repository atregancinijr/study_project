#include "ContaCorrente.hpp"
#include "Titular.hpp"
#include <iostream>
#include "Conta.hpp"

ContaCorrente::ContaCorrente(std::string numero_conta, Titular titular):
Conta(numero_conta, titular)
{

}

float ContaCorrente::retorna_taxa_de_saque() const
{
    return 0.05;
}

void ContaCorrente::transfere_para(Conta& conta, float valor)
{
    auto status_saque = sacar(valor);
    
    if (status_saque.index() == 1)
    {
        conta.depositar(valor);
    }

}

void ContaCorrente::operator+=(ContaCorrente& conta_origem)
{
    conta_origem.transfere_para(*this, conta_origem.recupera_saldo() / 2);
}