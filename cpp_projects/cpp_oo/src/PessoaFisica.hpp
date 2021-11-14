#pragma once
#include "Cpf.hpp"

class PessoaFisica
{
    private:Cpf cpf;
    protected:std::string nome; //protected -> somentes as classes que herdam de PessoaFisica poderam acessar essa variável

    public:PessoaFisica(Cpf cpf, std::string nome);
    private:void verifica_tamanho_do_nome(); 
    public:std::string nome_pessoa() const;
};