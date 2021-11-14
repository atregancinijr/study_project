#include<iostream>
#include<cstdlib>
#include<ctime>
using namespace std;

int main(){
    cout << "************************************" << endl;
    cout << "* BEM VINDO AO JOGO DA ADIVINHACAO *" << endl;
    cout << "************************************" << endl;
    cout << "Escolha o nivel de dificuldade:" << endl;
    cout << "Facil (F), Medio (M) ou Dificil (D)" << endl;

    srand(time(NULL)); //seed

    const int NUMERO_SECRETO = rand() % 100; //Constantes são read-only
    int MAX_CHANCES;
    int chances;
    int chute;
    
    bool aux = false;
    bool acertou;
    bool errou_para_mais;
    bool nao_escolheu_dificuldade_correta = true;

    double pontos = 1000.0;
    double pontos_perdidos;

    char dificuldade;
    
    while (nao_escolheu_dificuldade_correta)
    {
        cin >>  dificuldade;  

        if(dificuldade == 'F'){
            MAX_CHANCES = 10;
            nao_escolheu_dificuldade_correta = false;
        }
        else if(dificuldade == 'M'){
            MAX_CHANCES = 5;
            nao_escolheu_dificuldade_correta = false;
        }
        else if(dificuldade == 'D'){
            MAX_CHANCES = 3;
            nao_escolheu_dificuldade_correta = false;
        }
        else{
            cout << "Opcao invalida!" << endl;
        }
    }
    cout << "Voce escolheu: " << dificuldade << endl;

    for(chances = 0; chances < MAX_CHANCES; chances++)
    {
        cout << "Entre com um chute... Voce tem "<< MAX_CHANCES - chances <<" tentativas restantes" << endl;
        cin >> chute;
        cout << "Seu chute foi de: " << chute << endl;

        pontos_perdidos = abs(chute - NUMERO_SECRETO)/2.0;
        pontos -= pontos_perdidos;
        acertou = chute == NUMERO_SECRETO;

        errou_para_mais = chute > NUMERO_SECRETO;

        if(acertou){
            cout << "Parabens! Voce acertou o numero secreto!" << endl;
            cout.precision(2); //quantas casas depois da vírgula eu quero, retorna notação científica
            cout << fixed; // uso fixed para tirar da notação científica, mantendo a formatação de duas casas depois da vírgula
            cout << "Sua pontuacao final foi de " << pontos << endl;
            aux = true;
            break;
        }
        else if(errou_para_mais){
            cout << "Ops...Seu chute foi maior que o numero secreto" << endl;
        }
        else{
            cout << "Eita! Seu chute foi menor que o numero secreto" << endl;
        }
    }
    
    if(aux == false){
        cout << endl;
        cout << "Voce falhou... o numero secreto era "<< NUMERO_SECRETO << endl << endl;
    }
    
    system("pause");
}