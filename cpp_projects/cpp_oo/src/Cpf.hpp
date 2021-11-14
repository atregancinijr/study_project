#pragma once
#include<string>

class Cpf{

    public:explicit Cpf(std::string cpf); //explicit -> n�o permite convers�o impl�cita

    private:std::string cpf;

    public:std::string retorna_cpf();
    private:void verifica_validade_cpf();
    
};