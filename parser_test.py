from assembler.src.parser import Parser
from test_utils import error_log

def parser(test_name, data):
    # print(f"Test {test_name}:")
    success = False

    parser = Parser(data["input"]["tokens"]) 

    tokens = data["input"]["tokens"]
    
    tokens = parser.parse()

    out_p = data["output"]

    if tokens != out_p["tokens"]:
        error_log(test_name, out_p["tokens"], tokens, "tokens")
        return success 
    
    success = True
    return success


