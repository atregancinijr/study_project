#include "catch.hpp"
#include "../src/Avaliador.hpp"

TEST_CASE("Nao pode receber dois testes consecutivos de uma mesma pessoa") {
    // Arrange - Given
    Avaliador leiloeiro;
    Leilao leilao("Fiat 147 0Km");
    std::string anderson = "Anderson Jr";

    Lance primeiroLance(Usuario(anderson), 1000.0);
    Lance segundoLance(Usuario(anderson), 2000.0);
    leilao.recebeLance(primeiroLance);
    leilao.recebeLance(segundoLance);
    // Act - When
    leiloeiro.avalia(leilao);
    // Assert - Then
    REQUIRE(1 == leilao.recuperaLances().size());
}