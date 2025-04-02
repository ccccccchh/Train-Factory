import torch

def check_cuda_connection():
    if torch.cuda.is_available():
        print("CUDA is available.")
        device = torch.device("cuda:0")
        print(f"Using device: {device}")
        # 可以进一步检查GPU的属性，例如名称
        print(f"GPU Name: {torch.cuda.get_device_name(0)}")
    else:
        print("CUDA is not available.")

def select_cuda():
    print("cuda版本：" + torch.version.cuda)

if __name__ == "__main__":
    check_cuda_connection()
    select_cuda()
