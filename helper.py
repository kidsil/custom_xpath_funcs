def xpath_func_tokenize(context, string, split_token):
	if type(string) is list:
		string = string[0]
	return string.split(split_token)
def xpath_func_make_title(context, string):
	if type(string) is list:
		string = string[0]
	return string.title()
