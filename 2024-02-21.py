
import os
import platform

def obtener_ip():
    sistema_operativo = platform.system()

    if sistema_operativo == "Windows":
        ip = os.popen('ipconfig').read()
         #= resultado.find('IPv4 Address')
       # ip = resultado[inicio:].split('\n')[0].split(':')[-1].strip()

    elif sistema_operativo == "Linux":
        ip = os.popen('ifconfig').read()
        # = resultado.find('inet ')
        #ip = resultado[inicio:].split(' ')[1]

    
    

    return print(f"La dirección IP del sistema es: {ip}")

if __name__ == "__main__":
    obtener_ip()
