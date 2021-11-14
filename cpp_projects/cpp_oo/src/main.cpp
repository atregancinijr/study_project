#include <iostream>
#include <string>
#include "ContaPoupanca.hpp"
#include "ContaCorrente.hpp"
#include "Gerente.hpp"
#include "Titular.hpp"
#include "Cpf.hpp"
#include "DiaDaSemana.hpp"
//#include <optional>   --> alue that may or may not be present
//#include <any>  --> An object of class any stores an instance of any type that satisfies the constructor requirements or is empty
using namespace std;

void efetuar_um_saque_de_duzentos_reais(Conta& conta)
{
    std::variant<Conta::Resultado_Saque, float> resultado = conta.sacar(200);  
    if(auto saldo = std::get_if<float>(&resultado)){
        cout <<"Novo saldo da conta: "<< *saldo << endl;
    }  
}
void faz_login(Autenticavel& alguem, string senha)
{
    if(alguem.autentica(senha))
    {
        cout << "Login realizado com sucesso" << endl;
    }
    else
    {
        cout << "Senha inválida" << endl;
    }
}

ostream& operator<<(ostream& cout, Conta& conta)
{
    PessoaFisica titular = conta.titular; // titular é privado, como acessar? 
    //Resposta: devo declarar na definição da classe Conta este método e seus parâmetros com o modificador "friend"
    cout << "Teste method overload titular da conta: " << titular.nome_pessoa() << endl;
    cout << "Teste method overload saldo da conta: " << conta.recupera_saldo() << endl;
    
    return cout;
}
template<typename T>  //definicao .hpp -> template <typename NomeDoTipo> retorno nomeFuncao(NomeDoTipo parametros)
T Menor(T a, T b)
{
    return a < b ? a : b;
}

int main()
{
    //char* um_cpf = "123.456.789-01";
    //Cpf* meu_ponteiro = new Cpf(um_cpf);//alocando na Heap
    //cout << meu_ponteiro->retorna_cpf() << endl;

    Titular um_titular(Cpf("123.456.789-01"), "Anderson", "senhaX");
    Titular outro_titular(Cpf("098.765.432-10"), "Jessica", "senhaY");
    ContaCorrente umaConta("123-4", um_titular);
    ContaCorrente umaOutraConta("123-8", outro_titular);
    ContaCorrente umaNovaConta("567-9",  Titular(Cpf("456.789.123-59"), "Mae", "senhaZ"));
    umaConta.depositar(500);
    umaOutraConta.depositar(500);
    (Conta&) umaNovaConta+=1000; //sobrecarregar um operador: faz o mesmo que o depositar. Realizar operacoes em objetos
    efetuar_um_saque_de_duzentos_reais(umaConta);
    efetuar_um_saque_de_duzentos_reais(umaOutraConta);
    umaOutraConta.transfere_para(umaConta, 100);
    umaNovaConta.transfere_para(umaOutraConta, 200);
    //umaConta.recupera_saldo();
    //umaOutraConta.recupera_saldo();
    umaConta += umaOutraConta;
    //umaConta.recupera_saldo();
    //umaOutraConta.recupera_saldo();
    cout << "Numero de contas criadas: "<< Conta::recupera_numero_de_contas() << endl;
    Gerente umGerente(Cpf("000.000.000-00"), "Gerente", 10000, DiaDaSemana::Terca, "123123");
    
    cout << umaOutraConta;
    cout << Menor<Conta&>(umaConta, umaOutraConta) << endl;
    cout << Menor(1, 2) << endl;
    system("pause");
}