def superN(n):
	def check(s):
		if s == n:
			print(f"{n} is supernumber")
			return True
		elif s > N:
			print(f"{n} is not super number")
			return False
		if s%2==0:
			s +=1
			check(s)
		else:
			s = 2*s
			check(s)
	return check

if __name__=='__main__':
    i=superN(255)
    i(1)
