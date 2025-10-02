import matplotlib.pyplot as plt

# 三个维度点
points = {
    "Safety": (0, 1),
    "Liveness": (-0.87, -0.5),
    "Robustness": (0.87, -0.5)
}

fig, ax = plt.subplots(figsize=(6,6))

# 画三角形
triangle = plt.Polygon(list(points.values()), fill=None, edgecolor='black', linewidth=1.5)
ax.add_patch(triangle)

# 添加点和标签
for label, (x,y) in points.items():
    ax.plot(x, y, 'o', markersize=8, color='black')
    ax.text(x*1.15, y*1.15, label, ha='center', va='center', fontsize=12, weight='bold')

# 在中心加一个说明
ax.text(0, 0, "BFT Consensus\nSystem Quality", 
        ha='center', va='center', fontsize=11, color='darkred')

ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-1.2, 1.2)
ax.set_aspect('equal')
ax.axis('off')

plt.title("Safety - Liveness - Robustness Triangle", fontsize=13, weight='bold')
plt.tight_layout()
plt.savefig("slr.png")
# plt.show()