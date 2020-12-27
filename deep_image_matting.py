import torch

def get_dim_model(path, device):
    checkpoint = torch.load(path)
    model = checkpoint['model'].module
    model = model.to(device)
    model.eval()
    return model
