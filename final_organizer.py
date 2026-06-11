import os
import shutil
import re
from datetime import datetime, timedelta

# --- Configurações da Mesa de Operação ---
STAGING_BASE = '01_SOMBRA_AUDITORIA/CLEAN_ROOM_STAGING'
FINAL_BASE = '01_SOMBRA_AUDITORIA/REPO_EXECUTIVO_2026'

# Mapeamento Corporativo (De: Para)
STRUCTURE_MAP = [
    ('.agents', '01_GOVERNANCA/.agents'),
    ('01_SOMBRA_AUDITORIA/04_PROJETO_WTF/01_GOVERNANCA', '01_GOVERNANCA'),
    ('01_SOMBRA_AUDITORIA/04_PROJETO_WTF/02_TECNICO', '02_TECNICO'),
    ('08_PROJETOS_ENGENHARIA', '02_TECNICO/08_ENGENHARIA'),
    ('docs/09_DOSSIE_BNDES', '03_DOSSIE_BNDES'),
    ('01_SOMBRA_AUDITORIA/04_PROJETO_WTF/01_GOVERNANCA/02_ORCAMENTO_E_LOGISTICA', '03_DOSSIE_BNDES/02_FINANCEIRO_LOGISTICA'),
    ('01_SOMBRA_AUDITORIA/04_PROJETO_WTF/03_PESQUISA_EM_ANDAMENTO', '04_PESQUISA_ANDAMENTO'),
    ('99_RESTRITO', '99_RESTRITO')
]

# Prefixos a remover
PREFIXES_TO_PURGE = ['WTF_', 'TAK_', 'TAK-', 'WTF-']

def clean_filename(filename):
    for prefix in PREFIXES_TO_PURGE:
        filename = filename.replace(prefix, '')
    return filename

def filter_finance(file_path):
    # Lógica: Se estiver em pastas de orçamento/financeiro, checar data
    if any(x in file_path for x in ['ORCAMENTO', 'FINANCEIRO', '02_TRIAGEM_BRUTA']):
        mtime = datetime.fromtimestamp(os.path.getmtime(file_path))
        cutoff = datetime.now() - timedelta(days=15)
        if mtime < cutoff:
            return False # Ignorar antigo
    return True

def build_executive_repo():
    print("💼 Consolidando Repositório Executivo BNDES 2026...")
    os.makedirs(FINAL_BASE, exist_ok=True)
    
    for src_rel, dest_rel in STRUCTURE_MAP:
        src_full = os.path.join(STAGING_BASE, src_rel)
        if not os.path.exists(src_full): continue
        
        for root, dirs, files in os.walk(src_full):
            for file in files:
                src_path = os.path.join(root, file)
                
                # Check Finance Filter
                if not filter_finance(src_path):
                    continue
                
                # Criar caminho de destino limpo
                rel_to_src = os.path.relpath(src_path, src_full)
                new_filename = clean_filename(file)
                dest_path = os.path.join(FINAL_BASE, dest_rel, os.path.dirname(rel_to_src), new_filename)
                
                os.makedirs(os.path.dirname(dest_path), exist_ok=True)
                shutil.copy2(src_path, dest_path)
                print(f"📦 Movido: {new_filename}")

    # Mover Imagens para central de mídia
    # (Opcional, mas o usuário pediu para preservar)
    
    print("\n✨ Repositório Executivo pronto em REPO_EXECUTIVO_2026.")

if __name__ == "__main__":
    build_executive_repo()
