import os, glob, re

# --- Configurações de Caminhos ---
BASE_DIR = '01_SOMBRA_AUDITORIA/02_TECNICO/02_ESTUDOS_E_PESQUISA'
MAPA_PATH = 'MAPA_TEMATICO_WTF.md'
REF_PATH = '01_SOMBRA_AUDITORIA/QUARENTENA/docs_Legacy_Sombra/05_ADVOCACY_COP30/BD_referencias-acervo.md'

def gerar_mapa():
    fichas = glob.glob(f'{BASE_DIR}/CAT_*.md')
    print(f"🗺️  Mapeando {len(fichas)} itens do acervo...")

    conteudo_mapa = [
        "# 🗺️ Mapa Temático do Acervo — Mulheres que Tecem a Floresta (WTF)",
        "\n> **Status:** Acervo Auditado v2.1 | **DOI Master:** 10.5281/zenodo.18827106",
        "\nEste mapa organiza a inteligência técnica do projeto Takwara, facilitando a revisão bibliográfica e a redação de manuais.\n",
        "| ID | Título / Arquivo | Autor | Ano | Eixo Sugerido |",
        "|:---|:---|:---|:---|:---|"
    ]

    for i, ficha_path in enumerate(sorted(fichas), 1):
        with open(ficha_path, 'r', encoding='utf-8') as f:
            texto = f.read()

        # Extração de metadados via regex simples no YAML
        titulo = re.search(r'titulo_original: "(.*?)"', texto)
        autor = re.search(r'autor_principal: "(.*?)"', texto)
        ano = re.search(r'ano: "(.*?)"', texto)
        
        t = titulo.group(1) if titulo else os.path.basename(ficha_path)
        a = autor.group(1) if autor else "N/A"
        y = ano.group(1) if ano else "N/A"
        
        # Lógica de Eixo baseada no nome do arquivo ou conteúdo
        eixo = "Bambu" if "BAM" in t.upper() or "BAMBU" in t.upper() else "Bioeconomia"
        if "IMPERVEG" in t.upper() or "PU" in t.upper(): eixo = "Biopolímeros"
        if "SANEA" in t.upper(): eixo = "Saneamento"

        conteudo_mapa.append(f"| {i:03} | [{t}]({ficha_path}) | {a} | {y} | {eixo} |")

    # Adiciona link para o Banco de Referências
    conteudo_mapa.append(f"\n\n---\n🔗 **Integração:** [Banco de Referências Mestre (DOI/Links)]({REF_PATH})")

    with open(MAPA_PATH, 'w', encoding='utf-8') as f:
        f.write("\n".join(conteudo_mapa))
    
    print(f"✅ Mapa Temático gerado com sucesso em: {MAPA_PATH}")

if __name__ == "__main__":
    gerar_mapa()