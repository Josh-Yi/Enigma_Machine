class ROTOR:
    def __init__(self, map_r):
        self.map_l = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                      'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.map_r = map_r

    def state_update(self):
        # map_l = self.map_l
        # map = map_l.copy()
        # map[0] = map_l[len(map_l) - 1]
        # map[1:] = map_l[:len(map_l) - 1]
        map = self.map_r[1:len(self.map_r)]
        map.append(self.map_r[0])

        self.map_r = map

    def go_in(self, idx):
        letter_in = self.map_r[idx]
        return self.map_l.index(letter_in)

    def go_back(self, idx):
        letter_in = self.map_l[idx]
        return self.map_r.index(letter_in)
