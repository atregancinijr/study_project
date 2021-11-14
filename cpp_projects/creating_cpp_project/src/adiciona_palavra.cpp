#include<iostream>
#include<string>
#include<vector>

#include "le_arquivo.hpp"
#include "salvar_arquivo.hpp"

#include "adiciona_palavra.hpp"

std::string capitalize_string(std::string s){
    std::string res_str;
    for(char c : s){
        
        res_str.push_back(toupper(c));       
    }
 
    return res_str;
}

void adiciona_palavra(){
    std::string nova_palavra;
    std::cout << "Digite a nova palavra: " << std::endl;
    std::cin >> nova_palavra;

    std::vector<std::string> lista_palavras = le_arquivo();
    lista_palavras.push_back(capitalize_string(nova_palavra));

    salvar_arquivo(lista_palavras);
}

