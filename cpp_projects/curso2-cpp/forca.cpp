#include<iostream>
#include<string>
#include<map>
#include<vector>
#include<fstream>
#include<ctime>
#include<cstdlib>
#include "nao_enforcou.hpp"
#include "nao_acertou.hpp"
#include "letra_existe.hpp"
#include "le_arquivo.hpp"
#include "imprime_palavra.hpp"
#include "imprime_erros.hpp"
#include "imprime_cabecalho.hpp"
#include "chuta.hpp"
#include "adiciona_palavra.hpp"
#include "sorteia_palavra.hpp"

using namespace std;

const int NUMERO_DE_TENTATIVAS = 5;
string palavra_secreta;
map<char, bool> chutou;
vector<char> chutes_errados;

int main(){
    char resposta;
    imprime_cabecalho();
    le_arquivo();
    sorteia_palavra();
    while (nao_acertou() && nao_enforcou())
    {
        imprime_erros();
        imprime_palavra();
        chuta();
    }
    cout << "Fim de jogo" << endl << endl;
    cout << "A palavra secreta era: " << palavra_secreta << endl;

    if(nao_acertou()){
        cout << "Voce perdeu! Tente novamente..." <<endl;
    }
    else{
        cout << "Parabens voce venceu!!!" << endl;
        cout << "Voce deseja colocar uma nova palavra secreta ao branco? (S/N)" << endl;
        cin >> resposta;
        resposta = toupper(resposta);
        if(resposta == 'S'){
            adiciona_palavra();
        }
    }

}