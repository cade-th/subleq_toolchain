from assembler.src.parser import Parser
from test_utils import error_log

def preproc(test_name, data):
    # print(f"Test {test_name}:")
    success = False

    parser = Parser(data["input"]["tokens"]) 

    tokens = data["input"]["tokens"]
    
    tokens = parser.preproc()

    out_p = data["output"]

    if tokens != out_p["tokens"]:
        error_log(test_name, out_p["tokens"], tokens, "tokens")
        return success 
    
    success = True
    return success


 
def p2_macro(test_name, data):
    success = False

    parser = Parser(data["input"]["tokens"]) 

    tokens = data["input"]["tokens"]
    mnt = data["input"]["mnt"]
    mdt = data["input"]["mdt"]
    
    tokens = parser.macro_p2(mnt, mdt)

    out_p = data["output"]

    if tokens != out_p["tokens"]:
        error_log(test_name, out_p["tokens"], tokens, "tokens")
        return success 
    
    success = True
    return success

def p1_macro(test_name, data):
    # print(f"Test {test_name}:")
    success = True

    parser = Parser(data["input"]["tokens"]) 
    
    tokens, mnt, mdt = parser.macro_p1()

    # TODO: refactor data to be shorter
    if tokens != data["output"]["tokens"]:
        error_log(test_name, data["output"]["tokens"], tokens, "tokens")
        success = False

    if mnt != data["output"]["mnt"]:
        error_log(test_name, data["output"]["mnt"], mnt, "mnt")
        success = False

    if mdt != data["output"]["mdt"]:
        error_log(test_name, data["output"]["mdt"], mdt, "mdt")
        success = False


    if not success:
        return False
    else:
        return True
