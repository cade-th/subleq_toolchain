from emu.src.cpu import Cpu
from test_utils import error_log

 
def emu(test_name, data):
    #print(f"Test {test_name}:")
    success = False

    cpu = Cpu() 
    cpu.ram = data["input"]["ram"]
    cpu.subleq()

    if cpu.ram != data["output"]["ram"]:
        error_log(test_name, data["output"]["ram"], cpu.ram, "ram")
        return success
    if cpu.pc != data["output"]["pc"]:
        error_log(test_name, data["output"]["pc"], cpu.pc, "pc")
        return success

    success = True
    return success


