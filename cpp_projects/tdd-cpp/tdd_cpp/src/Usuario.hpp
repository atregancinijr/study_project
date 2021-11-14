#pragma once
#include <string>

class Usuario
{
private:
    std::string nome;
public:
    Usuario(std::string);
    std::string recuperaNome() const;
    std::string recuperaPrimeiroNome() const;
};