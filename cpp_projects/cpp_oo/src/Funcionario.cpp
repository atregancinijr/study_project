#include "Funcionario.hpp"

Funcionario::Funcionario(Cpf cpf, std::string nome, float salario, DiaDaSemana dia_do_pagamento):
PessoaFisica(cpf, nome), salario(salario), dia_do_pagamento(dia_do_pagamento)
{

}

float Funcionario::recupera_salario() const
{
    return salario;
}