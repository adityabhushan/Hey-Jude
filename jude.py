title = "hey jude "
hook_one = "don't "
two_one = ["make it bad ","be afraid ", "let me down "]
two_two = ["take a sad song and make it better ", "You were made to go out and get her ", "You have found her, now go and get her "]
hook_two = "remember to "
three_one = ["let her into your heart ", "let her under your skin "]
hook_three = "then you "
four_one = ["can start ", "will begin "]
four_two = "to make it better "
para_three = "And anytime you feel the pain, hey jude, refrain, \nDon't carry the world upon your shoulders. \nFor well you know that it's a fool who plays it cool\nBy making his world a little colder. \n"
para_five = "So let it out and let it in, hey jude, begin,\nYoure waiting for someone to perform with.\nAnd don't you know that it's just you, hey jude, you'll do,\nThe movement you need is on your shoulder.\n"
hook_four = "Better better better better better better, oh "
hook_five = "Na na na na na, na na na "
flag = 0
for n in range(0,3):
  if  n == 2:
		print para_three
	print title + hook_one + two_one[n] + ",\n" + two_two[n]
	if n > 1: 
		n = 0
		flag = 1
	print hook_two + three_one[n] + "\n" + hook_three + four_one[n] + four_two + "\n"
	if  flag == 1:
		n == 2
		print para_five
print title + hook_one + two_one[0] + ",\n" + two_two[0] + "\n" + hook_two + three_one[0] + "\n" + hook_three + four_one[0] + four_two + "\n\n" + hook_four + "\n" + hook_five
