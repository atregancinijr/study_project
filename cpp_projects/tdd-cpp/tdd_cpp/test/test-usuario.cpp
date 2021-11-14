#include "catch.hpp"
#include "../src/Usuario.hpp"
#include <string>

TEST_CASE("Usuario deve saber informar seu primeiro nome") {
	Usuario anderson("Anderson Tregancini Junior");

	std::string primeiro_nome = anderson.recuperaPrimeiroNome();

	REQUIRE("Anderson == primeiro_nome");
}