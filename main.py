import requests
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Email, To

API_KEY = "SUA_CHAVE_NEWSAPI"
SENDGRID_API_KEY = "SUA_CHAVE_SENDGRID"

EMAIL = "SEU_EMAIL_VERIFICADO"

def buscar_noticias():
    url = "https://newsapi.org/v2/everything"
    
    params = {
        "q": "technology",
        "language": "en",
        "sortBy": "publishedAt",
        "pageSize": 5,
        "apiKey": API_KEY
    }

    response = requests.get(url, params=params)
    dados = response.json()

    artigos = dados.get("articles", [])

    conteudo = "📰 Notícias de Tecnologia\n\n"

    for i, artigo in enumerate(artigos, 1):
        titulo = artigo.get("title") or "Sem título"
        link = artigo.get("url") or ""
        
        conteudo += f"{i}. {titulo}\n{link}\n\n"

    return conteudo


def enviar_email(conteudo):
    message = Mail(
        from_email=Email(EMAIL),
        to_emails=To(EMAIL),
        subject='📰 Notícias do Dia',
        plain_text_content=conteudo
    )

    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        print("Email enviado! Status:", response.status_code)
    except Exception as e:
        print("Erro ao enviar:", e)


texto_email = buscar_noticias()
print(texto_email)

enviar_email(texto_email)