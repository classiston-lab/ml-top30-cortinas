# smoke.py — valida acesso à API do Mercado Livre fora do Colab
import requests

URL = "https://api.mercadolivre.com/sites/MLB/search"
params = {"q": "cortina", "limit": 1, "offset": 0}
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Accept": "application/json",
    "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
    "Connection": "keep-alive",
}

r = requests.get(URL, params=params, headers=headers, timeout=30)
print("STATUS:", r.status_code)
print("URL:", r.url)
print("BODY PREVIEW:", r.text[:300])
r.raise_for_status()
print("OK: API acessível a partir do runner do GitHub.")
