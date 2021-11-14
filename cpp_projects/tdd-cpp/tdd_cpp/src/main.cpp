#include <iostream>
#include <string>
#include<memory>
#include <string_view>
#include "Usuario.hpp"
//curso Alura Perforance
//void* operator new(size_t bytes)
//{
//	std::cout << "Alocando " << bytes << " bytes" << std::endl;
//	return malloc(bytes);
//}
void ExibeNomeUsuario(std::shared_ptr<Usuario> usuario)
{
	std::cout << usuario->recuperaNome() << std::endl;
}

int& recuperanumero()
{
	static int valor = 10;
	return valor;
}

class MyString
{
	private:char* data;
		   size_t size;
	public:MyString(const char* string)
	{
		std::cout << "String criada" << std::endl;
		size = strlen(string);
		data = new char[size];
		memcpy(data, string, size);
	}

	public:~MyString()
	{
		delete data;
	}
	
	public:MyString(const MyString& outraString)
	{
		std::cout << "String copiada" << std::endl;
		//um recurso a mais;
		size = strlen(outraString.data);
		data = new char[size];
		memcpy(data, outraString.data, size);
	}
	public:MyString(MyString&& outraString)//move contructor
	{	//evitar ao máximo usar move constructor: apenas para casos de gerenciamento de recurso (usuando junto com o new)
		std::cout << "String movida" << std::endl;
		size = outraString.size;
		data = outraString.data;
		data[size] = 0; //caracter terminador
		//preciso deixar de quem eu peguei os dados, em um estado inicial, ou inválido. resumindo, eu movi para outro lugar, logo o lugar inicial não deve existir mais
		outraString.size = 0;
		data = outraString.data = nullptr;

	}


};

class Userr
{
private: MyString nome;

public:Userr(const MyString& string) : nome(string)
{

}

public:Userr(MyString&& string) : nome(std::move(string)) // ou ainda : nome((MyString&&) string)
{
	 
}
};


int main() {
	std::cout << "Teste 1-----------------------------" << std::endl;

	std::cout << "1.a) const char*:" << std::endl;
	const char* meu_nome_completo = "Anderson Jr";
	std::cout << meu_nome_completo << std::endl<< std::endl;

	std::cout << "1.b) string:" << std::endl;
	//Small String Optimization - SSO: se uma string é sufuciente para caber na stack, não teremos alocação de memória na Heap. Depende da plataforma, arquitetura, compilador etc
	std::string meu_nome_completo2 = "Anderson Jr";
	std::cout << meu_nome_completo2 << std::endl << std::endl;
	std::cout << "Teste 2-----------------------------" << std::endl << std::endl;
	std::string casal = "Anderson & Jessica";
	std::cout << "2.a) Exibir, visualizar parte da string, declaracao normal:" << std::endl;
	std::string meu_nome = casal.substr(0, casal.find('&')-1);
	std::string nome_dela = casal.substr(casal.find('&') + 2);
	std::cout << meu_nome << std::endl;
	std::cout << nome_dela << std::endl;
	std::cout << "2.b) Utilizando 'string_view'. nao aloca mais memoria na heap:" << std::endl;
	std::string_view meu_nome2(casal.c_str(), casal.find('&') - 1);
	std::string_view nome_dela2(casal.c_str() + casal.find('&') + 2);
	std::cout << meu_nome2 << std::endl;
	std::cout << nome_dela2 << std::endl;

	std::cout << "Teste 3: Alocando na Heap-----------------------------" << std::endl << std::endl;
	//3. a) mandamento número 1 dos novo evangélio c++: Nunca utilizar new e delete em vão
	std::cout << "Heresia!!!. forma antiga:" << std::endl;
	Usuario* usuario = new Usuario("Anderson Tregancini");
	std::cout << usuario->recuperaNome() << std::endl << std::endl;
	delete usuario;

	std::cout << "Forma nova:" << std::endl;
	//SMART POINTER: impedir vazamento de memória
	//std::unique_ptr<Usuario> usuario2(new Usuario("Anderson Tregancini"));
	std::cout << "make_unique:" << std::endl;
	std::unique_ptr<Usuario> usuario2 = std::make_unique<Usuario>(Usuario("Anderson Tregancini")); //make_unique vai garantir que tudo ocorreu bem na criação, que este ponteiro é um ponteiro válido. caso não for válido, a execução não vai continuar
	std::cout << usuario2->recuperaNome() << std::endl;
	//3. b)o unique_ptr garante que temos apenas um ponteiro, uma unica referencia para este espaço de memoria, não sendo possível copiar, nem passar por parâmetro, e que a memória será liberada imediatamente quando sair do escopo
	//na criação de um ponteiro, ou ponteiro unico, sempre utilizar o make_unique. ele garente que não vamos ter porblema caso ocorra algum exception, ou erro;
	std::cout << "make_shared:" << std::endl;
	std::shared_ptr<Usuario> usuario3 = std::make_shared<Usuario>("Anderson Tregancini"); //make_unique vai garantir que tudo ocorreu bem na criação, que este ponteiro é um ponteiro válido. caso não for válido, a execução não vai continuar
	//3. c)diferente do unque_ptr, shared_ptr é usado criar um ponteiro que vai ser compartilhado, copiado ou passado por parâmetro;
	//make_shared pega o parâmetro que ela recebe e vai passar para o construtor que está no tempate. Nunca devemos utilizar o make_share junto com o 'new'
	//make_ptr, só chama o destrutor quanto todas as referências da instancia acabarem (sairem de escopo)
	
	ExibeNomeUsuario(usuario3);
	
	std::cout << "Teste 4: L-values-----------------------------" << std::endl << std::endl;
	// um L-value (Left) é tudo que esta antes do sinal de atribuição ou pode estar antes. Se eu consigo atribuir um endereço de memória para algo, este algo é um l-value 
	// se eu consigo atribuir um valor para 'algo', este 'algo' é um l-value
	//Nem todo l-value precisa ser uma variável, mas toda variável é um l-value.
	recuperanumero() = 5;
	// diferente do L-value, temos o R-value (Right), que basicamente é algo que eu não posso de referenciar, ou não tem a um endereço de memoria
	// podemos ter um L-value a direta da atribuição, ou seja, nem sempre o que está a direita da atribuição é sempre um R-value;
	//ex.: static int = 10; (10 aqui é um R-value, pois eu não consigo me referenciar à 10)
	// R-values também é uma referência temporária: ex.: leilao.recebeLance(Lance(nome_x, 1000)), Lance(nome_x,1000) é temporário
	//se eu definir o parâmetro como 'const' e garantir que nada será mudado, eu consego agora passar um r-values (temporários);
	
	//Existem algumas regras quando falamos de gestão de recursos em C++. Regra de 3, 5 e 0
	//REGRA DOS 3: A regra de 3 diz que se implementamos um destrutor, um copy constructor ou um operador de atribuição por cópia, devemos implementar todos os 3.
	//REGRA DOS 5: A regra de 5 diz que se desejamos move semantics em uma classe que possui um destrutor, copy constructor, move constructor, operador de atribuição por cópia ou operador de atribuição que move os dados, devemos implementar os 5.
	//REGRA DOS 0: Já a regra de 0 diz que apenas classes que lidam diretamente com a gestão de recursos devem implementar estes métodos. Que via de regra nós não devemos precisar de nenhum deles.
	Userr(MyString("Anderson"));

	return 0;
}


