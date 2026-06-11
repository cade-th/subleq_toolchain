from tester import run
import json
 
def emu_test(test_name, data):
    success = False
    return success

if __name__ == "__main__":
    with open("emu/emu_test_data.json", "r") as f:
        test_data = json.load(f)
        run("Emulator Tests", test_data, emu_test)


