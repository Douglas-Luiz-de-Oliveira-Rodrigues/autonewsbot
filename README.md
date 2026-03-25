# 📰 AutoNewsBot

Sistema automatizado em Python que busca notícias de tecnologia em tempo real e envia por email.

---

## 🚀 Sobre o Projeto

O **AutoNewsBot** é um projeto de automação desenvolvido com foco em aprendizado prático de integração com APIs e envio de emails.

O sistema realiza automaticamente:

* 🔎 Busca de notícias atualizadas via API
* 📊 Processamento e organização dos dados
* 📩 Envio automático de email com as principais notícias

Este projeto foi desenvolvido com o objetivo de praticar conceitos de automação, consumo de APIs e integração com serviços externos.

---

## 🧠 Tecnologias Utilizadas

* Python
* Requests (requisições HTTP)
* SendGrid (envio de emails)

---

## ⚙️ Funcionamento

O fluxo do sistema é:

1. Faz uma requisição para a API de notícias
2. Filtra e coleta os dados mais relevantes
3. Formata as informações em um texto organizado
4. Envia automaticamente um email com os resultados

---

## 📦 Instalação

Clone o repositório:

```bash
git clone https://github.com/Douglas-Luiz-de-Oliveira-Rodrigues/autonewsbot.git
```

Acesse a pasta:

```bash
cd autonewsbot
```

Instale as dependências:

```bash
pip install requests sendgrid
```

---

## 🔑 Configuração

Antes de executar, configure as seguintes variáveis no código:

```python
API_KEY = "SUA_CHAVE_NEWSAPI"
SENDGRID_API_KEY = "SUA_CHAVE_SENDGRID"
EMAIL = "SEU_EMAIL"
```

### ⚠️ Importante

* Não compartilhe suas chaves no GitHub
* Utilize sempre variáveis seguras em projetos reais

---

## ▶️ Execução

```bash
python main.py
```

---

## 🎯 Funcionalidades

* ✔️ Consumo de API em tempo real
* ✔️ Processamento de dados em Python
* ✔️ Envio automático de email
* ✔️ Estrutura simples e escalável

---

## 🚀 Melhorias Futuras

* 🔥 Resumo de notícias com IA
* 📱 Envio via Telegram ou WhatsApp
* 🎨 Email com layout HTML avançado
* ⏰ Automação diária (agendador)

---

## 📌 Aprendizados

Durante o desenvolvimento deste projeto, foram aplicados conceitos como:

* Integração com APIs externas
* Manipulação de dados em Python
* Automação de tarefas
* Envio de emails via serviço externo

---

## 👨‍💻 Autor

Douglas Rodrigues

---

## ⭐ Observação

Este projeto faz parte do meu processo de aprendizado em desenvolvimento e automação com Python.
