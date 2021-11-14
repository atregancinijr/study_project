arquivo = open('dados/contatos-escrita.csv', encoding='latin_1', mode='a+')

print(type(arquivo.buffer))



texto_em_byte = bytes('Esse é um texto em bytes.', 'latin_1')

#print(texto_em_byte, type(texto_em_byte))

contato = bytes('15,Verônica,veronica@veronica.com.br\n', encoding='latin_1')
arquivo.buffer.write(contato)
arquivo.close()
