def usingGlobal():
    GLOBAL_CONST = 42
    print(GLOBAL_CONST)
    GLOBAL_CONST = 777
    print(GLOBAL_CONST)
    GLOBAL_CONST = 777
    print("GLOBAL_CONST:",GLOBAL_CONST)
    
usingGlobal()

