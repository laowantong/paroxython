def print_collatz(n):  # paroxython: added_block_label...
    while n != 1:  # paroxython: suggest_constant_definition
        print(n)
        if n % 2 == 0:  # paroxython: added_label_on_line_4
            n = n // 2  # paroxython: -literal:Num -binary_operator:FloorDiv
        else:  # paroxython: unknown_label
            n = 3 * n + 1
    print(n)  # paroxython: ...added_block_label
