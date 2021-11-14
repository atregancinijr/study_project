#include<iostream>
#include<map>
#include<vector>
#include "letra_existe.hpp"
#include "chuta.hpp"

extern std::map<char, bool> chutou;
extern std::vector<char> chutes_errados;

void chuta(){
    char chute;
    std::cout << "Chute um caracter:" << std::endl;
    std::cin >> chute;
    chute = toupper(chute);
    chutou[chute] = true;
    std::cout << "O seu chute foi: " << chute << std::endl;

    if(letra_existe(chute))
        {
            std::cout << "Voce acertou! Seu chute esta na palavra secreta" << std::endl;
        }
        else{
            std::cout << "Voce errou... Seu chute nao esta na palavra secreta" << std::endl;
            chutes_errados.push_back(chute);
        }
        std::cout << std::endl;
}