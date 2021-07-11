#
#         012345678901234
parrot = "Norwegian Blue"

print(parrot[0:6:2])  # Nre
print(parrot[0:6:3])  # Nw

number = "9,223;372:036 854,775;807"
seperators = number[1::4]
print(seperators)

values = "".join(char if char not in seperators else " " for char in number).split()
print([int(val) for val in values])

###############################
###############################
# This stuff was in the video, "Slicing with Negative Numbers". The above code is the current video, "Using a Step in
# a slice".
#
# print(parrot[0:6])  # Norweg print(parrot[-14:-8])
#
# print(parrot[-4:-2])  # Bl
# print(parrot[-4:12])  # Bl

##################################################################################
##################################################################################
# This Stuff was in the Slicing video. The above code is in the current video, "Slicing with Negative Numbers".
# print(parrot[3:5])
# print(parrot[0:9])
# print(parrot[:9])
#
# # MEGA mini-challenge. The challenge is to slice the word "Blue" in the parrot string on line 3. My answer is below.
# print(parrot[10:14])  # It works!
#
# print(parrot[10:])
#
# print(parrot[:6])
# print(parrot[6:])
#
# print(parrot[:6] + parrot[6:])
#
# print(parrot[:])
#
# letters = "abcdefghijklmnopqrstuvwxyz"

# -------------------------------------------

###############################################################################
###############################################################################
# This stuff was in the past few videos. The above code is in the current video.
# print(parrot)
#
# print(parrot[3])
#
# # Time for a mini-challenge! The instructions are below as follows:
# #
# # Add some code to the program, so that it prints out <bold>we win</bold>.
# # Each character should appear on a separate line.
# # The program should get the characters from the parrot string, using indexing.
# # The w is already printed out, you just need to print out the remaining 5 characters.
# # With the text is already printed, the final output from the program should be:
# #
# # Norweigian Blue
# # w
# # e
# #
# # w
# # i
# # n
#
# # My Answer: Notice that my first "w" is missing in my answer. I didn't want to to duplicate it so, I excluded it from
# # my answer. The code to print the "w" is on line 7.
# print(parrot[4])
# print(parrot[9])
# print(parrot[3])
# print(parrot[6])
# print(parrot[8])
# # END OF CHALLENGE
#
# print()
#
# # Same challenge as before, but with negative indexing.
# print(parrot[-11])
# print(parrot[-10])
# print(parrot[-5])
# print(parrot[-11])
# print(parrot[-8])
# print(parrot[-6])
#
# print()
#
# print(parrot[3 - 14])
# print(parrot[4 - 14])
# print(parrot[9 - 14])
# print(parrot[3 - 14])
# print(parrot[6 - 14])
# print(parrot[8 - 14])
