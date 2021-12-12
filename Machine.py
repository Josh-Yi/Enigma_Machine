from Rotor import ROTOR

class MACHINE():
    def __init__(self, r1, r2, r3, rf):
        self.r1 = ROTOR(r1)
        self.r2 = ROTOR(r2)
        self.r3 = ROTOR(r3)
        self.rf = ROTOR(rf)
        self.counter = 0
        self.key_map = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                        'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    def machine_state_update(self):
        self.counter += 1
        self.r1.state_update()
        if (self.counter % 26 == 0) & (self.counter > 1):
            self.r2.state_update()
            if (self.counter % 26 ** 2) == 0 & (self.counter > 1):
                self.r3.state_update()

    def encode(self, code_letter):
        # self.machine_state_update()
        num = self.key_map.index(code_letter)
        x = self.r1.go_in(num)
        x = self.r2.go_in(x)
        x = self.r3.go_in(x)
        x = self.rf.go_in(x)
        x = self.r3.go_back(x)
        x = self.r2.go_back(x)
        x = self.r1.go_back(x)
        self.machine_state_update()
        return self.key_map[x]
