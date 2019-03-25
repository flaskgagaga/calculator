pat = ['+', '-', '*', '/', '(', ')', '%','^']

#转换为逆波兰
def reverse_polish(data):

	'''
	首先维护两个空栈，（stack_exp）存逆波兰表达式，(stack_ops)暂存操作符，
	运算结束后stack_ops必为空循环遍历data(将表达式分为四种元素  
	1、数值; 2、操作符; 3、 左括号; 4、右括号)，具体情况如下：

	1、遇到数值， 将该值入栈stack_exp

	2、遇到左括号， 将左括号入栈stack_ops

	3、遇到右括号，将stack_ops中的操作符从栈顶依次出栈并入栈stack_exp,
		直到第一次遇到左括号终止操作（注意： 该左括号出栈stack_ops但不入栈stack_exp）
		至此消除表达式中的一对括号

	4、遇到四则运算操作符号（+ - * /）

		 4-1、 如果stack_ops为空， 操作符入栈stack_ops

		 4-2、 如果stack_ops不空，将stack_ops栈顶操作符与遍历到的操作符(op)比较：

				4-2-1： 如果stack_ops栈顶操作符为左括或者op优先级高于栈顶操作符优先级， o
					p入栈	 stack_ops，当前遍历结束

				4-2-2： 如果op优先级小于或者等于stack_ops栈顶操作符，
					stack_ops栈顶操作符出栈并入栈	 stack_exp，重复4-1、 4-2直到op入栈stack_ops

	5、data遍历结束后如果stack_ops栈不为空，则依次将操作符出栈并入栈stack_exp
	'''
	stack_ops = list()
	#数字栈
	stack_exp = list()
	#优先级
	dicts = {'+' : 1, '-' : 1, '*' : 2, '/' : 2, '(' : 0, '^':3}
	
	global pat
	
	for index in data:
		#1.数字，进exp栈
		if index not in pat:
			stack_exp.append(index)
		
		#2.非数字
		else:
			#2.1 ops栈空
			if	not stack_ops:
				stack_ops.append(index)
			#2.2 ops栈非空
			else:
				#2.2.1 index 是 左括号 ,入栈ops
				if index == '(':
					stack_ops.append(index)
				#2.2.2 index 是右括号,将栈顶的操作符出ops栈，并入exp栈 ，直到遇到左括号
				elif index == ')':
					while True:
						newdex = stack_ops.pop()
						#2.2.2.1 newdex是操作符
						if newdex != '(':
							stack_exp.append(newdex)
						#2.2.2.2 newdex 是左括号
						else:
							break
				#2.2.3 index是普通操作符
				else:
					while True:
						#2.2.3.0 ops栈空，则直接入栈
						if not stack_ops:
							stack_ops.append(index)
							break
						level_index = dicts[index]
						level_ops = dicts[stack_ops[-1]]
						#2.2.3.1 index 优先级 比 ops 栈顶优先级 高 ,index 入 ops栈
						if level_index > level_ops:
							stack_ops.append(index)
							break
						#2.2.3.2 index 优先级 比 ops 栈顶优先级 低或等于 , ops栈顶 出栈 并 入exp 栈，直到 index 优先级 高于 ops 栈顶优先级
						else:
							topdex = stack_ops.pop()
							stack_exp.append(topdex)
	#3. data 原表达式 已被遍历完，若ops 栈不为空，则依次出栈 进 exp栈
	while True:
		if len(stack_ops) != 0:
			dex = stack_ops.pop()
			stack_exp.append(dex)
		else:
			break
	return stack_exp
	
# 对逆波兰式求值
def compute(data):


	'''
	初始化一个数值栈stack_res,用于存放中间数值以及计算结果

	遍历data：

	1、如果遇到数字，入栈stack_res;

	2、如果遇到运算符， 从stack_res中依次出栈两个数（先出栈的在右， 后出栈的在左 ）连同遍历到的运算符组成二目运算，求值后将结果压栈stack_res；

	3、 继续遍历下一个元素，直到结束；
	'''
	stack_res = list()
	
	global pat
	
	for index in data:
		#1 数字，进res栈栈
		if index not in	 pat:
			stack_res.append(index)
		#2 运算符
		else:
			# 2.1 左右操作数
			right_ops = stack_res.pop()
			left_ops = stack_res.pop()
			
			if index == '*':
				res = left_ops*right_ops
				stack_res.append(res)
				
			if index == '/':
				res = left_ops/right_ops
				if right_ops == 0:
					raise Exception('Zero')
				stack_res.append(res)
				
			if index == '+':
				res = left_ops+right_ops
				stack_res.append(res)
				
			if index == '-':
				res = left_ops-right_ops
				stack_res.append(res)
				
			if index == '^':
				res =1
				for i in range(0,int(right_ops)):	
					res = left_ops*res
				stack_res.append(res)
				
	if len(stack_res) == 1:
		return stack_res[0]
		

	
if __name__ == '__main__':
	mydata = [2, '*', '(', 2, '+', 3, ')', '/', 2]
	rpn_data = reverse_polish(mydata)
	res = compute(rpn_data)
	print(b)
	
	
	
	
	
	
	