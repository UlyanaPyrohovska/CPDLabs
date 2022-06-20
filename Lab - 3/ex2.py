if __name__ == '__main__':
    n = 10000
    with open('outBig.bin', 'wb') as file:
        for i in range(n):
            file.write(i.to_bytes(4, byteorder='big', signed=False))
        with open('outLittle.bin', 'wb') as file:
            for i in range(n):
                file.write(i.to_bytes(4, byteorder='little', signed=False))
# Say what the i.to_bytes instruction does and explain the difference between byteorder='big' and
# byteorder='little'

# Answer: i.to_bytes instruction transforms an int into specified bytes (in this case 4) into hexadecimal
# byteorder='big' orders the array to convert from an int to bytes, where the most significant byte is stored
# at the beginning and the least significant at the end.
# byteorder ='little' - most significant byte is stored at the end and least at the beginning

# Task: Explain what the program does

# Answer: The program creates two files, outBig and outLittle, and then transforms
# and writes the numbers from 0 to n (10000)

# Task: Open the outBig.bin and outLittle.bin files and check how the
# integers. Access the HexEd.it website to open the files and, in the settings menu, change the
# number of bytes per line to 4. Check how the number 1024 is represented in
# each of the files.

# outBig.bin -    00 00 04 00
# outLittle.bin - 00 04 00 00

