# Generic success response
def success_response(message="Data returned successfully", data=[]):
	return {"response_code": "100", "message": message, "results": data}


# Generic error response
def error_response(message="An error occurred", response_code='101'):
	return {"response_code": response_code, "message": message}


def validate_post_content(request):
	# Get content from User
	content = request.POST.get("content")
	
	# Check if content is available
	if not content:
		return {"error": True, "error_message": "Please provide content to post", "error_code": 101}
	