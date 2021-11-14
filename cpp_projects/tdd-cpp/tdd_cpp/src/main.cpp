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
	{	//evitar ao m�ximo usar move constructor: apenas para casos de gerenciamento de recurso (usuando junto com o new)
		std::cout << "String movida" << std::endl;
		size = outraString.size;
		data = outraString.data;
		data[size] = 0; //caracter terminador
		//preciso deixar de quem eu peguei os dados, em um estado inicial, ou inv�lido. resumindo, eu movi para outro lugar, logo o lugar inicial n�o deve existir mais
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
	//Small String Optimization - SSO: se uma string � sufuciente para caber na stack, n�o teremos aloca��o de mem�ria na Heap. Depende da plataforma, arquitetura, compilador etc
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
	//3. a) mandamento n�mero 1 dos novo evang�lio c++: Nunca utilizar new e delete em v�o
	std::cout << "Heresia!!!. forma antiga:" << std::endl;
	Usuario* usuario = new Usuario("Anderson Tregancini");
	std::cout << usuario->recuperaNome() << std::endl << std::endl;
	delete usuario;

	std::cout << "Forma nova:" << std::endl;
	//SMART POINTER: impedir vazamento de mem�ria
	//std::unique_ptr<Usuario> usuario2(new Usuario("Anderson Tregancini"));
	std::cout << "make_unique:" << std::endl;
	std::unique_ptr<Usuario> usuario2 = std::make_unique<Usuario>(Usuario("Anderson Tregancini")); //make_unique vai garantir que tudo ocorreu bem na cria��o, que este ponteiro � um ponteiro v�lido. caso n�o for v�lido, a execu��o n�o vai continuar
	std::cout << usuario2->recuperaNome() << std::endl;
	//3. b)o unique_ptr garante que temos apenas um ponteiro, uma unica referencia para este espa�o de memoria, n�o sendo poss�vel copiar, nem passar por par�metro, e que a mem�ria ser� liberada imediatamente quando sair do escopo
	//na cria��o de um ponteiro, ou ponteiro unico, sempre utilizar o make_unique. ele garente que n�o vamos ter porblema caso ocorra algum exception, ou erro;
	std::cout << "make_shared:" << std::endl;
	std::shared_ptr<Usuario> usuario3 = std::make_shared<Usuario>("Anderson Tregancini"); //make_unique vai garantir que tudo ocorreu bem na cria��o, que este ponteiro � um ponteiro v�lido. caso n�o for v�lido, a execu��o n�o vai continuar
	//3. c)diferente do unque_ptr, shared_ptr � usado criar um ponteiro que vai ser compartilhado, copiado ou passado por par�metro;
	//make_shared pega o par�metro que ela recebe e vai passar para o construtor que est� no tempate. Nunca devemos utilizar o make_share junto com o 'new'
	//make_ptr, s� chama o destrutor quanto todas as refer�ncias da instancia acabarem (sairem de escopo)
	
	ExibeNomeUsuario(usuario3);
	
	std::cout << "Teste 4: L-values-----------------------------" << std::endl << std::endl;
	// um L-value (Left) � tudo que esta antes do sinal de atribui��o ou pode estar antes. Se eu consigo atribuir um endere�o de mem�ria para algo, este algo � um l-value 
	// se eu consigo atribuir um valor para 'algo', este 'algo' � um l-value
	//Nem todo l-value precisa ser uma vari�vel, mas toda vari�vel � um l-value.
	recuperanumero() = 5;
	// diferente do L-value, temos o R-value (Right), que basicamente � algo que eu n�o posso de referenciar, ou n�o tem a um endere�o de memoria
	// podemos ter um L-value a direta da atribui��o, ou seja, nem sempre o que est� a direita da atribui��o � sempre um R-value;
	//ex.: static int = 10; (10 aqui � um R-value, pois eu n�o consigo me referenciar � 10)
	// R-values tamb�m � uma refer�ncia tempor�ria: ex.: leilao.recebeLance(Lance(nome_x, 1000)), Lance(nome_x,1000) � tempor�rio
	//se eu definir o par�metro como 'const' e garantir que nada ser� mudado, eu consego agora passar um r-values (tempor�rios);
	
	//Existem algumas regras quando falamos de gest�o de recursos em C++. Regra de 3, 5 e 0
	//REGRA DOS 3: A regra de 3 diz que se implementamos um destrutor, um copy constructor ou um operador de atribui��o por c�pia, devemos implementar todos os 3.
	//REGRA DOS 5: A regra de 5 diz que se desejamos move semantics em uma classe que possui um destrutor, copy constructor, move constructor, operador de atribui��o por c�pia ou operador de atribui��o que move os dados, devemos implementar os 5.
	//REGRA DOS 0: J� a regra de 0 diz que apenas classes que lidam diretamente com a gest�o de recursos devem implementar estes m�todos. Que via de regra n�s n�o devemos precisar de nenhum deles.
	Userr(MyString("Anderson"));

	return 0;
}


