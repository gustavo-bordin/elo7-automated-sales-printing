import requests

import static


class Elo7:
    sales_url = "https://www.elo7.com.br/seller/list/order/OPEN? \
                 sortType=orderDate&pageNum={}&query="
    
    def __init__(self, names):
        self.names = names
        self.ids = []

    def get_orders_content(self, page):
        request = requests.get(self.sales_url.format(page), 
                            cookies=static.COOKIES, 
                            headers=static.HEADERS)

        return request.content

    def get_order_list(self, parsed_orders):
        order_list = parsed_orders.find_all("li", class_="order")
        return order_list

    def _get_order_id(self, order):
        order_uri = order.find("a", class_="print-content-statement")["href"]
        return order_uri.split('/')[2]

    def _get_buyer_name(self, order):
        name = order.find("span", class_="store-name").get_text()
        return name.lower()

    def get_order_ids(self, order_list):
        for order in order_list:
            buyer_name = self._get_buyer_name(order)
            if buyer_name in self.names:
                id_ = self._get_order_id(order)
                self.names.remove(buyer_name)
                self.ids.append(id_)
            
       