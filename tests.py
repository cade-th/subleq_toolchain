import sys
import json

from test_utils import errors


RED = "\033[31m"
GREEN = "\033[32m"
RESET = "\033[0m"

from lexer_test import lexer
from emu_test import emu
from macros_test import p1_macro, p2_macro, preproc
from labels_test import p1_label, p2_label
from parser_test import parser_test

def run(suite_name, test_data, test_func):
    success = True
    count = 0

    for name, data in test_data.items():
        count += 1  
        try:
            ok = test_func(name, data)
            if not ok:
                success = False
        except Exception as err:
            print(f"Error in test {name}: {err}")
            success = False
        
    if count == 0:
        print(f"{suite_name}: No tests found")
        return False

    if success:
        print(f"{suite_name} Tests: {GREEN}PASS{RESET}")
    else:
        print("".join(errors))
        print(f"{suite_name} Tests: {RED}FAIL{RESET}")
        sys.exit(1)

    return success

test_function_dict = {
    "emu": emu,
    "lexer_test": lexer,
    "p1_macro": p1_macro,
    "p2_macro": p2_macro,
    "p1_label": p1_label,
    "p2_label": p2_label,
    "preproc": preproc,
    "parser": parser_test,
}

def run_all_tests():

    with open("./tests/emu_tests/emu_tests.json", "r") as data:
        test_data = json.load(data)
        run("emu", test_data, test_function_dict["emu"])

    with open("./tests/assembler_tests/lexer.json", "r") as data:
        test_data = json.load(data)
        run("lexer", test_data, test_function_dict["lexer_test"])

    with open("./tests/assembler_tests/p1_macro.json", "r") as data:
            test_data = json.load(data)
            run("p1 macro", test_data, test_function_dict["p1_macro"])

    with open("./tests/assembler_tests/p2_macro.json", "r") as data:
            test_data = json.load(data)
            run("p2 macro", test_data, test_function_dict["p2_macro"])

    with open("./tests/assembler_tests/preproc.json", "r") as data:
            test_data = json.load(data)
            run("preproc", test_data, test_function_dict["preproc"])

    with open("./tests/assembler_tests/p1_label.json", "r") as data:
            test_data = json.load(data)
            run("label_p1", test_data, test_function_dict["p1_label"])

    with open("./tests/assembler_tests/p2_label.json", "r") as data:
            test_data = json.load(data)
            run("label_p2", test_data, test_function_dict["p2_label"])

    with open("./tests/assembler_tests/parser.json", "r") as data:
            test_data = json.load(data)
            run("parser", test_data, test_function_dict["parser"])


if __name__ == "__main__":
    run_all_tests()
