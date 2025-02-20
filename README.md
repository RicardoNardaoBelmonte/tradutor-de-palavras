# tradutor-de-palavras
Este projeto tem como função traduzir palavras do inglês para o português conforme selecionadas na área de transferência. 

# Funcionalidades 
Monitoramento contínuo da área de transferência (clipboard) a cada 4 segundos.

Tradução automática de palavras do inglês para o português.

Exibição da tradução no terminal apenas quando o conteúdo copiado for diferente do anterior.

# Bibliotecas e Tecnologias Utilizadas
pyperclip (para acessar a área de transferência)

googletrans (para realizar a tradução)

time (para controlar os intervalos de verificação - biblioteca nativa do Python)

# Instalação das Dependências
Execute os seguintes comandos para instalar as bibliotecas necessárias:

```bash
pip install pyperclip
pip install googletrans==4.0.0-rc1
```
Obs: A versão do googletrans recomendada é a 4.0.0-rc1, pois versões anteriores podem apresentar instabilidades.

# Como Funciona
O script verifica o conteúdo da área de transferência a cada 4 segundos.

Caso o conteúdo copiado seja diferente do anterior, ele será traduzido.

A tradução do inglês para o português será exibida no terminal.

Se o conteúdo copiado for igual ao anterior, nenhuma nova tradução será exibida.

Esse projeto é útil para quem precisa traduzir rapidamente palavras durante leituras ou estudos em inglês, otimizando o fluxo de trabalho.