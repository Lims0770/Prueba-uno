
import sys

def obtener_clase_ip(direccion_ip):
    primer_octeto = int(direccion_ip.split('.')[0])
    if 1 <= primer_octeto <= 126:
        return "A"
    elif 128 <= primer_octeto <= 191:
        return "B"
    elif 192 <= primer_octeto <= 223:
        return "C"
    elif 224 <= primer_octeto <= 239:
        return "D"
    elif 240 <= primer_octeto <= 255:
        return "E"
    else:
        return "Desconocida"

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python script.py <IP> <Clase>")
    else:
        ip = sys.argv[1]
        clase_correcta = sys.argv[2]
        clase_calculada = obtener_clase_ip(ip)
        
        if clase_calculada == clase_correcta:
            print(f"La dirección IP {ip} corresponde a la clase {clase_correcta}.")
        else:
            print(f"La dirección IP {ip} no corresponde a la clase {clase_correcta}. Pertenece a la clase {clase_calculada}.")
