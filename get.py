import json
import facebook

def main():
	token = "EAAQUo1z5pZC4BAC9wvgz8xbI9mZCNVkvmocLyKDYQtf9eUWr6x1RuDSWdXko2TZBJpv9kSLzw69omRFvPoiGcVUW57UDpZCvc343VCLSl6UapDTIw4fE5jWVZCEKgnno8EEW2JW9PAcPj9kMX2ZCBw3u4Tef65rxjxT7RZAGd3PKw6PUXs1gt3sM8WCnniHXLZCkRZCJ7GTLgI8KlU6KhurlJQVvEfGW1S1sZD"
	graph = facebook.GraphAPI(token)
	
	profile = graph.get_object('me',fields='id,name')	
	
	print(json.dumps(profile, indent=4))

if __name__ == '__main__':
	main()
