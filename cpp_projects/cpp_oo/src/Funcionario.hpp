#pragma once
#include <string>
#include "Cpf.hpp"
#include "PessoaFisica.hpp"
#include "DiaDaSemana.hpp"

class Funcionario:public PessoaFisica{

    private:float salario;
    DiaDaSemana dia_do_pagamento;

    public:Funcionario(Cpf cpf, std::string nome, float salario, DiaDaSemana dia_do_pagamento); //construtores 
    public:float recupera_salario() const;
    protected:virtual float bonificacao() const = 0;
};