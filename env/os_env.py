
import docker
import gymnasium as gym 

client = docker.from_env()

container = client.containers.get("587902f177a3")
cmd = "sh -c 'cd .. && ls'"
result = container.exec_run(cmd)
print(result.output.decode())


class OsEnv(gym.Env):
    def __init__(self, container_id:int, port:int, container_name:str, container_version:int):
