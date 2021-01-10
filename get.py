import json
import facebook

def main():
	token = "EAADiwW3e6YoBADa9AFvlDPX1greaqIedPKSqzZBuC0cgTyR0nphzbv66ZAITBqK3ldzyzf0K1lzHDi2xQSvsytm5of5BtwbKIznEqq4R0MxDxi6PmbRDQXzJBMKZAz5iGr4usPf43ZCSZCmCZCk9gbywk6iCmfpavVEZBYZAjZCA4qQZBDe5n0QdjeuxD77Ujcn6NJxFkZBJ7SdbxCk4PD1oNce"
	graph = facebook.GraphAPI(token)
	
	profile = graph.get_object('me',fields='id,name')	
	
	print(json.dumps(profile, indent=4))

if __name__ == '__main__':
	main()
