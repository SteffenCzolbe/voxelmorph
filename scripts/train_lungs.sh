python -m scripts.pytorch.train datadir --model-dir ./checkpoints/run --gpu 0,1 --batch_size 2 --epochs 1500 --steps_per_epoch 100 --image_loss mse --lambda 0.05