# secure-client-server

Sistema cliente e servidor para comunicar com uma base dados e salvar informações de Aluno.
A comunicação é realizada de maneira segura através dos protocolos HTTP e TLS.

Python3 é utilizado.

## Logs de autenticação (Certificados Inválidos)

### Cliente com certificado auto-assinado

- Lado do cliente: Problema na conexão: [SSL: TLSV1_ALERT_UNKNOWN_CA] tlsv1 alert unknown ca (\_ssl.c:1129)
- Lado do servidor: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self signed certificate (\_ssl.c:1129)

### Servidor com certificado auto-assinado

- Lado do cliente: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self signed certificate (\_ssl.c:1129)
- Lado do servidor: [SSL: TLSV1_ALERT_UNKNOWN_CA] tlsv1 alert unknown ca (\_ssl.c:1129)

## Useful Links

[Python Sockets](https://realpython.com/python-sockets/)

[Minha Implementação do Diffie-Hellman](https://www.inf.ufpr.br/cnb18/relatorioRedes2/relatorio.html)
