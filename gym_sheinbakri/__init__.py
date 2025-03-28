from gym.envs.registration import register

register(
    id='SheinBakri-v0',
    entry_point='gym_sheinbakri.sheinbakri_env:SheinBakriEnv',
)