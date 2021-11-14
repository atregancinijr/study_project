#include "Cpf.hpp"
#include <iostream>

Cpf::Cpf(std::string cpf):
cpf(cpf){
    verifica_validade_cpf();
}

void Cpf::verifica_validade_cpf(){
    if(cpf.size()< 11){
        std::cout << "CPF inválido!" << std::endl;
        exit(1);
    }
}

std::string Cpf::retorna_cpf()
{
    return cpf;
}