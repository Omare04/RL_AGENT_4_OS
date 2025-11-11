from gymnasium.envs.registration import register

register(
    id="os_env/GridWorld-v0",
    entry_point="os_env.envs:GridWorldEnv",
)
