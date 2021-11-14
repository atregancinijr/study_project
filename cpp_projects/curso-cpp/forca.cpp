#include<iostream>
#include<string>
#include<map>
#include<vector>
#include<fstream>
#include<ctime>
#include<cstdlib>
using namespace std;

string palavra_secreta;
const int NUMERO_DE_TENTATIVAS = 5;
map<char, bool> chutou;
vector<char> chutes_errados;

void imprime_cabecalho(){
    cout << "************************************" << endl;
    cout << "*    BEM VINDO AO JOGO DA FORCA    *" << endl;
    cout << "************************************" << endl;   
}

bool letra_existe(char chute){
    //for(int i=0; i<palavra_secreta.size(); i++){
    //    if(chute == palavra_secreta[i]){
    //        return true;
    //    }
    //}
    for(char letra : palavra_secreta){  // a partir do C++11
        if(chute == letra){
            return true;
        }
    }
    return false;       
}

void imprime_palavra(){
    for(char letra : palavra_secreta){
            if(chutou[letra]){
                cout << letra << " ";
            }
            else{
                cout << "_ ";
            }
        }     
    cout << endl << endl;
}

void imprime_lista_de_chutes_errados(){
    cout << "Chutes errados: ";
    for(char letra : chutes_errados){
        cout << letra << " ";
    }
    cout << endl;
}

void chuta(){
    char chute;
    cout << "Chute um caracter:" << endl;
    cin >> chute;
    chute = toupper(chute);
    chutou[chute] = true;
    cout << "O seu chute foi: " << chute << endl;

    if(letra_existe(chute))
        {
            cout << "Voce acertou! Seu chute esta na palavra secreta" << endl;
        }
        else{
            cout << "Voce errou... Seu chute nao esta na palavra secreta" << endl;
            chutes_errados.push_back(chute);
        }
        cout << endl;
}

vector<string> le_arquivo(){

    ifstream arquivo;
    string palavra_lida;
    vector<string> palavras_do_arquivo;
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
        cout << "Nao foi possivel acessar o banco de palavras." << endl;
        system("pause");
        exit(0);
    }
}

void sorteia_palavra(){
    vector<string> palavras = le_arquivo();
    srand(time(NULL));
    int indice_sorteado = rand() % palavras.size();
    palavra_secreta = palavras[indice_sorteado];
}

bool nao_acertou(){
    for(char letra : palavra_secreta){
        if(!chutou[letra]){
            
            return true;
        }
    }
    return false;
}

bool nao_enforcou(){
    return chutes_errados.size() < NUMERO_DE_TENTATIVAS;
}

string capitalize_string(string s){
    string res_str;
    for(char c : s){
        
        res_str.push_back(toupper(c));       
    }
 
    return res_str;
}

void salvar_arquivo(vector<string> nova_lista){
    ofstream arquivo;
    arquivo.open("palavras.txt");
     if(arquivo.is_open()){
       arquivo << nova_lista.size() << endl;

       for(string palavra : nova_lista){
           arquivo << palavra << endl;
       }
       arquivo.close();
    }
    else{
        cout << "Nao foi possivel acessar o banco de palavras." << endl;
        system("pause");
        exit(0);
    }
}

void adiciona_palavra(){
    string nova_palavra;
    cout << "Digite a nova palavra: " << endl;
    cin >> nova_palavra;

    vector<string> lista_palavras = le_arquivo();
    lista_palavras.push_back(capitalize_string(nova_palavra));

    salvar_arquivo(lista_palavras);
}

int main(){
    char resposta;
    imprime_cabecalho();
    le_arquivo();
    sorteia_palavra();
    while (nao_acertou() && nao_enforcou())
    {
        imprime_lista_de_chutes_errados();
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
    
    system("pause");
}