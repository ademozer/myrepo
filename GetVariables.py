from javax.servlet.http import HttpServlet
class GetVariables (HttpServlet):
	def doGet(self,request,response):
		variables = "var myvar1=\"deneme\";var sessionId=\""+request.getSession().getId()+"\"";
		out = response.getWriter()
		out.println(variables)		
	def getServletInfo(self):
		return "Short Description"