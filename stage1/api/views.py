from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view['GET']
def get(request):
    return Response(
        {
            "slack_name": "Mojolajah Adekunle",
            "current_day": "Tuesday",
            "utc_time": "2023-09-12T11:03:05Z",
            "track": "backend",
            "github_file_url": "",
            "github_repo_url": "https://github.com/mj-ad/stage1",
            "status_code": 200
        })