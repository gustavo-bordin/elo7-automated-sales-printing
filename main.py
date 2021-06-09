import os
import requests
from time import sleep

import static
from helpers.soup import create_soup_obj
from elo7 import Elo7


class Print4Me(Elo7):
    pdf_url = "https://www.elo7.com.br/t7/{}/content-statement"

    def __init__(self, names):
        super().__init__(names)

    def start(self):
        return self._get_pdf_urls()

    def _get_pdf_urls(self):
        initial_names_len = len(self.names)
        page = 1

        while True:
            print(f"Coletando os seus pedidos na Elo7 na pagina {page}...")
            orders_content = self.get_orders_content(page=page)
            print("Pedidos coletados!")
            print("Organizando seus pedidos... bip! bip!")
            parsed_orders = create_soup_obj(orders_content)
            print("Pedidos organizados!")
            print("Procurando pelos compradores... hmmm")
            order_list = self.get_order_list(parsed_orders)
            self.get_order_ids(order_list)

            new_names_len = len(self.names)

            if new_names_len != 0:
                if new_names_len < initial_names_len:
                    print("Encontrei alguns compradores, mas não todos :(")
                    print(f"Estou prosseguindo para a pagina {page + 1} \
                           para continuar a procura...")
            
            else:
                print("Encontrei todas as pessoas mencionadas :D, prosseguindo \
                       para a coleta dos PDFs... bip! bip!")
                print(static.COOKIES)
                return self._download_pdfs()

            page += 1
            sleep(3)

    def _download_pdfs(self):
        print("Começando a coleta de PDFs...")
        for id_ in self.ids:
            print(f"Encontrei o PDF do pedido {id_}, prosseguindo...")
            request = requests.get(self.pdf_url.format(id_), 
                                   cookies=static.COOKIES, 
                                   headers=static.HEADERS)
            
            print("Fiz o download do PDF, salvando... bip! bip!")
            with open(f"pdfs/pdf_{id_}.pdf", "wb") as pdf:
                pdf.write(request.content)

            print("PDF SALVO!!")

        print("Coleta de PDFs finalizada, encaminhando para a impressão...")
        return self._print()

    def _print(self):
        for directory, _, pdfs in os.walk('pdfs'):
            for pdf in pdfs:
                pdf_path = os.path.abspath(os.path.join(directory, pdf))
                print('Enviando requisição para imprimir o documento')
                os.system(f"lpr -P {static.PRINTER_NAME} {pdf_path}")
                print('Requisição enviada, aguardando 10 segundos para a proxima...')
                sleep(10)
        
        print("Tudo finalizado!! O programa será encerrado e a impressão deverá seguir!")



names = []
iteration_count = 0

print("###################################################")
buyers_amount = int(input("Digite a quantidade de impressões e aperte ENTER: "))

for buyer_count in range(1, buyers_amount + 1):
    name = input(f"\nDigite o nome da {buyer_count}º compradora e aperte ENTER: ")
    names.append(name)
    print(f"\nComprador(a) {name} registrado!\n")

p4me = Print4Me(names)
p4me.start()