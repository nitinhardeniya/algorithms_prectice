
class  String(object):
	"""docrtring for  String"""
	def __init__(self, arr):
		
		self.arr =list(arr)+'\0'

	def strcmp(str1,str2):
		i=0
		while str1[i]!='\0' and str2[i]!='\0':
			if str1[i]!=str2[i]:
				flag=1
				break
			i=i+1


		if flag==0 and str1[i]=='\0' and str2[i]=='\0' :
			return True
		else:
			return False

	def strcpy(self):
		s1=self.str
		s2=[]
		while s1[i]!=''
 			s2[i]=s1[i]
 			i++
 		
 		s2[i]=''

 		return s2
		

	def strlen(self):

		str=self.str
		count=0
		while str[i] !='\0':
			count=count+1

		return count