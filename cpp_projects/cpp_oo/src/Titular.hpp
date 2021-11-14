#pragma once
//#include<iostream>
#include<string>
#include "PessoaFisica.hpp"
#include "Autenticavel.hpp"
#include "Cpf.hpp"

class Titular:public PessoaFisica, public Autenticavel{
    public:Titular(Cpf cpf, std::string nome, std::string senha);
};