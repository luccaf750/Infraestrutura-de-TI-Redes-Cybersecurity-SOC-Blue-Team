# Event ID 4720 - User Account Created

## Descrição

O Event ID `4720` indica que uma conta de usuário foi criada.

## Campos relevantes

- Subject Account Name
- Subject Domain Name
- New Account Name
- New Account ID
- Account Domain
- Privilege-related context

## O que analisar

- Quem criou a conta?
- A criação estava autorizada?
- Qual nome foi atribuído?
- Quando ocorreu?
- A conta recebeu privilégios posteriormente?
- Houve logon utilizando a nova conta?
- A criação ocorreu após outro evento suspeito?

## Possíveis cenários

- provisionamento legítimo;
- atividade de administrador;
- criação não autorizada;
- persistência após comprometimento.

## Correlação

Uma investigação pode procurar eventos posteriores relacionados à nova conta, como autenticações e alterações de grupos ou privilégios.
