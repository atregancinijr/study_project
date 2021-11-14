#include "Conta.hpp"
#include <iostream>


int Conta::numero_de_contas = 0;

Conta::Conta(std::string numero_conta, Titular titular):
numero_conta(numero_conta),titular(titular),saldo(0)
{
    numero_de_contas++;
}

/* posso definir um construtor desta forma tbm. É um pouco menos eficiente que o outro:
    Conta::Conta(std::string numero_conta, std::string nome_titular, std::string cpf_titular)
{
    this->numero_conta = numero_conta;
    this->nome_titular = nome_titular;
    this->cpf_titular = cpf_titular;
    this->saldo = 0;
}
*/

Conta::~Conta(){//destrutor não tem argumentos
    numero_de_contas--;
}

std::variant<Conta::Resultado_Saque, float> Conta::sacar(float valorASacar)
{
    float tarifa_de_saque  = valorASacar * retorna_taxa_de_saque();
    
    if (valorASacar < 0) {
            std::cout << "Não pode sacar valor negativo" << std::endl;
            return ValorNegativo;
        }
        
        if (valorASacar > saldo) {
            std::cout << "Saldo insuficiente" << std::endl;
            return SaldoInsuficiente;
        }
        
        saldo -= (valorASacar + tarifa_de_saque);
        return saldo;
}

void Conta::depositar(float valorADepositar)
{
        if (valorADepositar < 0) {
            std::cout << "Não pode sacar valor negativo" << std::endl;
            return;
        }

        saldo += valorADepositar;
}
void Conta::operator+=(float valorADepositar){
        depositar(valorADepositar);
}

float Conta::recupera_saldo()
{
    return saldo;
}

int Conta::recupera_numero_de_contas()
{
    return numero_de_contas;
}

std::string Conta::recupera_numero_da_conta()
{
    return numero_conta;
}

bool Conta::operator<(const Conta& outra)
{
    return this->saldo < outra.saldo;
}