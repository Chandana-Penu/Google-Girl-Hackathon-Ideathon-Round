# Fault Identification in digital chips

This code requires Python 3 to run. No additional libraries are required. 

The input needs to be given in the form of two `.txt` files, namely,

- `circuit.txt`, containing the logical circuit desciption in the form of sequential boolean logical expressions. For example, the circuit descibed in the problem document will be described as follows,

    > net_e = A & B\
    > net_f = C | D\
    > net_g = ~ net_f\
    > Z = net_g ^ net_e

- `fault.txt`, containing the fault location and type, in the following format (problem document example),

    > FAULT_AT = net_f\
    > FAULT_TYPE = SA0

These files need to be included in the same folder as the main python file `main.py`.

All the input vectors resulting in faulty outputs, along with the corresponding faulty output will be written into a new file `output.txt`, in the following format,
    
> [A, B, C, D] = [`A`, `B`, `C`, `D`], Z = `Z`

where `A`, `B`, `C`, `D` and `Z` are appropriate bits.