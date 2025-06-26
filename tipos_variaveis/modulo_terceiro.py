print("\nImportação e uso de um módulo de terceiros")

import requests

url = "https://github.com"
response = requests.get(url)
print(f"Solicitacao HTTP para {url} retornou o status {response.status_code}")