from django.http import JsonResponse
from datetime import datetime
import pytz

def get_info(request):
    # Get query parameters
    slack_name = request.GET.get('slack_name')
    track = request.GET.get('track')

    # Get current day of the week and UTC time
    utc_now = datetime.now(pytz.UTC)
    current_day_of_week = utc_now.strftime("%A")
    current_utc_time = utc_now.strftime("%Y-%m-%d %H:%M:%S UTC")

    # GitHub URLs
    github_file_url = "https://github.com/your_username/your_repo/blob/main/your_file.py"
    github_source_code_url = "https://github.com/your_username/your_repo"

    # Response data
    response_data = {
        "slack_name": slack_name,
        "current_day_of_week": current_day_of_week,
        "current_utc_time": current_utc_time,
        "track": track,
        "github_file_url": github_file_url,
        "github_source_code_url": github_source_code_url,
        "status_code": 200
    }

    return JsonResponse(response_data)
