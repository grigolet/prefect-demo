from prefect import flow
import lib


@flow(name="Run function using pool", log_prints=True)
def flow_function_using_pool(times: list[int]):
    print("Preparing flow")
    result = lib.function_using_pool(times)
    print("Flow terminated with result %s", result)
    return result
