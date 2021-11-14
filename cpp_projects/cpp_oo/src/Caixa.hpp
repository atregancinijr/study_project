#pragma once
#include "Funcionario.hpp"
#include "Cpf.hpp"

class Caixa final: public Funcionario{
    public:Caixa(Cpf cpf, std::string nome, float salario, DiaDaSemana dia_do_pagamento);
    public:float bonificacao() const;
};