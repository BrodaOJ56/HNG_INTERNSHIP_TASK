# HNG_INTERNSHIP_TASK
This project is a web-based API built using Django, designed to provide specific information in JSON format. 
It serves as a solution for the HNG Internship Task, providing users with valuable data including the Slack name, 
current day of the week, current UTC time, track, and GitHub URLs. 


## Features:

Retrieve user-specific information by providing Slack name and track as query parameters.
Returns the current day of the week and UTC time with +/-2 validation.
Includes GitHub URLs for both the file being executed and the full source code.
Delivers responses in JSON format, making it easy to integrate with other systems and applications.


## How to Use:

Make a GET request to the ``` https://hngtask-po2z.onrender.com/info/get_info/ ``` endpoint with the following query parameters:

slack_name: Your Slack name
track: Your chosen track

Example : ``` https://hngtask-po2z.onrender.com/info/get_info/?slack_name=BrodaOJ&track=Backend ```
Receive a JSON response containing the requested information, including current day and time, GitHub URLs, and more.

## How to run on Local:

1. Clone the repository:

  ```git clone https://github.com/BrodaOJ56/HNG_INTERNSHIP_TASK.git```

  ```cd HNG_INTERNSHIP_TASK```

2. Create and activate a virtual environment (optional but recommended):
 ```
  python3 -m venv venv
  ```

```
source venv/bin/activate
```

3. Install the dependencies:
```
pip install -r requirements.txt
```
4. Run the Django development server:

```python manage.py runserver ```

Access the API at ```http://127.0.0.1:8000/info/get_info/``` with appropriate query parameters.

## Contributing:

Contributions to this project are welcome! Feel free to fork the repository, make improvements, and submit pull requests.

## License:

This project is licensed under the MIT License.
