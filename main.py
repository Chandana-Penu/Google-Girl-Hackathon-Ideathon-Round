if __name__ == "__main__":
    A, B, C, D = 0, 0, 0, 0
    Z_corr = []
    Z_fault = []

    ckt_file = open("circuit.txt", 'r')
    fault_file = open("fault.txt", 'r')
    output_file = open("output.txt", 'w')

    ckt_desc = [s.strip() for s in ckt_file.readlines()]
    fault_node = fault_file.readline().split(" ")[-1].strip()
    fault_type = int(fault_file.readline()[-2].strip())

    for _ in range(16):
        for line in ckt_desc:
            line += f"\nop = {line.split(' ')[0]}\nop %= 2\nif line.split(' ')[0] == 'Z':\n\tZ_corr.append(op)"
            exec(line)

        for line in ckt_desc:
            line += f"\nop = {line.split(' ')[0]}\nop %= 2\nif line.split(' ')[0] == 'Z':\n\tZ_fault.append(op)"
            if line.split(' ')[0] == fault_node:
                exec(f"\n{line.split(' ')[0]} = {fault_type}\nif line.split(' ')[0] == 'Z':\n\tZ_fault.append(op)")
            else:
                exec(line)

        if Z_corr[-1] != Z_fault[-1]:
            # output_file.write(f"[A, B, C, D] = [{A}, {B}, {C}, {D}], expected Z = {Z_corr[-1]}, observed Z = {Z_fault[-1]}\n")
            output_file.write(f"[A, B, C, D] = [{A}, {B}, {C}, {D}], Z = {Z_fault[-1]}\n")

        A = A ^ (B & C & D)
        B = B ^ (C & D)
        C = C ^ D
        D = D ^ 1

    # print(Z_corr)
    # print(Z_fault)

    ckt_file.close()
    fault_file.close()
    output_file.close()
