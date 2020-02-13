class Time:
    def __init__(self, mins=0, secs=0):
        self.mins = mins
        self.secs = secs

    def __str__(self):
        return """"①""":"""②"""".format(self.mins, self.secs)

    def """③"""(self, to_add):
        """to_add is an integer"""
        new_time = Time()
        new_time.mins = self.mins
        new_time.secs = self.secs
        new_time.secs += to_add

        if new_time.secs """④""" 60:
          new_time.mins += new_time.secs """⑤""" 60
          new_time.secs = new_time.secs """⑥""" 60

        return new_time


print(Time(3, 5) + 122)
