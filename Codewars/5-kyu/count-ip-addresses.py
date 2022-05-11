# https://www.codewars.com/kata/526989a41034285187000de4/python

# 5 kyu

# Count IP Addresses

def ips_between(start, end):
    s =iptoint(start)
    e = iptoint(end)
    f = s - e
    return abs(f)

def iptoint(ip):
        h=list(map(int,ip.split(".")))
        return (h[0]<<24)+(h[1]<<16)+(h[2]<<8)+(h[3]<<0)

from ipaddress import ip_address

def ips_between(start, end):
    return int(ip_address(end)) - int(ip_address(start))
