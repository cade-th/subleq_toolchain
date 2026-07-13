class Cpu:
    def __init__(self):
        self.pc = 0
        self.ram = []
    
    def subleq(self):

        a_addr = self.ram[self.pc]
        b_addr = self.ram[self.pc + 1]
        c_addr = self.ram[self.pc + 2]
        
        sub = self.ram[b_addr] - self.ram[a_addr]
        self.ram[b_addr] = sub

        if sub <= 0:
            self.pc = c_addr
        else:
            self.pc += 3
