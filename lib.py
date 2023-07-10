from multiprocessing import cpu_count
from concurrent.futures import ProcessPoolExecutor, as_completed
import time


def single_process_function(sleep_time: int) -> int:
    print("Sleeping for %d seconds", sleep_time)
    time.sleep(sleep_time)
    return sleep_time


def function_using_pool(times: list[int]) -> list[int]:
    results = []
    print("Starting ProcessPoolExecutor")
    with ProcessPoolExecutor(max_workers=cpu_count()) as executor:
        print("Sending jobs")
        jobs = {
            (executor.submit(single_process_function, time)): time for time in times
        }
        for job_instance in as_completed(jobs):
            print("Completed job with sleep %d", jobs[job_instance])
            results.append(job_instance.result())
    print("Getting back results ", results)
    return results


if __name__ == "__main__":
    function_using_pool()
