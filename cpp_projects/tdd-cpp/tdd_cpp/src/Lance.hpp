#pragma once
#include "Usuario.hpp"

class Lance
{
private:
    Usuario usuario;
    float valor;
public:
    Lance(Usuario usuario, float valor);
    float recuperaValor() const;
    Usuario recuperaUsuario() const;
    //Lance(const Lance& outro_lance); 
    //usa-se copy constructor em cenários de gerenciamento de ponteiros, stream de arquivos, reescrita de libs. Via de regra, confie no que o c++ já tras.
    //pare empedir o copy constructor --> Lance(const Lance&) = delete;
};