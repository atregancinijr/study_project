#pragma once
#include "Conta.hpp"
#include <string>

class ContaPoupanca final:public Conta{
    public:ContaPoupanca(std::string numero_conta, Titular titular);
     //override verifica se a assinatura bate com algum método virtual da classe base.
    public:float retorna_taxa_de_saque() const override;
};