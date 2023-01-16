# Recupera el dolar blue del día y lo envia por WhatsApp


import requests

from bs4 import BeautifulSoup

import pywhatkit
 

response = requests.get("https://www.cronista.com/MercadosOnline/moneda.html?id=ARSB")

print(response)


html_string = response.text

document = BeautifulSoup(html_string, "html.parser")

datas = document.find_all("li")[1]


try: 

#   # Enviamos el mensaje

  pywhatkit.sendwhatmsg("+542994101328",  
                        datas.text,
                       13,2)
                

  print("Mensaje Enviado") 
  
  

except: 

  print("Ocurrio Un Error")
