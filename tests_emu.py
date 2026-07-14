from tests.tester import run
from emu.src.cpu import Cpu
import json
 
def emu_test(test_name, data):
    print(f"Test {test_name}:")
    success = False

    cpu = Cpu() 
    cpu.ram = data["input"]["ram"]
    cpu.subleq()

    if cpu.ram != data["output"]["ram"]:
        error_log(data["output"]["ram"], cpu.ram, "ram")
        return success
    if cpu.pc != data["output"]["pc"]:
        error_log(data["output"]["pc"], cpu.pc, "pc")
        return success

    success = True
    return success

def error_log(expected, received, string):
    print(f"\tIncorrect {string}:")
    print(f"\t\tExpected {string}: {expected}")
    print(f"\t\tRecieved {string}: {received}")

if __name__ == "__main__":
    with open("tests/emu_tests/emu_tests.json", "r") as f:
        test_data = json.load(f)
        run("Emulator", test_data, emu_test)


