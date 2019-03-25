import tkinter #导入tkinter模块
import re
from rpn import *
root  = tkinter.Tk()
root.minsize(280,560)
root.title('计算器')


#1.界面布局
#显示面板
result = tkinter.StringVar()
result.set(0)							#显示面板显示结果1，用于显示默认数字0
result2 = tkinter.StringVar()			#显示面板显示结果2，用于显示计算过程
result2.set('')
#显示版
label = tkinter.Label(root,font = ('微软雅黑',10),bg = '#EEE9E9',bd ='9',fg = '#828282',anchor = 'se',textvariable = result2)
label.place(width = 280,height = 170)
label2 = tkinter.Label(root,font = ('微软雅黑',15),bg = '#EEE9E9',bd ='9',fg = 'black',anchor = 'se',textvariable = result)
label2.place(y = 170,width = 280,height = 60)




#数字键按钮
btn7 = tkinter.Button(root,text = '7',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda : getNum('7'))
btn7.place(x = 0,y = 285,width = 70,height = 55)
btn8 = tkinter.Button(root,text = '8',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda : getNum('8'))
btn8.place(x = 70,y = 285,width = 70,height = 55)
btn9 = tkinter.Button(root,text = '9',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda : getNum('9'))
btn9.place(x = 140,y = 285,width = 70,height = 55)

btn4 = tkinter.Button(root,text = '4',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda : getNum('4'))
btn4.place(x = 0,y = 340,width = 70,height = 55)
btn5 = tkinter.Button(root,text = '5',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda : getNum('5'))
btn5.place(x = 70,y = 340,width = 70,height = 55)
btn6 = tkinter.Button(root,text = '6',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda : getNum('6'))
btn6.place(x = 140,y = 340,width = 70,height = 55)

btn1 = tkinter.Button(root,text = '1',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda : getNum('1'))
btn1.place(x = 0,y = 395,width = 70,height = 55)
btn2 = tkinter.Button(root,text = '2',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda : getNum('2'))
btn2.place(x = 70,y = 395,width = 70,height = 55)
btn3 = tkinter.Button(root,text = '3',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda : getNum('3'))
btn3.place(x = 140,y = 395,width = 70,height = 55)
btn0 = tkinter.Button(root,text = '0',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda : getNum('0'))
btn0.place(x = 70,y = 450,width = 70,height = 55)


#运算符号按钮
btnac = tkinter.Button(root,text = 'AC',bd = 0.5,font = ('黑体',20),fg = 'orange',command = lambda :pressControl('AC'))
btnac.place(x = 0,y = 230,width = 70,height = 55)
btnback = tkinter.Button(root,text = '←',font = ('微软雅黑',20),fg = '#4F4F4F',bd = 0.5,command = lambda:pressControl('b'))
btnback.place(x = 70,y = 230,width = 70,height = 55)
btndivi = tkinter.Button(root,text = '÷',font = ('微软雅黑',20),fg = '#4F4F4F',bd = 0.5,command = lambda:getNum('/'))
btndivi.place(x = 140,y = 230,width = 70,height = 55)
btnmul = tkinter.Button(root,text ='×',font = ('微软雅黑',20),fg = "#4F4F4F",bd = 0.5,command = lambda:getNum('*'))
btnmul.place(x = 210,y = 230,width = 70,height = 55)
btnsub = tkinter.Button(root,text = '-',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda:getNum('-'))
btnsub.place(x = 210,y = 285,width = 70,height = 55)
btnadd = tkinter.Button(root,text = '+',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda:getNum('+'))
btnadd.place(x = 210,y = 340,width = 70,height = 55)
btnequ = tkinter.Button(root,text = '=',bg = 'orange',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda :pressEqual())
btnequ.place(x = 210,y = 395,width = 70,height = 55)
btnper = tkinter.Button(root,text = '.',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda:getNum('.'))
btnper.place(x = 0,y = 450,width = 70,height = 55)
btnpoint = tkinter.Button(root,text = '(',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda:getNum('('))
btnpoint.place(x = 140,y = 450,width = 70,height = 55)
btnpoint = tkinter.Button(root,text = ')',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda:getNum(')'))
btnpoint.place(x = 210,y = 450,width = 70,height = 55)
btnpoint = tkinter.Button(root,text = '^',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda:getNum('^'))
btnpoint.place(x = 210,y = 505,width = 70,height = 55)
btnpoint = tkinter.Button(root,text = 'matrix',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda:matrixUnit())
btnpoint.place(x = 0,y = 505,width = 210,height = 55)

#high-compute
# btnpoint = tkinter.Button(root,text = '(',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda:getNum('('))
# btnpoint.place(x = 0,y = 505,width = 70,height = 55)
# btnpoint = tkinter.Button(root,text = ')',font = ('微软雅黑',20),fg = ('#4F4F4F'),bd = 0.5,command = lambda:getNum(')'))
# btnpoint.place(x = 70,y = 505,width = 70,height = 55)





#获取输入
arrys = list()
pat = '[*\-+\/%\^]'
def getNum(chars):	 
	if len(arrys)==0 or (re.compile(pat).match(arrys[-1]) and re.compile(pat).match(chars))== None:
		arrys.append(chars)		   
		result.set(arrys)
		print(chars)
		
#数据处理
def tackleData():
	global arrys
	pat0 = '[*\-+\/%\(\)\^]'
	print(arrys)
	newarry = list()
	strs = ''
	for i in arrys:
		if re.compile(pat0).match(i) == None:
			strs = strs+i
		else:
			newarry.append(strs)
			newarry.append(i)
			strs=''
	newarry.append(strs)
	newarry2=list()

	for i in range(len(newarry)):
		if newarry[i] != '':
			newarry2.append(newarry[i])
	# result2.set(newarry)
	# arrys.clear()
	pat1 = ['+','-','*','/','%','(',')','^']
	for i in range(len(newarry2)):
		if newarry2[i] not in pat1:
			newarry2[i] = round((float(newarry2[i])),2)
	print(newarry2)
	result2.set(newarry2)
	arrys.clear()
	return newarry2

#控制操作
def pressControl(sign):
	global arrys
	if sign =='AC':
		arrys.clear()
		result.set(0)
	if sign =='b':
		arrys = arrys[0:-1]
		result.set(arrys)

def pressEqual():
	global arrys
	data = tackleData()
	
	#转换为逆波兰表达式
	rpn_data = reverse_polish(data)
	try:
		results = compute(rpn_data)
		print(results)
		result.set(results)
	except Exception as e:
		print(e)
		result.set(e)

#线性运算，待扩展
def matrixUnit():
	pass
	
	




root.mainloop()
