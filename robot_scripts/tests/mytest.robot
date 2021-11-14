*** Settings ***
Resource  ../resources/menus/navegation.robot

Documentation     Este exemplo abre um página de pesquisa e faz uma pesquisa qualquer

Test Setup       Abre o browser
#Test Teardown    Fecha o browser

*** Variables ***
#
*** Tasks ***
Faça uma busca por uma palavra
    Navegue até a página de pesquisa
    Busque pela palavra
