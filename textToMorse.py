from time import sleep

def textToMorse(message):
	message = message.upper()
	morse = ""
	code = {	
		"A": ".-",
		"B": "-...",
		"C": "-.-.",
		"D": "-..",
		"E": ".",
		"F": "..-.",
		"G": "--.",
		"H": "....",
		"I": "..",
		"J": ".---",
		"K": "-.-",
		"L": ".-..",
		"M": "--",
		"N": "-.",
		"O": "---",
		"P": ".--.",
		"Q": "--.-",
		"R": ".-.",
		"S": "...",
		"T": "-",
		"U": "..-",
		"V": "...-",
		"W": ".--",
		"X": "-..-",
		"Y": "-.--",
		"Z": "--..",
		"0": "-----",
		"1": ".----",
		"2": "..---",
		"3": "...--",
		"4": "....-",
		"5": ".....",
		"6": "-....",
		"7": "--...",
		"8": "---..",
		"9": "----."
	}
	for ch in message:
		if ch in code:
			morse += code[ch] +  " "
		elif ch == " ":
			morse += " "
		else:
			pass
	return morse

def shortYo():
	print 'yo'

def longYo():
	print 'yoyo'

def morseToYo(morsemessage):
	for ch in morsemessage:
		if ch == ".":
			shortYo()
		elif ch == "-":
			longYo()
		else:
			print " "