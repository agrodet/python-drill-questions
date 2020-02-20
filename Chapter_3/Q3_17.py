class Greetings:
    def __init__(self, name):
        self.name = name

    def __getattr__(self, attr):
        allowed = ['hello', 'good_morning', 'good_afternoon', 'good_evening', 'nice_to_meet_you', 'wake_up', 'good_night']

        def call(name=None):
            if attr in allowed:
                greeting = attr.replace('_', ' ')
                name = name or self.name

                print(f'{greeting.capitalize()}, {name}.')
            else:
                raise ValueError(f'Invalid name or greeting. name: {name}, greeting: {attr}')

        return call


greeting = Greetings('Link')
greeting.wake_up()  # 出力例："""①"""
greeting.hello(name='Princess')  # 出力例："""②"""
greeting.nice_to_meet_you(name='Mister Bond')  # 出力例："""③"""
greeting.hi()  # 出力例："""④"""