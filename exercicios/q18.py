
tamanho_arquivo_mb = float(input("Qual o tamanho do seu arquivo para download (em MB): "))

velocidade_link_mbps = float(input("Digite a velocidade do link (em Mbps): "))

tamanho_arquivo_mbits = tamanho_arquivo_mb * 8

tempo_download_segundos = tamanho_arquivo_mbits / velocidade_link_mbps

tempo_download_minutos = tempo_download_segundos / 60

print(f"O tempo aproximado de download é de {tempo_download_minutos:.2f} minutos.")