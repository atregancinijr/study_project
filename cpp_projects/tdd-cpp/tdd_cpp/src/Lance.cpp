#include "Lance.hpp"
#include <iostream>
Lance::Lance(Usuario usuario, float valor) : usuario(usuario), valor(valor)
{
}

float Lance::recuperaValor() const
{
    return valor;
}

Usuario Lance::recuperaUsuario() const
{
    return usuario;
}


//C++ já faz isso por padrão:
//Lance::Lance(const Lance& outro_lance):
//usuario(outro_lance.usuario), valor(outro_lance.valor) //copy constructor
//{
//   std::cout << "Executando copia de lance de valor: " << valor << std::endl;
//}