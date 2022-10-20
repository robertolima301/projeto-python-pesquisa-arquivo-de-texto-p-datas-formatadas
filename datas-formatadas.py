# Arquivo de banco de dados onde pesquisa arquivo de texto para datas formatadas
# /usr/bin/env python
# date2SQL.py -- pesquisa arquivo de texto para datas formatadas
# MM-DD-AAAA ou MM/DD/AAAA ou MM.DD.AAAA e crie
# novo arquivo convertendo-os para o estilo SQL YYYY-MM-DD ou lidar com
M/D/AAAA.

import sys, re

file = open(sys.argv[1])
newfile = open(sys.argv[1]+'.SQLdates', "w")

regex = re.compile('[\d][\d][\./-][\d][\d][\./-][\d][\d][\d][\d]')

line = file.readline()
while line:
    if regex.search(line):
        datelist=regex.findall(line)
        for n in range(len(datelist)):
            date=datelist[n][0:10]
            newdate=date[6:10]+'-'+date[0:2]+'-'+date[3:5]
            line=re.sub(date, newdate, line)
        newfile.write(line)
    else: newfile.write(line)
    line = file.readline()

file.close()
newfile.close()


