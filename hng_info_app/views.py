from django.http import JsonResponse
from datetime import datetime
import pytz

def get_info(request):
    # Get query parameters
    slack_name = request.GET.get('slack_name')
    track = request.GET.get('track')

    # Validate track format
    if track != "backend":
        return JsonResponse({
            "error": "Invalid track format. Should be 'backend'",
            "status_code": 400
        })

    # Get current day of the week and UTC time
    utc_now = datetime.now(pytz.UTC)
    current_day_of_week = utc_now.strftime("%A")
    current_utc_time = utc_now.strftime("%Y-%m-%dT%H:%M:%SZ")

    # GitHub URLs
    github_file_url = "https://github.com/BrodaOJ56/HNG_INTERNSHIP_TASK/blob/master/hng_info_app/views.py"
    github_repo_url = "https://github.com/BrodaOJ56/HNG_INTERNSHIP_TASK"

    # Check for required fields
    if not slack_name or not current_day_of_week or not current_utc_time or not github_repo_url:
        return JsonResponse({
            "error": "Missing required field(s)",
            "status_code": 400
        })

    # Response data
    response_data = {
        "slack_name": slack_name,
        "current_day": current_day_of_week,
        "utc_time": current_utc_time,
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": 200
    }

    return JsonResponse(response_data)
