#!/usr/bin/python3
import subprocess
from netaddr import IPNetwork, IPAddress, AddrFormatError

RED = "\033[91m"
RESET = "\033[0m"

def figlet():
    try:
        subprocess.call(["figlet", "IP ANALIZ"])
    except FileNotFoundError:
        print("--- IP ANALIZ ---")

def get_ip(islem_no):
    if islem_no == 1:
        try:
            # eth0 yerine varsayılan IP'yi almak daha güvenlidir
            cmd = "hostname -I | awk '{print $1}'"
            ip = subprocess.check_output(cmd, shell=True).decode().strip()
            return ip
        except Exception:
            return "127.0.0.1"
    else:
        return input("Lütfen IP adresinizi giriniz: ")

def analiz_et(ip_str):
    try:
        ip = IPAddress(ip_str)
        ilk_oktet = ip.words[0]
        
        # Sınıf ve Varsayılan Maske Belirleme
        if 1 <= ilk_oktet <= 126:
            sinif, mask = "A", "255.0.0.0"
        elif 128 <= ilk_oktet <= 191:
            sinif, mask = "B", "255.255.0.0"
        elif 192 <= ilk_oktet <= 223:
            sinif, mask = "C", "255.255.255.0"
        else:
            print("Özel veya rezerve edilmiş IP (D/E Sınıfı veya Loopback).")
            return

        network = IPNetwork(f"{ip_str}/{mask}")
        
        print(f"\n--- Analiz Sonuçları ({ip_str}) ---")
        print(f"IP Sınıfı:        {RED}Class {sinif}{RESET}")
        print(f"Ağ Adresi:        {RED}{network.network}{RESET}")
        print(f"Alt Ağ Maskesi:   {RED}{network.netmask}{RESET}")
        print(f"Broadcast Adres:  {RED}{network.broadcast}{RESET}")
        print(f"CIDR Değeri:      {RED}/{network.prefixlen}{RESET}")
        
        host_sayisi = network.size - 2
        print(f"Kullanılabilir Host: {RED}{host_sayisi}{RESET}")
        
        if host_sayisi > 2:
            yeni_host = (network.size // 2) - 2
            print(f"Bu ağ bölünebilir. \nBölünürse alt ağ başına host: {RED}{yeni_host}{RESET}")
            
    except AddrFormatError:
        print("Hata: Geçersiz bir IP formatı girdiniz!")

# Ana Akış
figlet()
secim = input("1: Makine IP'si, 2: Manuel giriş\nİşlem: ")
if secim in ['1', '2']:
    hedef_ip = get_ip(int(secim))
    if hedef_ip:
        analiz_et(hedef_ip)
else:
    print("Geçersiz seçim.")