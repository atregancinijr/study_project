#pragma once
#include<string>

class Autenticavel
{
    private:std::string senha;

    public:Autenticavel(std::string senha);
    public:bool autentica(std::string senha) const;
};