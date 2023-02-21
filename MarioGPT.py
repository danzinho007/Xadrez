from mario_gpt import MarioLM, SampleOutput

# pretrained_model = shyamsn97/Mario-GPT2-700-context-length

mario_lm = MarioLM()

# use cuda to speed stuff up
# import torch
# device = torch.device('cuda')
# mario_lm = mario_lm.to(device)

prompts = ["many pipes, many enemies, some blocks, high elevation"]

# generate level of size 1400, pump temperature up to ~2.4 for more stochastic but playable levels
generated_level = mario_lm.sample(
    prompts=prompts,
    num_steps=1400,
    temperature=2.0,
    use_tqdm=True
)

# show string list
generated_level.level

# show PIL image
generated_level.img

# save image
generated_level.img.save("generated_level.png")

# save text level to file
generated_level.save("generated_level.txt")

# play in interactive
generated_level.play()

# run Astar agent
generated_level.run_astar()

# load from text file
loaded_level = SampleOutput.load("generated_level.txt")

# play from loaded (should be the same level that we generated)
loaded_level.play()
...
