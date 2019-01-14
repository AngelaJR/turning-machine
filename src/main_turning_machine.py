"""
This program simulates a truning machine in which
the righ side of the tape is infinite...

Created by: Angela Raymond.
"""

""""
This method eads the text file and  modifies the text file
by saving the instructions into a dictionary
and saves the initial and accepting state in variables
"""
def getMachineInstructions():
    f = input("Enter file name: ")  #ask user for input
    file = open(f, 'r')             #open file

    lines = [line.strip() for line in file] #read file line by line and save it to a list
    lines[:] = [item for item in lines if item != ''] #remove empty strings from list

    ini_state = (lines[1].split(" "))[1]    #get initial state
    accepting = (lines[2].split(" "))[1]    #get accepting state

    #remove the first elements in list
    n = 3
    instructions = lines[n:]

    #iterate through list and save in into a dictionary
    i = iter(instructions)
    dictionary = dict(zip(i, i))

    #change keys and values in dictionary to tuplets
    machine_instructions = {tuple(k.split(",")):dictionary[k] for k, v in dictionary.items()}
    for k, v in machine_instructions.items():
        machine_instructions[k] = tuple(v.split(","))

    main(ini_state, accepting, machine_instructions)

#ask user for a string to test & saves the string in a list
def usrInput(inpt):
    tape = list(inpt)
    tape.append("_")
    return tape

#start of programs afte the file has been read and modified
def main(ini_state, accepting, machine_instructions):
    while True:
        usr_inpt = input("\nEnter Input String: ")
        if usr_inpt == "quit":
            break
        else:
            tape = usrInput(usr_inpt)
            machine(ini_state, accepting, tape, machine_instructions)

#Main Method. This is what makes the turning machine work.
def machine(ini_state, accepting, tape, machine_instructions):

    #calls method machineInstruction and returns the machine steps
    machine = machine_instructions

    #variables
    reject = False
    current_state = ini_state
    accepting_state = accepting
    head = 0
    tape_string = ''.join(tape)

    print ("\n", tape_string) #print inistial tape

    #while the current state does not equal to the accepting go through machine
    while current_state != accepting_state:

        slot = tape[head]   #slot variable equls to the current symbol in the tape
        print(' ' * (head) + '^') #print locatio of the head

        #loop through the keys in dictionary, as well as the values
        for key, value in machine.items():
            machine_states = key[0] #saves the states of the machine
            read_symbol = key[1]    #saves the the symbol that may be next in the machine

            #checks if the current state and the current slot is in the machine
            # if neither of them are in the machine then go to junk state and stop machine
            if (current_state, slot) not in machine:
                reject = True
                current_state = accepting_state
                break

            else:
                #if current state and slot are in the machine then find current state
                # and slot in machine
                if machine_states == current_state and read_symbol == slot:
                    instuction = value              #save the instructions of current state
                    current_state = instuction[0]   #move to next state
                    write_symbol = instuction[1]    #overwrite current symbol in tape
                    tape[head] = write_symbol       #with new symbol
                    tape_string = ''.join(tape)     #save new tape
                    print (tape_string)             #print new tape
                    direction = instuction[2]       #move direction of head

                    #if symbol is > then move the head to the right of tape
                    if direction == ">":
                        head = head + 1
                    #if symbol is < then move the head to the left of tape
                    if direction == "<":
                        head = head - 1
                    break

    #calls method machineEnd
    machineEnd(reject)

#checks if the machine rejected or accepted the string
def machineEnd(reject):
    if reject == True:
        print ("\nReject!")
    else:
        print ("\nAccept!")


getMachineInstructions()
