#include<iostream>
#include<string>
#include "Titular.hpp"

Titular::Titular(Cpf cpf, std::string nome, std::string senha):
PessoaFisica(cpf, nome),Autenticavel(senha) //herança
{   
}
