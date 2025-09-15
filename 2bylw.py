import numpy as np
import matplotlib.pyplot as plt

# x axis: Byzantine proportions (%)
props = np.array([0, 5, 10, 15, 20, 25, 30, 33])

# ------------------------------
# 1. TPS for all fault scenarios
# ------------------------------
tps = {
    "baseline": np.array([1000]*8),
    "equiv_single": np.array([1000,995,990,980,965,940,900,880]),
    "equiv_collude": np.array([1000,950,900,820,720,620,520,480]),
    "delay_border": np.array([1000,980,960,920,880,820,700,640]),
    "delay_trigger": np.array([1000,940,860,760,640,500,360,320]),
    "dos_single": np.array([1000,990,980,970,940,900,820,780]),
    "dos_collude": np.array([1000,930,820,680,520,360,220,180]),
    "net_loss": np.array([1000,985,970,940,900,840,760,720]),
}

plt.figure(figsize=(8,4.5))
for k,v in tps.items():
    plt.plot(props, v, marker='o', label=k)
plt.title("TPS vs Byzantine proportion (all fault scenarios)")
plt.xlabel("Byzantine proportion (%)")
plt.ylabel("TPS (tx/s)")
plt.grid(True)
plt.legend(fontsize='small', ncol=2)
plt.tight_layout()
plt.savefig("fig1_tps.png")
# plt.show()

# ------------------------------
# 2. Committed-correct ratio (baseline vs collusive)
# ------------------------------
commit_ratio = {
    "baseline": np.array([1.0]*8),
    "equiv_collude": np.array([1.0,0.995,0.985,0.96,0.91,0.85,0.72,0.65]),
}

plt.figure(figsize=(8,4))
for k,v in commit_ratio.items():
    plt.plot(props, v, marker='o', label=k)
plt.title("Committed-correct ratio vs Byzantine proportion")
plt.xlabel("Byzantine proportion (%)")
plt.ylabel("Committed-correct ratio")
plt.ylim(0,1.02)
plt.grid(True)
plt.legend(fontsize='small', ncol=2)
plt.tight_layout()
plt.savefig("fig2_commit_ratio.png")
# plt.show()

# ------------------------------
# 3. Latency comparison (p95 and p99) for baseline vs delayed attacks
# ------------------------------
p95 = {
    "baseline": np.array([300]*8),
    "delay_border": np.array([300,420,540,700,920,1150,1350,1500]),
    "delay_trigger": np.array([300,480,700,1000,1500,2200,3000,3500]),
}

p99 = {
    "baseline": np.array([450]*8),
    "delay_border": np.array([450,620,800,1100,1500,2000,2600,3000]),
    "delay_trigger": np.array([450,800,1100,1600,2400,3400,4500,5200]),
}

# p95
plt.figure(figsize=(8,4))
for k,v in p95.items():
    plt.plot(props, v, marker='o', label=k)
plt.title("p95 latency vs Byzantine proportion")
plt.xlabel("Byzantine proportion (%)")
plt.ylabel("p95 latency (ms)")
plt.grid(True)
plt.legend(fontsize='small', ncol=2)
plt.tight_layout()
plt.savefig("fig3_p95.png")
# plt.show()

# p99
plt.figure(figsize=(8,4))
for k,v in p99.items():
    plt.plot(props, v, marker='o', label=k)
plt.title("p99 latency vs Byzantine proportion")
plt.xlabel("Byzantine proportion (%)")
plt.ylabel("p99 latency (ms)")
plt.grid(True)
plt.legend(fontsize='small', ncol=2)
plt.tight_layout()
plt.savefig("fig3_p99.png")
# plt.show()

# ------------------------------
# 4. View-change counts (baseline vs collusive)
# ------------------------------
view_change = {
    "baseline": np.array([0]*8),
    "equiv_collude": np.array([0,2,4,6,9,12,16,20]),
}

plt.figure(figsize=(8,4))
for k,v in view_change.items():
    plt.plot(props, v, marker='o', label=k)
plt.title("View-change count vs Byzantine proportion")
plt.xlabel("Byzantine proportion (%)")
plt.ylabel("View-change count")
plt.grid(True)
plt.legend(fontsize='small', ncol=2)
plt.tight_layout()
plt.savefig("fig4_view_change.png")
# plt.show()
