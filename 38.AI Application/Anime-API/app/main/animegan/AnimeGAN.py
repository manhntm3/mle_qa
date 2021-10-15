import torch
import cv2
import numpy as np
import os

from .model import Generator

torch.backends.cudnn.enabled = False
torch.backends.cudnn.benchmark = False
torch.backends.cudnn.deterministic = True
    
from .test import load_image

class AnimeGAN:
    def __init__(self):
        self.model_path = "/home/manh/Learning/Python/Anime-API/app/main/animegan/pytorch_generator_Paprika.pt"
        self.device = "cpu"
        self.net = Generator()
        self.net.load_state_dict(torch.load(self.model_path, map_location="cpu"))
        self.net.to(self.device).eval()

    def runInference(self, image_path, output_path):
        image_np = load_image(image_path, True)
        image = torch.from_numpy(image_np)
        image = image/127.5 - 1.0
        print(f"image loaded: {image_path}")

        with torch.no_grad():
            input = image.permute(2, 0, 1).unsqueeze(0).to(self.device)
            out = self.net(input, False).squeeze(0).permute(1, 2, 0).cpu().numpy()
            out = (out + 1)*127.5
            out = np.clip(out, 0, 255).astype(np.uint8)

        out = cv2.resize(out, dsize=(image_np.shape[1], image_np.shape[0]), interpolation=cv2.INTER_CUBIC)
        out = np.concatenate((image_np, out), axis=1)

        cv2.imwrite(os.path.join(output_path), cv2.cvtColor(out, cv2.COLOR_BGR2RGB))
        print(f"image saved: {output_path}")