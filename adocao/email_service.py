from django.core.mail import send_mail

def enviar_email_confirmação(adocao):
    assunto= "Adocao realizada com sucesso!"
    conteudo= f"Parabéns por realizar a adoção do {adocao.pet.name} com o valor mensal de R${adocao.valor}"
    remetente= "email@email.com"
    destinatario= [adocao.email]
    send_mail(assunto, conteudo, remetente, destinatario)