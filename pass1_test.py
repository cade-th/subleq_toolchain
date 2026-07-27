from tests.tester import run
from assembler.src.parser import Parser
import json
 
def pass1_test(test_name, data):
    print(f"Test {test_name}:")
    success = True

    parser = Parser(data["input"]["tokens"]) 
    
    tokens, sym_table, mnt, mdt = parser.pass1()

    if tokens != data["output"]["tokens"]:
        error_log(data["output"]["tokens"], tokens, "tokens")
        success = False

    if sym_table != data["output"]["sym_table"]:
        error_log(data["output"]["sym_table"], sym_table, "sym_table")
        success = False

    if mnt != data["output"]["mnt"]:
        error_log(data["output"]["mnt"], mnt, "mnt")
        success = False

    if mdt != data["output"]["mdt"]:
        error_log(data["output"]["mdt"], mdt, "mdt")
        success = False


    if not success:
        return False
    else:
        return True

def error_log(expected, received, string):
    print(f"\tIncorrect {string}:")
    print(f"\t\tExpected {string}: {expected}")
    print(f"\t\tRecieved {string}: {received}")

if __name__ == "__main__":
    with open("tests/assembler_tests/pass1_tests.json", "r") as f:
        test_data = json.load(f)
        run("Pass_1", test_data, pass1_test)
