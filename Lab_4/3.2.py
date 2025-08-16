GLOBAL_CONST = 123

def usingGlobal():
    global GLOBAL_CONST
    print(GLOBAL_CONST)
    GLOBAL_CONST = 777
    print(GLOBAL_CONST)

usingGlobal()
print("Ngoài hàm:", GLOBAL_CONST)
