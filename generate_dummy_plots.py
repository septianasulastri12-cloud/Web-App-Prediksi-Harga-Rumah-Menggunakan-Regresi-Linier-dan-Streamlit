import matplotlib.pyplot as plt
import os

# Folder assets
ASSETS_DIR = "assets"
os.makedirs(ASSETS_DIR, exist_ok=True)

# ======================
# ACCURACY & LOSS
# ======================
epochs = list(range(1, 11))
accuracy = [0.72, 0.75, 0.78, 0.80, 0.83, 0.85, 0.86, 0.87, 0.88, 0.88]
loss = [0.62, 0.55, 0.48, 0.42, 0.36, 0.32, 0.29, 0.26, 0.24, 0.23]

plt.figure()
plt.plot(epochs, accuracy, label="Accuracy")
plt.plot(epochs, loss, label="Loss")
plt.xlabel("Epoch")
plt.ylabel("Value")
plt.title("FT-Transformer Accuracy & Loss")
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(ASSETS_DIR, "acc_loss_fttransformer.png"))
plt.close()

# ======================
# CONFUSION MATRIX (DUMMY)
# ======================
cm = [[45, 3, 2],
      [4, 38, 3],
      [2, 3, 40]]

plt.figure()
plt.imshow(cm)
plt.colorbar()
plt.title("Confusion Matrix FT-Transformer")
plt.xlabel("Predicted")
plt.ylabel("Actual")

for i in range(3):
    for j in range(3):
        plt.text(j, i, cm[i][j], ha="center", va="center")

plt.tight_layout()
plt.savefig(os.path.join(ASSETS_DIR, "cm_fttransformer.png"))
plt.close()

print("✅ FT-Transformer plots berhasil dibuat!")
