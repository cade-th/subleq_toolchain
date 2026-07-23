from tests.tester import run
from assembler.src.parser import Parser
import json
 
def pass2_test(test_name, data):
    print(f"Test {test_name}:")
    success = False

    parser = Parser(data["input"]["tokens"]) 

    tokens = data["input"]["tokens"]
    sym_table = data["input"]["sym_table"]
    mnt = data["input"]["mnt"]
    mdt = data["input"]["mdt"]
    
    tokens = parser.pass2(tokens, sym_table, mnt, mdt)

    if (
        not check_data("tokens", data, tokens)
    ):
        return success
    
    success = True
    return success

def check_data(string, test_data, output):
    if output != test_data["output"][string]:
        error_log(test_data["output"][string], output, string) 
        return False
    else:
        return True

def error_log(expected, received, string):
    print(f"\tIncorrect {string}:")
    print(f"\t\tExpected {string}: {expected}")
    print(f"\t\tRecieved {string}: {received}")

if __name__ == "__main__":
    with open("tests/assembler_tests/pass2_tests.json", "r") as f:
        test_data = json.load(f)
        run("Pass_2", test_data, pass2_test)
