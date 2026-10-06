import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class CourseAPIHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/api/courses":
            with open("data/courses.json", "r") as file:
                data = json.load(file)

            response = data["courses"]

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()

            self.wfile.write(
                json.dumps(response, indent=2).encode("utf-8")
            )

        else:
            self.send_response(404)
            self.end_headers()


server = HTTPServer(("0.0.0.0", 8000), CourseAPIHandler)

print("Course API running at http://localhost:8000")
server.serve_forever()
