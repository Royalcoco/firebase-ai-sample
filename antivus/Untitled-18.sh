#!/bin/bash

# Exemple d'adresses IP suspectes détectées
suspect_ips=("192.168.1.2" "192.168.1.4")

# Configuration du pare-feu pour bloquer ces adresses IP
for ip in "${suspect_ips[@]}"
do
    iptables -A INPUT -s $ip -j DROP
    iptables -A FORWARD -s $ip -j DROP
done

# Enregistrer les règles iptables
iptables-save > /etc/iptables/rules.v4
