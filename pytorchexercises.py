import numpy
import torch

if torch.cuda.is_available():
    device = torch.device("cuda")
    x = torch.ones(5,device=device)
    print(x)
