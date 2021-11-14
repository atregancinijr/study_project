#pragma once
#include "Conta.hpp"
#include <string>

class ContaCorrente final:public Conta{
    public:ContaCorrente(std::string numero_conta, Titular titular);
     //override verifica se a assinatura bate com algum método virtual da classe base.
    public:float retorna_taxa_de_saque() const override;

    void transfere_para(Conta& conta, float valor);
    void operator+=(ContaCorrente& conta_origem);
};