import os, glob, json, urllib.request, ssl, time

# --- Configurações de Ambiente ---
context = ssl._create_unverified_context()
ORIGEM_TXT = '01_SOMBRA_AUDITORIA/04_PROJETO_WTF/03_PESQUISA_EM_ANDAMENTO/TRANSCRIPT/AMAZONIA_GESTORAS'
DESTINO_MD = '01_SOMBRA_AUDITORIA/02_TECNICO/02_ESTUDOS_E_PESQUISA/AMAZONIA_GESTORAS'
API_KEY = os.getenv('GOOGLE_API_KEY')

# --- Prompt de Especialista ---
PROMPT_CIENTIFICO = """Atue como Pesquisador Sênior e Biblioteconomista. 
Analise o texto técnico fornecido e extraia RIGOROSAMENTE os seguintes campos para um cabeçalho YAML e uma Resenha Acadêmica:
1. Autor Principal (Pessoa ou Instituição)
2. Ano de Publicação
3. Local/Região de referência
4. Palavras-chave (mínimo 3)
5. RESENHA TÉCNICA (1 parágrafo denso com Metodologia e Resultados)
6. DADOS PARAMÉTRICOS (Extraia números, medidas ou resistências citadas)

Responda APENAS no formato:
---
autor_principal: "..."
ano: "..."
local: "..."
palavras_chave: ["...", "..."]
---
### RESENHA TÉCNICA
...
### DADOS PARAMÉTRICOS
...
"""

for arq_path in glob.glob(f'{ORIGEM_TXT}/RAW_*.txt'):
    nome_base = os.path.basename(arq_path).replace('.txt', '')
    dest_path = f'{DESTINO_MD}/CAT_{nome_base}.md'
    
    print(f"🔬 Extraindo Ciência: {nome_base}...")
    
    try:
        with open(arq_path, 'r', encoding='utf-8', errors='ignore') as f:
            texto = f.read()[:12000] # Mais contexto para capturar autores

        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={API_KEY}"
        data = {"contents": [{"parts": [{"text": f"{PROMPT_CIENTIFICO}\n\nTexto: {texto}"}]}]}
        
        req = urllib.request.Request(url, data=json.dumps(data).encode('utf-8'), headers={'Content-Type': 'application/json'})
        
        with urllib.request.urlopen(req, context=context) as response:
            res_data = json.loads(response.read().decode('utf-8'))
            markdown_cientifico = res_data['candidates'][0]['content']['parts'][0]['text']
            
            # Atualiza a ficha mantendo o DOI Master
            footer = f"\n\n---\n**DOI Acervo:** 10.5281/zenodo.18827106\n**Coleção:** WTF - Mulheres que Tecem a Floresta"
            
            with open(dest_path, 'w', encoding='utf-8') as f:
                f.write(markdown_cientifico + footer)
            print(f"✅ Ficha Científica Atualizada!")
            time.sleep(1) # Cota segura para Nível Pago 1

    except Exception as e:
        print(f"⚠️ Erro em {nome_base}: {e}")