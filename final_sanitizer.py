import os

FINAL_BASE = '01_SOMBRA_AUDITORIA/REPO_EXECUTIVO_2026'
PURGE_TERMS = ['WTF', 'TAK']

def sanitize_repo():
    print("🧹 Iniciando Sanitização Final de Nomes...")
    
    # Rodar de baixo para cima para evitar erros de diretório renomeado
    for root, dirs, files in os.walk(FINAL_BASE, topdown=False):
        for name in files + dirs:
            old_path = os.path.join(root, name)
            new_name = name
            for term in PURGE_TERMS:
                new_name = new_name.replace(term + '_', '').replace('_' + term, '').replace(term, '')
            
            # Limpar underscores duplos ou sobrando
            new_name = new_name.replace('__', '_').strip('_')
            
            # Caso especial: Se o nome ficou vazio, manter o original ou dar erro
            if not new_name: 
                new_name = "asset_" + name
                
            if new_name != name:
                new_path = os.path.join(root, new_name)
                # Se o destino já existe, tentar um sufixo
                if os.path.exists(new_path):
                     new_path = new_path + "_alt"
                     
                os.rename(old_path, new_path)
                print(f"🔄 Renomeado: {name} -> {new_name}")

if __name__ == "__main__":
    sanitize_repo()
