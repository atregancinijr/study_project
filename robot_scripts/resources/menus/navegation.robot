*** Settings ***
Library     SeleniumLibrary

*** Variables ***
#Global
${DEFAULT_BROWSER}        chrome
${URL_DEFAULT}    about:blank
${SEARCH_URL}     http://www.google.com.br
${it_default_search_box}    //input[@type="text" or @type="search"]
*** Keywords ***
Abre o browser
    [Arguments]     ${url}=${URL_DEFAULT}   ${browser}=${DEFAULT_BROWSER}
    ${chrome_options}=     Evaluate    sys.modules['selenium.webdriver'].ChromeOptions()    sys, selenium.webdriver
    #Call Method    ${chrome_options}   add_argument    no-sandbox
    Call Method    ${chrome_options}   add_argument    ignore-ssl-errors
    ${options}=     Call Method     ${chrome_options}    to_capabilities

    SeleniumLibrary.Open Browser  ${url}   browser=chrome  desired_capabilities=${options}
    Maximize Browser Window

Fecha o browser
    Close Browser

Navegue até a página de pesquisa
    [Arguments]     ${url}=${SEARCH_URL}
    Go To    ${url}

Busque pela palavra
    [Arguments]   ${alguma_coisa}
    Wait Until Element Is Visible    ${it_default_search_box}
    Input Text     ${it_default_search_box}    ${alguma_coisa}
    Press Keys     ${it_default_search_box}    ENTER
