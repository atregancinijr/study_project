*** Settings ***
Library     RequestsLibrary
Library     String
Library    OperatingSystem

Documentation     Esta Task faz o download de um arquivo e joga em outra pasta

*** Variables ***
${url}    https://www.mtggoldfish.com/archetype/commander-asmoranomardicadaistinaculdacar#paper
${commander_name}   Prosper, Tome-Bound

*** Test Cases ***
Download from MTGGoldfish
  Create Session    mtggoldfish_connection    http://www.mtggoldfish.com
  ${response}=   Get On Session  alias=mtggoldfish_connection   url=https://www.mtggoldfish.com/archetype/commander-prosper-tome-bound
  #Log To Console    ${response.content}
  ${res1}=    Convert To String    ${response.content}
  ${res}=   Split String    ${res1}     href="/deck/download/
  ${result}=    Split String        ${res}[1]       "
  Log To Console    ${result}[0]
  ${uri}            Set Variable    /deck/download/${result}[0]

  ${response2}=          Get On Session    mtggoldfish_connection    ${uri}
  Should Be Equal As Numbers     ${response2.status_code}    200
  ${x}=   Set Variable       ${response2.content}
  Log To Console    ${x}
  ${x}=   Convert To String    ${x}
  ${y}=   Replace String Using Regexp   ${x}    1 ${commander_name}   ${EMPTY}
  ${file}=    Catenate   Commander\n1 ${commander_name}\nMain\n   ${y}
  #Log To Console    ${file}
  Create Binary File    C:\\Users\\Pichau\\AppData\\Roaming\\Forge\\decks\\${commander_name}.dck    ${file}
