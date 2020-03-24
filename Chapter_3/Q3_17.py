class Greetings:
    def __init__(self, name):
        self.name = name

    def __getattr__(self, attr):
        allowed = ['hello', 'wake_up', 'good_morning', 'good_afternoon',
                   'good_evening', 'nice_to_meet_you', 'good_night']

        def call(name=None):
            if attr in allowed:
                greeting = attr.replace('_', ' ')
                name = name or self.name

                print(f'{greeting.capitalize()}, {name}.')
            else:
                msg = f'name: {name}, greeting: {attr}'
                raise ValueError(f'Invalid name or greeting. {msg}')

        return call


greeting = Greetings('Link')
greeting.wake_up()  # 出力は　"""①"""
greeting.hello(name='Princess')  # 出力例は　"""②"""
greeting.nice_to_meet_you(name='Mister Bond')  # 出力は　"""③"""
greeting.hi()  # 出力は　"""④"""
