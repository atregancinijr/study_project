#include "Caixa.hpp"
#include<string>
#include "DiaDaSemana.hpp"

Caixa::Caixa(Cpf cpf, std::string nome, float salario, DiaDaSemana dia_do_pagamento):
Funcionario(cpf, nome, salario, dia_do_pagamento)
{

}

float Caixa::bonificacao() const
{
    return recupera_salario() * 0.1;
}