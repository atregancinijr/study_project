#include "Gerente.hpp"
#include<string>

Gerente::Gerente(Cpf cpf, std::string nome, float salario, DiaDaSemana dia_do_pagamento, std::string senha):
Funcionario(cpf, nome, salario, dia_do_pagamento), Autenticavel(senha)
{

}

float Gerente::bonificacao() const
{
    return recupera_salario() * 0.5;
}