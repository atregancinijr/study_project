#pragma once

enum class DiaDaSemana:unsigned short int
{
    Domingo, Segunda, Terca, Quarta, Quinta, Sexta, Sabado
};

//enum -> facilmente convers�vel
//enum class -> n�o define as vari�veis fora do escopo travado, tenho que manter o namespace na frente do elemento, 
//por exemplo DiaDaSemana::Terca