import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class CourseAPIHandler(BaseHTTPRequestHandler):


    def do_GET(self):
        with open("data/courses.json", "r") as file:
            data = json.load(file)

        # Return all courses
        if self.path == "/api/courses":
            response = data["courses"]

        # Return one specific course
        elif self.path.startswith("/api/courses/"):
            course_id = self.path.split("/")[-1]

            response = next(
                (course for course in data["courses"]
                if course["id"] == course_id),
                None
            )

            if response is None:
                self.send_response(404)
                self.end_headers()
                return

        else:
            self.send_response(404)
            self.end_headers()
            return

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()

        self.wfile.write(
            json.dumps(response, indent=2).encode("utf-8")
        )


server = HTTPServer(("0.0.0.0", 8000), CourseAPIHandler)

print("Course API running at http://localhost:8000")
server.serve_forever()
