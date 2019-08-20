"""CPU functionality."""

import sys

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0] * 256
        self.reg = [0] * 8
        self.pc = 0
        self.HLT = 0b00000001
        self.LDI = 0b10000010
        self.PRN = 0b01000111
        self.running = True

    def load(self):
        """Load a program into memory."""

        address = 0

        # For now, we've just hardcoded a program:

        program = [
            # From print8.ls8
            0b10000010, # LDI R0,8
            0b00000000,
            0b00001000,
            0b01000111, # PRN R0
            0b00000000,
            0b00000001, # HLT
        ]

        for instruction in program:
            self.ram[address] = instruction
            address += 1



    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
            
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        
        while self.running:
            #read program counter(PC) address into instruction register(IR)
            ir = self.ram_read(self.pc)
            print("Instruction",ir)

            
          
            try:
            #read next two instructions in case they are needed
                operand_a = self.ram_read(self.pc + 1)
                operand_b = self.ram_read(self.pc + 2)

            except IndexError:
                print("register operand out of range")
            

           

            if ir == self.LDI:
                print("LDI")
                reg_address = operand_a
                data = operand_b
                self.reg_write(data,reg_address)


            elif ir == self.PRN:
                print("PRINT")
                data = self.reg_read(operand_a)
                print(data)
                

            elif ir == self.HLT:
                print("HLT")
                
                self.running = False
            
            #go to next instruction based of of two high bits of current instruction in IR
            next_instruction = self.pc + ir >>6
            if next_instruction >= 1:

                self.pc += next_instruction + 1
            
            else:
                self.pc += 1
            
            # print(f"program counter is {self.pc}"

            


        """Run the CPU."""
        

    def ram_read(self,mar):
        return self.ram[mar]

    def ram_write(self,mdr,mar):
        self.ram[mar] = mdr


    def reg_read(self,ra):
        return self.reg[ra]

    def reg_write(self,rd,ra):
        self.reg[ra] = rd
