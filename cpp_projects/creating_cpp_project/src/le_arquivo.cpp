
#include<iostream>
#include<fstream>
#include "le_arquivo.hpp"

std::vector<std::string> le_arquivo(){

    std::ifstream arquivo;
    std::string palavra_lida;
    std::vector<std::string> palavras_do_arquivo;
    int quantidade_palavras;

    arquivo.open("palavras.txt");
    if(arquivo.is_open()){
        arquivo >> quantidade_palavras;
        
        for(int i=0; i<quantidade_palavras;i++){
            arquivo >> palavra_lida;
            palavras_do_arquivo.push_back(palavra_lida);
        }
        arquivo.close();
        return palavras_do_arquivo;
    }
    else{
        std::cout << "Nao foi possivel acessar o banco de palavras." << std::endl;
        system("pause");
        exit(0);
    }
}