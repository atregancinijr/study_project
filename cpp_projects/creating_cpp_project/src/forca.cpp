#include<iostream>
#include<string>
#include<map>
#include<vector>
#include "nao_enforcou.hpp"
#include "nao_acertou.hpp"
#include "le_arquivo.hpp"
#include "imprime_palavra.hpp"
#include "imprime_erros.hpp"
#include "imprime_cabecalho.hpp"
#include "chuta.hpp"
#include "adiciona_palavra.hpp"
#include "sorteia_palavra.hpp"

using namespace std;

int main(){
    const unsigned int NUMERO_DE_TENTATIVAS = 5;
    string palavra_secreta;
    map<char, bool> chutou;
    vector<char> chutes_errados;

    imprime_cabecalho();
    char resposta;
    palavra_secreta = sorteia_palavra();
    while (nao_acertou(palavra_secreta, chutou) && nao_enforcou(chutes_errados, NUMERO_DE_TENTATIVAS))
    {
        Forca::imprime_erros(chutes_errados);
        imprime_palavra(palavra_secreta, chutou);
        chuta(chutou, chutes_errados, palavra_secreta);
    }
    cout << "Fim de jogo" << endl << endl;
    cout << "A palavra secreta era: " << palavra_secreta << endl;

    if(nao_acertou(palavra_secreta, chutou)){
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
    system("pause");
}