# secure-client-server

Sistema cliente e servidor para comunicar com uma base dados e salvar informações de Aluno.
A comunicação é realizada de maneira segura através dos protocolos HTTP e TLS, escritos utilizando a linguagem python em sua versão 3.

Dados sensíveis de alunos são trafegados pela aplicação, como por exemplo CPF, o que motiva a utilização desses protocolos que garantem o sigilo, autenticidade e integridade. Para um passo a passo de como implementar um cliente/servidor com TLS em python veja o tutorial:
[Cliente/Servidor Seguro com TLS e Python Sockets](https://www.youtube.com/watch?v=8AlmRA68JnU)

Além disso o vídeo demonstra as propriedades de `Sigilo, Autencidade e Integridade` que são proporcionadas pelo TLS.

# Organização do código

O código está separado em duas (2) pastas principais: "client" e "server". Cada pasta possui os arquivos necessários para a execução do cliente e do servidor, respectivamente.

O arquivo `main.py` é o principal de ambos e responsável pela inicialização do fluxo. A lógica de negócio esta do lado do cliente o qual permite as ações:` criar, atualizar, listar, deletar, sair ou exit`.

A lógica de conexão e gerenciamento do que se refere a comunicação cliente-servidor está no arquivo `client/client.py` para o cliente, e no arquivo `server/server.py` para o servidor. Todos os outros arquivos são referentes à outros aspectos do sistema (regras de negócio, modelos do banco, validação de parâmetros, etc).

## Execução

Para executar o código, estando na pasta client, por exemplo:

```console
    $ python3 main.py
```

Para o servidor o comando é o mesmo, basta estar na pasta correta.

Obs: **Primeiro deve ser executado o servidor e depois o cliente para que a conexão tenha sucesso.**

Com os programas conectados o cliente aguardará uma entrada do usuário:

```console
  $ >
```
Os comandos aceitos foram descritos acima e são:
`criar, atualizar, listar, deletar, sair, exit`

Após digitar um comando e pressionar `enter` o usuário será guiado a preencher o que for necessário.

Exemplo de criação:

```
> criar
===Criação de aluno===
> Nome do aluno: aluno teste
> Idade do aluno: 16
> CPF do aluno: 123.123.123-13
> e-mail do aluno: email@email.com
mensagem enviada:  {"action": "create", "data": {"name": "aluno teste", "age": "16", "br_document": "123.123.123-13", "email": "email@email.com"}}
server_response:  {'status': 'OK', 'message': 'ok'}
>
```
A cada interação é apresentado no console a mensagem enviada e a resposta do servidor.
```
mensagem enviada:  {"action": "create", "data": {"name": "aluno teste", "age": "16", "br_document": "123.123.123-13", "email": "email@email.com"}}
server_response:  {'status': 'OK', 'message': 'ok'}
```

Do lado do servidor também é possível conferir um log de sucesso na execução, para esse exemplo:
```console
Starting server...
Server started...
Ação criar executada.
```

## Dependências

* SSL
* peewee

## Logs de autenticação (Certificados Inválidos)

### Cliente com certificado auto-assinado

- Lado do cliente: Problema na conexão: [SSL: TLSV1_ALERT_UNKNOWN_CA] tlsv1 alert unknown ca (\_ssl.c:1129)
- Lado do servidor: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self signed certificate (\_ssl.c:1129)

### Servidor com certificado auto-assinado

- Lado do cliente: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self signed certificate (\_ssl.c:1129)
- Lado do servidor: [SSL: TLSV1_ALERT_UNKNOWN_CA] tlsv1 alert unknown ca (\_ssl.c:1129)

### Links úteis

[Python Sockets](https://realpython.com/python-sockets/)

## Motivação

Código e tutorial criados como parte da disciplina CI1365: TÓPICOS EM REDES DE COMPUTADORES do curso de Bacharelado em Ciência da Computação da Universidade Federal do Paraná (UFPR) - 2022
