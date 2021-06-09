from dotenv import dotenv_values

cookies_env = dotenv_values("cookies.env")

PRINTER_NAME = "HP_Ink_Tank_Wireless_410_series_3CC611_"

COOKIES = cookies_env

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.5",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Host": "www.elo7.com.br",
    "Referer": "https://www.elo7.com.br/sellerOrder.do?command=showOrderHistoryForm",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0"
}