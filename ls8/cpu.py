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
        self.MUL = 0b10100010
        self.running = True

    def load(self,filename):
        """Load a program into self.ram."""
        
     
        try:
            address = 0
            with open(filename) as f:
                for line in f:
                    # Split before and after any comment symbols
                    comment_split = line.split("#")
                    num = comment_split[0].strip()
                    # Ignore blanks
                    if num == "":
                        continue

                    value = int(num,2)
                    self.ram[address] = value
                    address += 1

        except FileNotFoundError:
            print(f"{sys.argv[0]}: {sys.argv[1]} not found")
            sys.exit(2)

        if len(sys.argv) != 2:
            print("usage: simple.py <filename>", file=sys.stderr)
            sys.exit(1)

     



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
                instruction_a = self.ram_read(self.pc + 1)
                instruction_b = self.ram_read(self.pc + 2)

            except IndexError:
                print("register instruction out of range")
            

           

            if ir == self.LDI:
                print("LDI")
                reg_address = instruction_a
                data = instruction_b
                self.reg_write(data,reg_address)


            elif ir == self.PRN:
                print("PRINT")
                data = self.reg_read(instruction_a)
                print(data)

            elif ir == self.MUL:
                register_a = self.reg_read(instruction_a)
                register_b = self.reg_read(instruction_b)
                self.reg_write(register_a*register_b,instruction_a)
                print("MUL")
                

            elif ir == self.HLT:
                print("HLT")
                
                self.running = False
            
            #go to next instruction based of of two high bits of current instruction in IR
            #you many need custom jump numbers based on OP CODE
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


    #load CLI

    
