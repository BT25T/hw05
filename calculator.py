calculate = lambda a, operator, b : a+b if operator == '+' else a-b if operator == '-' else a*b if operator == '*' else a/b if operator == '/' and b != 0 else None; main = lambda : ([print(f"Result: {r}\n" if r is not None else "Cannot calculate that\n") for a in iter(lambda: input("First number (or q): "), "q") for op in [input("Operator (+ - * /): ")] for b in [float(input("Second number: "))] for r in [calculate(float(a), op, b)]],print("the program stops\n"))

if __name__ == "__main__":
    main()