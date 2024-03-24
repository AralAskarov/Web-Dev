for i in range(1, 9):
    filename = f"{i}.py"
    with open(filename, "w") as file:
        file.write("#ddilnaz\n")
    print(f"Generated file: {filename}")
