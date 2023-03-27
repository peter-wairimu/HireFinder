#### HireFinder

HireFinder is a RESTful API that provides a way to create, update, delete and retrieve jobs. It also provides a way to create and retrieve users.

#### Getting Started

To get started with the HireFinder API, you will need to have Python 3 and pip installed on your computer. Once you have these installed, you can follow the steps below to set up and run the API:

1. Clone the repository to your computer
2. Navigate to the project directory in your terminal
3. Install the required dependencies by running the command pip install -r requirements.txt
4. Run the command python manage.py migrate to create the database tables
5. Start the development server by running the command python manage.py runserver


#### API Endpoints

The HireFinder API provides the following endpoints:

Jobs
1. GET /api/jobs/ - Retrieves a list of all jobs
2. POST /api/jobs/ - Creates a new job
3. GET /api/jobs/{job_id}/ - Retrieves a specific job by ID
4. PUT /api/jobs/{job_id}/ - Updates a specific job by ID
5. DELETE /api/jobs/{job_id}/ - Deletes a specific job by ID

#### Example Response

{
  "id": 1,

  "title": "Web Developer",

  "description": "We are looking for an experienced web developer to join our team.",

  "location": "New York, NY",

  "salary": "75000",

  "created_at": "2023-03-23T12:34:56Z",
  
  "updated_at": "2023-03-23T12:34:56Z"
}
