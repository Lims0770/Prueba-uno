
import argparse

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

def main():
    parser = argparse.ArgumentParser(description="Determinar la clase de una dirección IP")
    parser.add_argument("ip", help="Dirección IP a verificar")
    parser.add_argument("clase", help="Clase esperada de la dirección IP")

    args = parser.parse_args()
    ip = args.ip
    clase_correcta = args.clase
    clase_calculada = obtener_clase_ip(ip)

    if clase_calculada == clase_correcta:
        print(f"La dirección IP {ip} corresponde a la clase {clase_correcta}.")
    else:
        print(f"La dirección IP {ip} no corresponde a la clase {clase_correcta}. Pertenece a la clase {clase_calculada}.")

if __name__ == "__main__":
    main()
