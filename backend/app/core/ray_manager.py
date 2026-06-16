import ray


def initialize_ray():

    if not ray.is_initialized():

        ray.init(
            ignore_reinit_error=True
        )