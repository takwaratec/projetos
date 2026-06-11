import os, glob, json, urllib.request, ssl, time

# --- Configurações ---
context = ssl._create_unverified_context()
TXT_DIR = '01_SOMBRA_AUDITORIA/04_PROJETO_WTF/03_PESQUISA_EM_ANDAMENTO/TRANSCRIPT'
MD_DIR = '01_SOMBRA_AUDITORIA/02_TECNICO/02_ESTUDOS_E_PESQUISA'
API_KEY = os.getenv('GOOGLE_API_KEY')

PROMPT = """Atue como Pesquisador e Biblioteconomista. Gere uma ficha científica estritamente neste formato:
---
autor_principal: "..."
ano: "..."
local: "..."
palavras_chave: ["...", "..."]
---
### RESENHA TÉCNICA
(Parágrafo denso sobre metodologia e resultados)
### DADOS PARAMÉTRICOS
(Lista de números e medidas extraídos)
"""

for txt_path in glob.glob(f'{TXT_DIR}/RAW_*.txt'):
    nome_base = os.path.basename(txt_path).replace('.txt', '')
    dest_md = f'{MD_DIR}/CAT_{nome_base}.md'
    
    print(f"🏗️  Reconstruindo do zero: {nome_base}...")
    
    try:
        with open(txt_path, 'r', encoding='utf-8', errors='ignore') as f:
            texto = f.read()[:12000]

        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={API_KEY}"
        data = {"contents": [{"parts": [{"text": f"{PROMPT}\n\nTexto: {texto}"}]}]}
        req = urllib.request.Request(url, data=json.dumps(data).encode('utf-8'), headers={'Content-Type': 'application/json'})
        
        with urllib.request.urlopen(req, context=context) as response:
            res_data = json.loads(response.read().decode('utf-8'))
            ia_content = res_data['candidates'][0]['content']['parts'][0]['text']
            
            # Montagem final garantida
            conteudo_final = f"{ia_content.strip()}\n\n---\n**DOI Acervo:** 10.5281/zenodo.18827106\n**Coleção:** WTF — Mulheres que Tecem a Floresta"
            
            with open(dest_md, 'w', encoding='utf-8') as f:
                f.write(conteudo_final)
            print(f"✅ Sucesso!")
            time.sleep(1)

    except Exception as e:
        print(f"❌ Erro em {nome_base}: {e}")