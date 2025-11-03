import os, requests, sys, json

ACCESS_TOKEN = os.environ.get("ML_ACCESS_TOKEN", "")
if not ACCESS_TOKEN:
    print("ERRO: ML_ACCESS_TOKEN não definido nos Secrets")
    sys.exit(1)

r = requests.get(
    "https://api.mercadolibre.com/users/me",
    headers={
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Accept": "application/json",
        "User-Agent": "cleiton-ml-pipeline/1.0"
    },
    timeout=30
)

print("STATUS:", r.status_code)
print("CONTENT-TYPE:", r.headers.get("content-type", ""))
print("PREVIEW:", r.text[:300])
r.raise_for_status()
print("OK: token válido para /users/me")
