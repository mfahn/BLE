from ast import Num

#order first, <loop start> second, count, third, number, fourth </endloop>, fifth

First = "<macro name=\"PWCrack\" icon=\"SNAKE\"><assert-service description=\"Ensure 6834636b-6d33-4c31-3668-744275314221 service\" uuid=\"6834636b-6d33-4c31-3668-744275314221\"><assert-characteristic description=\"Ensure 6834636b-6d33-4c31-3668-744275314203 characteristic\" uuid=\"6834636b-6d33-4c31-3668-744275314203\"><property name=\"WRITE\" requirement=\"MANDATORY\"/></assert-characteristic></assert-service>"
Second="<write description=\""

Third = "\" characteristic-uuid=\"6834636b-6d33-4c31-3668-744275314203\" service-uuid=\"6834636b-6d33-4c31-3668-744275314221\" value=\"BE"

Fourth = "01FF\" type=\"WRITE_REQUEST\"/>"
Fifth="</macro>"

first_count = 0
second_count = 0
third_count = 0
num = 0

with open('output.xml', 'w') as file:
    file.write(First)

    #iterate first two hex digits
    for first_count in range(10):
        #iterate second two hex digits
        for second_count in range(10):
            #iterate third two hex digits
            for third_count in range(10):
                if(int(str(first_count) + str(second_count) + str(third_count)) < 110):
                    if(int(str(first_count) + str(second_count) + str(third_count)) < 10):
                        num = '00' + hex(first_count).lstrip("0x") + '0' + hex(second_count).lstrip("0x") + '00' + hex(third_count).lstrip("0x")
                        if(int(str(first_count) + str(second_count) + str(third_count)) == 0):
                            num = '00' + hex(first_count).lstrip("0x") + '00' + hex(second_count).lstrip("0x") + hex(third_count).lstrip("0x") + '00'

                    #elif((int(str(first_count) + str(second_count) + str(third_count)) % 10 == 0) & (first_count == 0)):
                     #   num = '00' + hex(first_count).lstrip("0x") + '0' + hex(second_count).lstrip("0x") + hex(third_count).lstrip("0x") + '0'

                    elif((int(str(first_count) + str(second_count) + str(third_count)) % 10 == 0)):
                        num = '0' + hex(first_count).lstrip("0x") + '00' + hex(second_count).lstrip("0x") + '0' + hex(third_count).lstrip("0x") + '0'

                    else:
                        num = '0' + hex(first_count).lstrip("0x") + '00' + hex(second_count).lstrip("0x") + '0' + hex(third_count).lstrip("0x")

                elif((int(str(first_count) + str(second_count) + str(third_count)) >= 110)):
                    if((int(str(first_count) + str(second_count) + str(third_count)) % 10 == 0) & (second_count == 0) & (third_count == 0)):
                        num = '0' + hex(first_count).lstrip("0x") + '0' + hex(second_count).lstrip("0x") + '0' + hex(third_count).lstrip("0x") + '00'

                    elif(int(str(first_count) + str(second_count) + str(third_count)) % 10 == 0):
                        num = '0' + hex(first_count).lstrip("0x") + '0' + hex(second_count).lstrip("0x") + '0' + hex(third_count).lstrip("0x") + '0'

                    elif((int(str(first_count) + str(second_count) + str(third_count)) % 10 != 0) & (second_count == 0)):
                        num = '0' + hex(first_count).lstrip("0x") + '0' + hex(second_count).lstrip("0x") + '00' + hex(third_count).lstrip("0x")

                    else:
                        num = '0' + hex(first_count).lstrip("0x") + '0' + hex(second_count).lstrip("0x") + '0' + hex(third_count).lstrip("0x")

                print(num, len(num), str(first_count)+str(second_count)+str(third_count))


                file.write(Second)

                #this writes to nrfConnect, it should be the actual number, not a garbled mess like num
                track = str(first_count) + str(second_count) + str(third_count)

                file.write(track)
                file.write(Third)

                #this is the value that is being written. It must have the prefix and suffix
                file.write(num)
                file.write(Fourth)

            third_count = 0

        second_count = 0

    file.write(Fifth)