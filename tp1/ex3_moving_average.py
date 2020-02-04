def moving_average_1(nb_list, n):
	"""Computes the mean of l on a window of size n
	
	nb_list: list of numerical values
	n: positive integer
	"""
	len_result = len(nb_list) - n + 1
	result = []
	for i in range(len_result):
		s = 0.0
		for j in range(i, i+n):
			s = s + nb_list[j]
		result.append(s / n)
	return result


def moving_average_2(nb_list, n):
	"""Computes the mean of l on a window of size n
	
	nb_list: list of numerical values
	n: positive integer
	"""
	len_result = len(nb_list) - n + 1
	result = []
	for i in range(len_result):
		result.append(sum(nb_list[i:i+n]) / n)
	return result


if __name__ == "__main__":
	nb_list = [2, 3, 5, 7, 11, 13, 15, 17]
	a = moving_average_1(nb_list, 3)
	print(a)
