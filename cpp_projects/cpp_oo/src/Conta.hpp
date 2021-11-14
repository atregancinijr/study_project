#pragma once
#include <string>
#include <utility>
#include "Titular.hpp"
#include<variant>

class Conta{
public:
    //construtor:
    Conta(std::string numero_conta, Titular titular);
    //destrutor:
    ~Conta();
protected:
    std::string numero_conta;
    Titular titular;
    float saldo = 0;
public:enum Resultado_Saque {ValorNegativo, SaldoInsuficiente};
//std::pair<Resultado_Saque, float> sacar(float valorASacar);
public:std::variant<Resultado_Saque, float> sacar(float valorASacar);
    float recupera_saldo(); //quando for chamado, ele vai olhar para o objeto e definir qual ".sacar" utilizar. Usado para sobreescrita de método.
    void depositar(float valorADepositar);
    void operator+=(float valorADepositar);
    std::string recupera_numero_da_conta();
public:virtual float retorna_taxa_de_saque() const = 0; //este igual a zero diz que o método está incompleto, ou seja, está aguardando implementação nas classes filhas. Em Resumo, isso torna a classe mãe, uma classe abstrata
private:void definir_nome_titular(std::string nome);

private:void verifica_tamanho_do_nome(std::string nome); //exemplo de metodo privado

private:
    static int numero_de_contas;     //exemplo de atributo da classe

public:
    static int recupera_numero_de_contas();     //exemplo de método de classe

friend std::ostream& operator<<(std::ostream& cout, Conta& conta); //friend dará acesso a todos os atributos (privados etc) e métodos
bool operator < (const Conta &conta);

};