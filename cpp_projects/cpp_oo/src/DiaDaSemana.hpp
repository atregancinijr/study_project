#pragma once

enum class DiaDaSemana:unsigned short int
{
    Domingo, Segunda, Terca, Quarta, Quinta, Sexta, Sabado
};

//enum -> facilmente conversível
//enum class -> não define as variáveis fora do escopo travado, tenho que manter o namespace na frente do elemento, 
//por exemplo DiaDaSemana::Terca