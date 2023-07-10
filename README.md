# README

Clone the repo.
The deployment uses a working queue `default_work_queue`:
```bash
prefect deployment build --name flow_function_using_pool -q default_work_queue flows.py:flow_function_using_pool
```

The concurrency limit is set to 1 when applying the flow: 
```bash
prefect deployment apply --limit 1 flow_function_using_pool-deployment.yaml
```

Set the logging level to debug:
```bash
prefect config set PREFECT_LOGGING_LEVEL=DEBUG
```

Start the agent on the local machine

```bash
prefect agent start -q 'default_work_queue'
```

Start the server on a separate shell

```bash
prefect server start
```