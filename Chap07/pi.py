from math import *

def estimate_pi(n):
	k = 0
	pi_est = 0
	new_term = 1
	const = 2*sqrt(2) / 9801
	while new_term > 1e-15:
		num = factorial(4*k)*(1103 + 26390*k)
		den = factorial(k)**4 * 396**(4*k)
		new_term = const * num / den
		k += 1
		pi_est = pi_est + new_term
	return 1/pi_est

print estimate_pi(3)

