# Use the superfacility API to interact with NERSC

## Token authentication
- To get a token, please check the readme file in the main page. 
- When using the API, you need to authenticate yourself. The API uses token authentication. The IP address of the client is used to determine the user. For testing I am using `JIRIAF2302` whose IP address is `129.57.178.20`.
- The token is not uploaded to github. Manually copy the files to the `sf-api/key/red` folder.`

## Basic usage
### Execute commands
Please check the functions `run_cmd` in `sf-api/example.py`. To check the status of the job, insert the `task_id` to the function `read_api_result`. Notice that there will be a delay between the execution and the return of the results. 


### Submit Slurm jobs
To submit a slurm job, please check the function `submit_slurm_job` in `sf-api/example.py`. The job script should be prepared in advance. To check the status of the job, insert the `task_id` to the function `read_api_result`.






