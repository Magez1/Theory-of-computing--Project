class TuringMachine:
    def __init__(self, states, alphabet, transitions, start_state, accept_state, reject_state):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.current_state = start_state
        self.start_state = start_state
        self.accept_state = accept_state
        self.reject_state = reject_state
        self.tape = []
        self.head_position = 0

    def reset(self):
        self.current_state = self.start_state
        self.tape = []
        self.head_position = 0

    def step(self, symbol):
        if (self.current_state, symbol) in self.transitions:
            new_state, new_symbol, direction = self.transitions[(self.current_state, symbol)]
            self.tape[self.head_position] = new_symbol
            self.current_state = new_state
            if direction == 'R':
                self.head_position += 1
                if self.head_position >= len(self.tape):
                    self.tape.append(' ')
            elif direction == 'L':
                self.head_position -= 1
                if self.head_position < 0:
                    self.tape.insert(0, ' ')
                    self.head_position = 0
        else:
            self.current_state = self.reject_state

    def run(self, input_string):
        self.reset()
        self.tape = list(input_string)
        self.tape.append(' ')
        while self.current_state != self.accept_state and self.current_state != self.reject_state:
            self.step(self.tape[self.head_position])
        return self.current_state == self.accept_state

def check_turing_recognizable(tm, input_string):
    if tm.run(input_string):
        return "Turing Recognizable"
    else:
        tm.reset()
        if tm.run(complement(input_string)):
            return "Co-Turing Recognizable"
        else:
            return "Neither"

def complement(string):
    
    pass


states = {'q0', 'q1', 'qa', 'qr'}
alphabet = {'0', '1', ' '}
transitions = {
    ('q0', '0'): ('q1', '1', 'R'),
    ('q1', '1'): ('qa', '1', 'R')
}
start_state = 'q0'
accept_state = 'qa'
reject_state = 'qr'

tm = TuringMachine(states, alphabet, transitions, start_state, accept_state, reject_state)
input_string = "01"
result = check_turing_recognizable(tm, input_string)
print(f"The language is {result}")
