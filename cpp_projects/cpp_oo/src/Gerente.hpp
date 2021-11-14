#pragma once
#include "Funcionario.hpp"
#include "Autenticavel.hpp"
#include "Cpf.hpp"
#include "DiaDaSemana.hpp"

class Gerente final: public Funcionario, public Autenticavel{
    public:Gerente(Cpf cpf, std::string nome, float salario, DiaDaSemana dia_do_pagamento, std::string senha);
    public:float bonificacao() const;
};