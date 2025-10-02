import matplotlib.pyplot as plt

# 五组实验数据 (TPS, Latency)
data = {
    "baseline(c=b=0)": [
        (132,3.035),(220,2.43),(255,2.558),(280,2.405),(290,2.596),(286,3.127),(312,2.613),(307,3.162),
        (309,3.032),(321,2.995),(315,3.003),(321,3.051),(312,3.388),(316,3.322),(319,3.266),(315,3.298),
        (311,3.854),(315,2.859),(310,3.445),(306,3.565),(299,3.95),(306,3.687),(305,3.326),(296,3.933),
        (292,4.673),(296,3.58),(288,4.281),(283,4.953),(288,4.06),(281,4.097),(276,4.917),(277,4.499),
        (274,3.987)
    ],
    "DEY-EDG1(f=33, b=33, c=33)": [
        (141,2.83),(200,2.863),(235,2.79),(268,2.51),(283,2.756),(282,3.064),(289,3.327),(302,2.769),
        (306,2.563),(307,2.897),(311,3.036),(311,2.937),(319,2.757),(315,3.198),(311,3.498),(313,3.299),
        (315,3.048),(316,2.93),(312,3.487),(314,3.411),(315,2.824),(315,2.91)
    ],
    "DEY-EDG2(f=33, b=33, c=33(c1=16, c2=17))": [
        (129,3.096),(207,2.7),(222,2.954),(237,3.336),(257,3.115),(239,4.214),(252,4.026),(261,3.093),
        (259,3.322),(267,3.309),(273,3.082),(249,4.89)
    ]
}

fig, axes = plt.subplots(2, 1, figsize=(10,8), sharex=True)
colors = ['b','g','r']

for i,(label,vals) in enumerate(data.items()):
    x = list(range(1, len(vals)+1))  # 模拟blockheight为顺序编号
    tps = [v[0] for v in vals]
    lat = [v[1] for v in vals]
    axes[0].plot(x, tps, marker='o', label=label, color=colors[i % len(colors)])
    axes[1].plot(x, lat, marker='o', label=label, color=colors[i % len(colors)])
    # 在最后一个blockheight处画竖线并标注
    axes[0].axvline(x[-1], color=colors[i % len(colors)], linestyle='--', alpha=0.3)
    axes[1].axvline(x[-1], color=colors[i % len(colors)], linestyle='--', alpha=0.3)
    axes[0].text(x[-1], max(tps)*0.95, f"{x[-1]}", color=colors[i % len(colors)], ha='right')
    axes[1].text(x[-1], max(lat)*0.95, f"{x[-1]}", color=colors[i % len(colors)], ha='right')

axes[0].set_ylabel("TPS")
axes[1].set_ylabel("Latency (s)")
axes[0].set_xlabel("Block Height (sequential index)")  # 上图也加横轴
axes[1].set_xlabel("Block Height (sequential index)")  # 下图保持

axes[0].legend()
axes[0].set_title("TPS and Latency vs Blockheight for different DEY-EDG experiments")

plt.tight_layout()
plt.savefig("deg_edg.png")
