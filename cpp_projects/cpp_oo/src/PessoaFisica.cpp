#include "PessoaFisica.hpp"
#include <iostream>

PessoaFisica::PessoaFisica(Cpf cpf, std::string nome):
cpf(cpf), nome(nome)
{   
    verifica_tamanho_do_nome();      
}

void PessoaFisica::verifica_tamanho_do_nome()
{
    if(nome.size()<3){
        std::cout << "Nome muito curto" << std::endl;
        exit(1);
    }
}

std::string PessoaFisica::nome_pessoa() const
{
    return nome;
}