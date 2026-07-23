from tests.tester import run
from assembler.src.parser import Parser
import json
 
def pass1_test(test_name, data):
    print(f"Test {test_name}:")
    success = False

    parser = Parser(data["input"]["tokens"]) 
    
    tokens, sym_table, mnt, mdt = parser.pass1()

    if (
        not check_data("tokens", data, tokens)
        and not check_data("sym_table", data, sym_table)
        and not check_data("mdt", data, mdt)
        and not check_data("mnt", data, mnt)
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
    with open("tests/assembler_tests/pass1_tests.json", "r") as f:
        test_data = json.load(f)
        run("Pass_1", test_data, pass1_test)
