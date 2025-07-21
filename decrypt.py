import base64
import itertools

def generate_case_variations(s):
    # Find positions of alphabetic characters
    letter_positions = [i for i, c in enumerate(s) if c.isalpha()]
    num_letters = len(letter_positions)
    
    # Generate all combinations of upper/lower for the letters
    for case_comb in itertools.product([str.lower, str.upper], repeat=num_letters):
        variant = list(s)
        for pos, func in zip(letter_positions, case_comb):
            variant[pos] = func(variant[pos])
        yield ''.join(variant)

# Get input string
input_str = input("Enter the input string: ")

# Generate and decode
for variant in generate_case_variations(input_str):
    # Pad if necessary
    padded = variant + '=' * ((4 - len(variant) % 4)
    try:
        decoded_bytes = base64.b64decode(padded, validate=True)
        try:
            decoded_str = decoded_bytes.decode('utf-8')
        except UnicodeDecodeError:
            decoded_str = " (non-UTF8: " + repr(decoded_bytes) + ")"
        print(f"Variant: {variant}\nDecoded bytes: {decoded_bytes}\nDecoded string: {decoded_str}\n")
    except Exception as e:
        # Optional: uncomment to show errors
        # print(f"Variant: {variant} - Error: {e}\n")
        pass
