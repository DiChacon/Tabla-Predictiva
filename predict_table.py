class PredictTable:
    def __init__(self):
        self.table = {
            'A': {
                'let': ['T', 'N', 'M', ';'],
                '0..9': None,
                'a...z': None,
                '[': None,
                ']': None,
                ',': None
            },
            'N': {
                'let': None,
                '0..9': None,
                'a...z': ['L', 'R'],
                '[': None,
                ']': None,
                ',': None
            },
            'R': {
                'let': None,
                '0..9': None,
                'a...z': ['L', 'R'],
                '[': ['empty'],
                ']': None,
                ',': None
            },
            'M': {
                'let': None,
                '0..9': None,
                'a...z': None,
                '[': ['[', 'E', ']'],
                ']': None,
                ',': None
            },
            'E': {
                'let': None,
                '0..9': ['D', 'C', 'X'],
                'a...z': None,
                '[': None,
                ']': None,
                ',': None
            },
            'C': {
                'let': None,
                '0..9': ['D', 'C'],
                'a...z': None,
                '[': None,
                ']': ['empty'],
                ',': ['empty']
            },
            'T': {
                'let': ['let'],
                '0..9': None,
                'a...z': None,
                '[': None,
                ']': None,
                ',': None
            },
            'L': {
                'let': None,
                '0..9': None,
                'a...z': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
                '[': None,
                ']': None,
                ',': None
            },
            'D': {
                'let': None,
                '0..9': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
                'a...z': None,
                '[': None,
                ']': None,
                ',': None
            },
            'X': {
                'let': None,
                '0..9': None,
                'a...z': None,
                '[': None,
                ']': ['empty'],
                ',': [',', 'D', 'C', 'X']
            }
        }