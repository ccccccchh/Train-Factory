🐟 整体流程

    git clone https://github.com/ccccccchh/Train-Factory.git

    cd ../../Train-Factory

    pip install -e .

    python src/webui.py


🦄 1.1 基座模型

     https://huggingface.co/

🦐 1.2 数据集收集

    示例 https://github.com/ccccccchh/Train-Factory/blob/main/data/fintech.json
  
    放入data下
    并在数据注册文件添加，如下示例代码：
  
      "fintech": {
      "file_name": "fintech.json",
      "columns": {
        "prompt": "instruction",
        "query": "input",
        "response": "output",
        "history": "history"
      }
    }
    
  
🌐 2.3 启动 Web UI

    cd Train-Factory
    python src/webui.py


🦓 2.4 配置文件

    cutoff_len: 1024
    dataset: fintech,identity
    dataset_dir: data
    do_train: true
    finetuning_type: lora
    flash_attn: auto
    fp16: true
    gradient_accumulation_steps: 8
    learning_rate: 0.0002
    logging_steps: 5
    lora_alpha: 16
    lora_dropout: 0
    lora_rank: 8
    lora_target: q_proj,v_proj
    lr_scheduler_type: cosine
    max_grad_norm: 1.0
    max_samples: 1000
    num_train_epochs: 10.0
    optim: adamw_torch
    packing: false
    per_device_train_batch_size: 2
    plot_loss: true
    preprocessing_num_workers: 16
    report_to: none
    save_steps: 100
    stage: sft
    use_unsloth: true
    warmup_steps: 0
    

🔢 2.5 模型量化

    模型量化（Model Quantization）是一种将模型的参数和计算从高精度（通常是 32 位浮点数，FP32）转换为低精度（如 16 位浮点数，FP16，或者 8 位整数，INT8）的过程。
    

🛠️ 2.6 模型合并

    将 base model 与训练好的 LoRA Adapter 合并成一个新的模型。⚠️ 不要使用量化后的模型或 `quantization_bit` 参数来合并 LoRA 适配器。
