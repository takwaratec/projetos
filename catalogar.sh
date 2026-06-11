#!/usr/bin/env python3
import os, glob, json, urllib.request, ssl, time

# --- A VACINA SSL ---
context = ssl._create_unverified_context()

# Configurações
ORIGEM = '01_SOMBRA_AUDITORIA/04_PROJETO_WTF/03_PESQUISA_EM_ANDAMENTO/TRANSCRIPT'
DESTINO = '01_SOMBRA_AUDITORIA/02_TECNICO/02_ESTUDOS_E_PESQUISA'
API_KEY = os.getenv('GOOGLE_API_KEY')

os.makedirs(DESTINO, exist_ok=True)

PROMPT_BASE = "Aja como Biblioteconomista e Especialista em Bioeconomia. Analise o texto e gere uma FICHA DE CATALOGO em Markdown com: Titulo Original, Sigla Takwara (ex: TAK-BAM-MAN), Orgao (EMBRAPA, BNDES, etc), Eixo, Sub-Eixo, Resumo Executivo (3 linhas) e Potencial para o Projeto Mulheres Bioeconomia Amazonia."

for arq_path in glob.glob(f'{ORIGEM}/RAW_*.txt'):
    nome_base = os.path.basename(arq_path).replace('.txt', '')
    dest_path = f'{DESTINO}/CAT_{nome_base}.md'
    
    if os.path.exists(dest_path): continue 

    print(f"🏷️  Catalogando: {nome_base}...")
    
    sucesso = False
    tentativas = 0
    
    while not sucesso and tentativas < 3:
        try:
            with open(arq_path, 'r', encoding='utf-8', errors='ignore') as f:
                texto = f.read()[:8000]

            url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={API_KEY}"
            data = {"contents": [{"parts": [{"text": f"{PROMPT_BASE}\n\nTexto: {texto}"}]}]}
            
            req = urllib.request.Request(url, data=json.dumps(data).encode('utf-8'), headers={'Content-Type': 'application/json'})
            
            with urllib.request.urlopen(req, context=context) as response:
                res_data = json.loads(response.read().decode('utf-8'))
                markdown = res_data['candidates'][0]['content']['parts'][0]['text']
                
                with open(dest_path, 'w', encoding='utf-8') as f:
                    f.write(markdown)
                print(f"✅ Sucesso!")
                sucesso = True
                # Pausa de 4 segundos entre arquivos para respeitar a cota de 15 RPM (Requests Per Minute)
                time.sleep(0.5) 

        except urllib.error.HTTPError as e:
            if e.code == 429:
                print("⏳ Cota atingida. Esperando 30 segundos para retomar...")
                time.sleep(30)
                tentativas += 1
            else:
                print(f"❌ Erro HTTP {e.code}: {nome_base}")
                break
        except Exception as e:
            print(f"⚠️ Falha: {e}")
            break