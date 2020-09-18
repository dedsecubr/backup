# coding: utf-8
import logging
import os

op = input("Você quer fazer backup? ")

if op == 'y':
    os.system('powershell.exe Copy-Item -Path C:\\xampp\\htdocs\\dedsecurity -Recurse -Destination D:\\SITE')
    logging.basicConfig(filename='info.log', level=logging.DEBUG)
    logging.debug('Fazendo backup...')
    logging.info('O backup está funcionando!')
    logging.debug('Concluído!')
if op == 'n':
    logging.basicConfig(filename='info.log', level=logging.DEBUG)
    logging.info('não funcionou')
    exit()
