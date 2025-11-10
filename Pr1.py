MOT = {
    'ADD': ('IS', '01'),
    'SUB': ('IS', '02'),
    'MOVER': ('IS', '04'),
    'MULT': ('IS', '03'),
    'DS': ('DL', '01'),
    'DC': ('DL', '02'),
    'START': ('AD', '01'),
    'END': ('AD', '02'),
    'LTORG': ('AD', '05'),
}

REGISTERS = {
    'AREG': '1',
    'BREG': '2',
    'CREG': '3',
    'DREG': '4'
}
def pass_two(IC, SYMTAB, LITTAB):
    MC = []
    for line in IC:
        parts = line.strip().split()
        if not parts:
            continue

        if parts[0].startswith('(AD') or parts[0].startswith('(DL'):
            continue

        opcode_token = parts[0]  
        reg_token = parts[1] if len(parts) > 1 else None
        operand_token = parts[2] if len(parts) > 2 else None

        opcode = opcode_token[4:-1]

        reg = reg_token[1] if reg_token else '0'

        if operand_token:
            if operand_token.startswith('(S'):
                sym_index = int(operand_token[3:-1])
                address = SYMTAB[sym_index][1]
                MC.append(f"{opcode} {reg} {address}")
            elif operand_token.startswith('(L'):
                lit_index = int(operand_token[3:-1])
                address = LITTAB[lit_index][1]
                MC.append(f"{opcode} {reg} {address}")
            else:
                MC.append(f"{opcode} {reg}")
        else:
            MC.append(f"{opcode} {reg}")

    return MC


def pass_one(assembly_code):
    LC = 0
    IC = []
    SYMTAB = []
    symbol_index_map = {}
    LITTAB = []
    literal_map = {}
    POOLTAB = [0]

    def assign_literals():
        nonlocal LC
        for i in range(POOLTAB[-1], len(LITTAB)):
            lit, addr = LITTAB[i]
            if addr == -1:
                LITTAB[i] = (lit, LC)
                LC += 1
        POOLTAB.append(len(LITTAB))

    for line in assembly_code:
        parts = line.strip().split()
        label = ''
        opcode = ''
        operands = []

        if len(parts) >= 2:
            if parts[1] in MOT:
                label = parts[0]
                opcode = parts[1]
                if len(parts) > 2:
                    operand_str = ' '.join(parts[2:])
                    operands = [op.strip() for op in operand_str.split(',')]
            else:
                opcode = parts[0]
                operand_str = ' '.join(parts[1:])
                operands = [op.strip() for op in operand_str.split(',')] if operand_str else []
        elif len(parts) == 1:
            opcode = parts[0]

        if opcode == 'START':
            LC = int(operands[0]) if operands else 0
            IC.append(f"(AD,01) (C,{LC})")

        elif opcode in ['END', 'LTORG']:
            assign_literals()
            IC.append(f"(AD,{MOT[opcode][1]})")

        elif opcode in MOT:
            opcode_type, opcode_code = MOT[opcode]
            if label:
                if label not in symbol_index_map:
                    symbol_index_map[label] = len(SYMTAB)
                    SYMTAB.append((label, LC))
                else:
                    idx = symbol_index_map[label]
                    SYMTAB[idx] = (label, LC)

            if opcode_type == 'IS':
                reg = '0'
                op = ''
                if len(operands) >= 2:
                    reg = REGISTERS.get(operands[0], '0')
                    operand = operands[1]
                    if operand.startswith('='):
                        if operand not in literal_map:
                            literal_map[operand] = len(LITTAB)
                            LITTAB.append((operand, -1))
                        index = literal_map[operand]
                        op = f"(L,{index})"
                    else:
                        if operand not in symbol_index_map:
                            symbol_index_map[operand] = len(SYMTAB)
                            SYMTAB.append((operand, -1))
                        index = symbol_index_map[operand]
                        op = f"(S,{index})"
                    IC.append(f"({opcode_type},{opcode_code}) ({reg}) {op}")
                elif len(operands) == 1:
                    reg = REGISTERS.get(operands[0], '0')
                    IC.append(f"({opcode_type},{opcode_code}) ({reg})")
                LC += 1

            elif opcode_type == 'DL':
                if opcode == 'DS':
                    size = int(operands[0])
                    IC.append(f"({opcode_type},{opcode_code}) (C,{size})")
                    LC += size
                elif opcode == 'DC':
                    const = operands[0]
                    IC.append(f"({opcode_type},{opcode_code}) (C,{const})")
                    LC += 1

        elif label and not opcode:
            if label not in symbol_index_map:
                symbol_index_map[label] = len(SYMTAB)
                SYMTAB.append((label, LC))

    return IC, SYMTAB, LITTAB, POOLTAB



assembly_code = [
    "START 100",
    "MOVER AREG, ='5'",
    "ADD BREG, ALPHA",
    "SUB BREG, ='6'",
    "ALPHA DS 1",
    "LTORG",
    "END"
]

IC, SYMTAB, LITTAB, POOLTAB = pass_one(assembly_code)

print("Intermediate Code:")
for code in IC:
    print(code)

print("\nSymbol Table:")
for symbol, addr in SYMTAB:
    print(f"{symbol}: {addr}")

print("\nLiteral Table:")
for literal, addr in LITTAB:
    print(f"{literal}: {addr}")

print("\nPool Table:")
print(POOLTAB)

mc = pass_two(IC, SYMTAB, LITTAB)
print("The machine code for the assembly code is: ")
for line in mc:
    print(line)
