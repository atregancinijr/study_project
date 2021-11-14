#include "catch.hpp"
#include "../src/Avaliador.hpp"
#include <iostream>
#include <string>

Leilao emOrdemCrescente() {
    Lance primeiroLance(Usuario("Vinicius Dias"), 1000);
    Lance segundoLance(Usuario("Ana Maria"), 2000);
    Leilao leilao("Fiat 147 0Km");
    leilao.recebeLance(primeiroLance);
    leilao.recebeLance(segundoLance);
    return leilao;
}

Leilao emOrdemDecrescente() {
    Lance primeiroLance(Usuario("Vinicius Dias"), 2000);
    Lance segundoLance(Usuario("Ana Maria"), 1000);
    Leilao leilao("Fiat 147 0Km");
    leilao.recebeLance(primeiroLance);
    leilao.recebeLance(segundoLance);
    return leilao;
}

TEST_CASE("Testes Avaliador")
{
    Avaliador leiloeiro;
    SECTION("Leiloes ordenados")
    {
        SECTION("Deve recuperar maior lance de leilão") {
            // Arrange - Given
            Leilao leilao = GENERATE(emOrdemCrescente(), emOrdemDecrescente());

            // Act - When
            leiloeiro.avalia(leilao);

            // Assert - Then
            REQUIRE(2000 == leiloeiro.recuperaMaiorValor());
        }

        SECTION("Deve recuperar menor lance de leilão") {
            // Arrange - Given
            Leilao leilao = GENERATE(emOrdemCrescente(), emOrdemDecrescente());

            // Act - When
            leiloeiro.avalia(leilao);

            // Assert - Then
            REQUIRE(1000 == leiloeiro.recuperaMenorValor());
        }

    }

    SECTION("Deve recuperar os 3 maiores lances")
    {
        // Arrange - Given
        Lance primeiroLance(Usuario("Vinicius Vacalvante"), 1000.0);

        Lance terceiroLance(Usuario("Pedro Puto"), 1500.0);
        Lance quartoLance(Usuario("Rozilda Rose"), 2500.0);
        Leilao leilao("Fiat 147 0Km");
        leilao.recebeLance(primeiroLance);
        leilao.recebeLance(Lance(Usuario("Ana Amanda"), 2000.0)); //R-values
        leilao.recebeLance(terceiroLance);
        leilao.recebeLance(quartoLance);

        // Act - When
        leiloeiro.avalia(leilao);

        // Assert - Then
        std::vector<Lance> maiores3Lances = leiloeiro.recupera3MaioresLances();
        REQUIRE(3 == maiores3Lances.size());
        REQUIRE(2500 == maiores3Lances[0].recuperaValor());
        REQUIRE(2000 == maiores3Lances[1].recuperaValor());
        REQUIRE(1500 == maiores3Lances[2].recuperaValor());
    }
}
