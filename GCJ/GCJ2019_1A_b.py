# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051635/0000000000104f1a
import sys
t, n, g = map(int, input().split())

# t num of test case
# n num of night
# g upper limit of num gopher

if (n == 365):
	#test set 1
	for _ in range(t):

		attempt = [17] * 18
		str_attempt = ' '.join(map(str,attempt))
		print(str_attempt)
		sys.stdout.flush()

		mod17 = sum(map(int, input().split()))
		mod17 %= 17

		attempt = [13] * 18
		str_attempt = ' '.join(map(str,attempt))
		print(str_attempt)
		sys.stdout.flush()

		mod13 = sum(map(int, input().split()))
		mod13 %= 13

		findmyanswer = False

		for i in range(g+1):
			if (i % 17 == mod17 and i % 13 == mod13):
				print(i)
				sys.stdout.flush()
				findmyanswer = True
				break

		if (findmyanswer ==False):
			print ("something wrong")
			exit() #something wrong


		response = int(input())
		if response == -1:
			exit()

else:
	#test set 2
	for _ in range(t):

		attempt = [18] * 18
		str_attempt = ' '.join(map(str,attempt))
		print(str_attempt)
		sys.stdout.flush()

		mod18 = sum(map(int, input().split()))
		mod18 %= 18

		attempt = [17] * 18
		str_attempt = ' '.join(map(str,attempt))
		print(str_attempt)
		sys.stdout.flush()

		mod17 = sum(map(int, input().split()))
		mod17 %= 17

		attempt = [13] * 18
		str_attempt = ' '.join(map(str,attempt))
		print(str_attempt)
		sys.stdout.flush()

		mod13 = sum(map(int, input().split()))
		mod13 %= 13

		attempt = [11] * 18
		str_attempt = ' '.join(map(str,attempt))
		print(str_attempt)
		sys.stdout.flush()

		mod11 = sum(map(int, input().split()))
		mod11 %= 11

		attempt = [7] * 18
		str_attempt = ' '.join(map(str,attempt))
		print(str_attempt)
		sys.stdout.flush()

		mod7 = sum(map(int, input().split()))
		mod7 %= 7

		attempt = [5] * 18
		str_attempt = ' '.join(map(str,attempt))
		print(str_attempt)
		sys.stdout.flush()

		mod5 = sum(map(int, input().split()))
		mod5 %= 5


		findmyanswer = False

		for i in range(mod18, 1000000+18, 18):

			if (i % 17 == mod17 and i % 13 == mod13 and i % 11 == mod11 and i % 7 == mod7 and i % 5 == mod5):
				print(i)
				sys.stdout.flush()
				findmyanswer = True
				break

		if (findmyanswer ==False):
			print ("something wrong")
			exit() #something wrong


		response = int(input())
		if response == -1:
			exit()

