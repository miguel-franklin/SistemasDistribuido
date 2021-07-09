import requests
from requests.models import Response


URL = "https://double-nirvana-273602.appspot.com/?hl=pt-BR"
SOMAR = 1
SUBTRAIR = 2
MULTI = 3
DIVIDIR = 4


# handle de tratamento de resposta
def print_response(r:Response, *args, **kwargs):
    # Se o status do response vier ok o programa printa o retorno
    if r.status_code in (200, 201):
        print(r.request.url)
        print("Printing Reponse:\n")
        print(r.text)

# Monta o payload
payload = { "oper1": 5, "oper2": 5, "operacao": SOMAR}

# Envia o post request para o endereco informado
# Como nao ha definicao no header de content type ele seta como padrao o multipar/form-data
# ao definir hooks voce aponta um handle para o metodo print_response para tratar o response
r = requests.post(URL, payload, hooks={'response': print_response})


payload = { "oper1": 5, "oper2": 5, "operacao": SUBTRAIR}
r = requests.post(URL, payload, hooks={'response': print_response})
payload = { "oper1": 5, "oper2": 5, "operacao": MULTI}
r = requests.post(URL, payload, hooks={'response': print_response})
payload = { "oper1": 5, "oper2": 5, "operacao": DIVIDIR}
r = requests.post(URL, payload, hooks={'response': print_response})



