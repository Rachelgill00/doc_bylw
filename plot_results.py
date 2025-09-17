import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 读取实验结果 CSV
df = pd.read_csv("results_template.csv")

# 统一画图风格
sns.set(style="whitegrid", font_scale=1.2)

# --------- 1. TPS vs b (不同协同规模 c) ----------
plt.figure(figsize=(8,5))
sns.lineplot(
    data=df,
    x="b", y="tps",
    hue="c",
    style="S",
    markers=True, dashes=False
)
plt.title("TPS vs Byzantine Node Count (不同协同规模)")
plt.xlabel("Byzantine Node Count (b)")
plt.ylabel("TPS")
plt.legend(title="协同规模 c")
plt.tight_layout()
plt.savefig("tps_vs_b.png")
plt.close()

# --------- 2. p95/p99 延迟 vs b ----------
plt.figure(figsize=(8,5))
sns.lineplot(data=df, x="b", y="lat_p95_ms", hue="S", markers=True, dashes=False)
sns.lineplot(
    data=df,
    x="b",
    y="lat_p99_ms",
    hue="S",
    style="S",        # 根据 S 分组自动给不同线型
    markers=True,
    dashes=False      # 或 True，让 seaborn 自动管理
)

plt.title("p95 / p99 延迟 vs Byzantine Node Count")
plt.xlabel("Byzantine Node Count (b)")
plt.ylabel("Latency (ms)")
plt.tight_layout()
plt.savefig("latency_p95_p99_vs_b.png")
plt.close()

# --------- 3. 正确区块提交率 vs b ----------
plt.figure(figsize=(8,5))
sns.lineplot(
    data=df,
    x="b", y="commit_ratio",
    hue="S",
    style="c",
    markers=True, dashes=False
)
plt.title("正确区块提交率 vs Byzantine Node Count")
plt.xlabel("Byzantine Node Count (b)")
plt.ylabel("Commit Ratio")
plt.ylim(0,1.05)
plt.tight_layout()
plt.savefig("commit_ratio_vs_b.png")
plt.close()

# --------- 4. 协同覆盖率 κ 与 有效度 ε ----------
fig, axes = plt.subplots(1, 2, figsize=(12,5))
sns.lineplot(data=df, x="b", y="kappa", hue="S", markers=True, dashes=False, ax=axes[0])
axes[0].set_title("协同覆盖率 κ vs b")
axes[0].set_ylim(0,1)
axes[0].set_xlabel("Byzantine Node Count (b)")
axes[0].set_ylabel("κ")

sns.lineplot(data=df, x="b", y="epsilon", hue="S", markers=True, dashes=False, ax=axes[1])
axes[1].set_title("协同有效度 ε vs b")
axes[1].set_xlabel("Byzantine Node Count (b)")
axes[1].set_ylabel("ε")

plt.tight_layout()
plt.savefig("kappa_epsilon_vs_b.png")
plt.close()

print("✅ 所有图表已生成: tps_vs_b.png, latency_p95_p99_vs_b.png, commit_ratio_vs_b.png, kappa_epsilon_vs_b.png")
