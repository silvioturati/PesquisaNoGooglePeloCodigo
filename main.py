from googlesearch import search

palavra_pesquisa = input("Insira o termo que deseja pesquisar: ")

lista_urls = search(palavra_pesquisa, tld="com.br", lang="pt", num=5, stop=10, pause=2)

for url in lista_urls:
    print(url)
