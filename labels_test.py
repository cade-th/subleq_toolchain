from assembler.src.parser import Parser
from test_utils import error_log

def p1_label(test_name, data):
    # print(f"Test {test_name}:")
    success = True

    parser = Parser(data["input"]["tokens"])
    tokens, sym_table = parser.p1_label()

    if tokens != data["output"]["tokens"]:
        error_log(test_name, data["output"]["tokens"], tokens, "tokens")
        success = False

    if sym_table != data["output"]["sym_table"]:
        error_log(test_name, data["output"]["sym_table"], sym_table, "sym_table")
        success = False

    return success

def p2_label(test_name, data):
    # print(f"Test {test_name}:")
    success = False

    parser = Parser(data["input"]["tokens"])

    tokens = data["input"]["tokens"]
    sym_table = data["input"]["sym_table"]

    tokens = parser.p2_label(sym_table)

    out_p = data["output"]

    if tokens != out_p["tokens"]:
        error_log(test_name, out_p["tokens"], tokens, "tokens")
        return success

    success = True
    return success
