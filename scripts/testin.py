import os
import datetime

# Define um caminho onde a aplicação comprovadamente tem escrita (pasta de logs ou tmp)
log_path = "/tmp/gradio/evidence.txt"

try:
    # Comando inofensivo que identifica o usuário e o contexto
    evidence = f"""
    --- AUDITORIA DE SEGURANÇA ---
    Data/Hora: {datetime.datetime.now()}
    Usuário do Processo: {os.popen('whoami').read().strip()}
    Hostname: {os.popen('hostname').read().strip()}
    ID: {os.popen('id').read().strip()}
    -------------------------------
    """
    with open(log_path, "w") as f:
        f.write(evidence)
except Exception as e:
    pass
