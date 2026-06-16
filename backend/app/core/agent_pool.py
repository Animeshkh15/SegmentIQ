import ray

from app.core.adk_runner import ADKRunner
from app.core.ray_manager import initialize_ray


@ray.remote
def run_agent(
    page_number: int,
    text: str
):

    print(f"Starting Agent for page {page_number}")

    runner = ADKRunner()

    result = runner.classify_page(
        page_number=page_number,
        text=text
    )

    print(f"Finished Agent for page {page_number}")

    return result

    print(f"Starting Agent for page {page_number}")

    runner = ADKRunner()

    result = runner.classify_page(
        page_number=page_number,
        text=text
    )

    print(f"Finished Agent for page {page_number}")

    return result
    
class AgentPool:

    def __init__(self):

        initialize_ray()

        self.agent_count = 5

    def classify_page(
        self,
        page_number: int,
        text: str
    ):

        tasks = [

            run_agent.remote(
                page_number,
                text
            )

            for _ in range(self.agent_count)
        ]

        print(f"Submitted {len(tasks)} tasks")

        print("Waiting for Ray results...")

        results = ray.get(tasks)

        print("Ray results received")

        return results