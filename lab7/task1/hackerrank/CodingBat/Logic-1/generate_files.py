for i in range(1, 13):
    filename = f"{i}.py"
    with open(filename, "w") as file:
        file.write("# ddilnaz\n")
    print(f"Generated file: {filename}")
