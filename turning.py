class TuringMachine:
    def __init__(self, initial_state, final_states, transitions):
        self.state = initial_state
        self.final_states = final_states
        self.transitions = transitions
        self.tape = ['B']  # Blank symbol
        self.head_position = 0

    def step(self):
        if self.state in self.final_states:
            print("Reached a final state.")
            return

        current_symbol = self.tape[self.head_position]

        if (self.state, current_symbol) in self.transitions:
            new_state, new_symbol, move_direction = self.transitions[(self.state, current_symbol)]

            self.tape[self.head_position] = new_symbol
            self.state = new_state

            if move_direction == 'R':
                self.head_position += 1
                if self.head_position == len(self.tape):
                    self.tape.append('B')
            elif move_direction == 'L':
                self.head_position -= 1
                if self.head_position < 0:
                    self.tape.insert(0, 'B')

        else:
            print("No transition defined for current state and symbol.")
            return

    def run(self):
        while self.state not in self.final_states:
            self.step()

    def get_tape_contents(self):
        return ''.join(self.tape)


# Define the initial state, final states, and transitions for doubling a binary number.
initial_state = 'q0'
final_states = {'qf'}
transitions = {
    ('q0', '0'): ('q1', '0', 'R'),  # Move right and change to '0'
    ('q0', '1'): ('q1', '1', 'R'),  # Move right and change to '1'
    ('q1', '0'): ('q1', '0', 'R'),  # Continue moving right
    ('q1', '1'): ('q1', '1', 'R'),  # Continue moving right
    ('q1', 'B'): ('q2', 'B', 'L'),  # Move left to the beginning of the input
    ('q2', '0'): ('q2', '0', 'L'),  # Move left and continue
    ('q2', '1'): ('q2', '1', 'L'),  # Move left and continue
    ('q2', 'B'): ('qf', 'B', 'S'),  # Stop if blank symbol is encountered after moving left
}

# Initialize the Turing machine
tm = TuringMachine(initial_state, final_states, transitions)

# Set the input tape content
input_binary = input("Enter a binary number: ")
tm.tape = list(input_binary) + ['B'] * (len(input_binary) * 2)  # Initialize with input binary and additional space

# Run the Turing machine
tm.run()

# Output the result
doubled_binary = tm.get_tape_contents().rstrip('B')  # Remove trailing blank symbols
if doubled_binary[0] == 'B':
    doubled_binary = doubled_binary[1:]  # Remove leading blank symbol if present
print("The doubled binary number is:", input_binary + doubled_binary)

